from .const import DOMAIN, HOST_PREFIX, HOST_SUFFIX

from typing import Any

import ipaddress
import logging

import voluptuous as vol
import aiohttp
import async_timeout

from homeassistant import config_entries, exceptions
from homeassistant.data_entry_flow import FlowResult, AbortFlow
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo

_LOGGER = logging.getLogger(__name__)

async def _validate_input(ip: str) -> None:
    try:
        ipaddress.ip_address(ip)
    except ValueError as err:
        raise InvalidIP from err

async def _get_device_info(host: str) -> dict[str, Any]:
    try:
        async with async_timeout.timeout(5):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{host}/read") as resp:
                    if resp.status != 200:
                        raise CannotConnect
                    data = await resp.json()
                    sn = data.get("state", {}).get("reported", {}).get("SN")
                    model = data.get("state", {}).get("reported", {}).get("DevType")
                    if not isinstance(sn, str):
                        raise CannotGetSN
                    if not isinstance(model, str):
                        raise CannotGetModel
                    return {"sn":sn, "model":model}
    except Exception:
        raise CannotConnect

class SunlitConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    MINOR_VERSION = 1

    def __init__(self) -> None:
        self._discovered_sn: str | None = None
        self._discovered_ip: str | None = None
        self._discovered_model: str | None = None

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult:
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                ip = user_input['IP']
                await _validate_input(ip)
                info = await _get_device_info(ip)
                sn = info["sn"]
                model = info["model"]

                await self.async_set_unique_id(sn)
                self._abort_if_unique_id_configured(updates={"ip": ip})
            
            except InvalidIP:
                errors["base"] = "invalid_ip"

            except CannotConnect:
                errors["base"] = "cannot_connect"

            except CannotGetSN:
                errors["base"] = "cannot_get_sn"

            except CannotGetModel:
                errors["base"] = "cannot_get_model"

            except AbortFlow as af:
                reason = getattr(af, "reason", str(af))
                if reason == "already_configured":
                    errors["base"] = "already_configured"
                elif reason == "already_in_progress":
                    errors["base"] = "already_in_progress"
                else:
                    raise

            except Exception as err:
                _LOGGER.exception("Unexpected error during user step: %s", err)
                errors["base"] = "unknown"

            if not errors:
                return self.async_create_entry(
                    title=model,
                    data={
                        "ip": ip,
                        "sn": sn,
                        "model": model,
                    },
                )

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({vol.Required("IP"): str}), errors=errors,
        )
    
    async def async_step_zeroconf(self, discovery_info:ZeroconfServiceInfo) -> FlowResult:
        hostname = (discovery_info.hostname or "").rstrip(".")
        if not (
            hostname.startswith(HOST_PREFIX)
            and hostname.endswith(HOST_SUFFIX)
        ):
            return self.async_abort(reason="not_device")

        sn = hostname[len(HOST_PREFIX) : -len(HOST_SUFFIX)]
        ip = str(discovery_info.host)
        model = discovery_info.properties["model"]

        await self.async_set_unique_id(sn)
        self._abort_if_unique_id_configured(updates={"ip": ip})

        _LOGGER.info("Zeroconf discovery: %s", discovery_info)

        self._discovered_sn = sn
        self._discovered_ip = ip
        self._discovered_model = model

        return await self.async_step_zeroconf_confirm()
    
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult:
        errors: dict[str, str] = {}

        if user_input is not None:
            sn = self._discovered_sn
            ip = self._discovered_ip
            model = self._discovered_model

            try:
                await _validate_input(ip)
                info = await _get_device_info(ip)
                sn = info["sn"]
                model = info["model"]

                await self.async_set_unique_id(sn)
                self._abort_if_unique_id_configured(updates={"ip": ip})

            except CannotConnect:
                return self.async_abort(reason="cannot_connect")

            except CannotGetSN:
                return self.async_abort(reason="cannot_get_sn")

            except CannotGetModel:
                return self.async_abort(reason="cannot_get_model")
            
            except AbortFlow as af:
                reason = getattr(af, "reason", str(af))
                if reason == "already_configured":
                    return self.async_abort(reason="already_configured")
                else:
                    raise

            except Exception as err:
                _LOGGER.exception("Unexpected error during zeroconf step: %s", err)
                return self.async_abort(reason="unknown")

            return self.async_create_entry(
                title=model,
                data={
                    "ip": ip,
                    "sn": sn,
                    "model": model
                },
            )

        return self.async_show_form(
            step_id="zeroconf_confirm",
            data_schema=vol.Schema({}),
            description_placeholders={
                "sn": self._discovered_sn,
                "host": self._discovered_ip,
            },
            errors=errors,
        )

class InvalidIP(exceptions.HomeAssistantError):
    """Input invalid IP."""

class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""

class CannotGetSN(exceptions.HomeAssistantError):
    """Error to indicate we cannot get SN."""
class CannotGetModel(exceptions.HomeAssistantError):
    """Error to indicate we cannot get Model."""
