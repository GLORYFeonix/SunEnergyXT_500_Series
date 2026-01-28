from __future__ import annotations

from .const import DOMAIN
from .coordinator import SunlitDataUpdateCoordinator

import logging
import aiohttp
import async_timeout

from homeassistant.core import HomeAssistant
from homeassistant.const import Platform
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from homeassistant.exceptions import ConfigEntryNotReady

_LOGGER = logging.getLogger(__name__)
PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.NUMBER, Platform.BUTTON, Platform.SWITCH, Platform.TEXT]

async def _test_connection(ip: str) -> None:
    try:
        async with async_timeout.timeout(5):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{ip}/read") as resp:
                    if resp.status != 200:
                        raise RuntimeError(f"HTTP status {resp.status}")
                    await resp.json()
    except Exception as err:
        raise RuntimeError(f"Cannot connect to device at {ip}: {err}") from err

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    sn = entry.data.get("sn")
    ip = entry.data.get("ip")
    model = entry.data.get("model")

    try:
        await _test_connection(ip)
    except Exception as err:
        _LOGGER.warning("Device %s (%s) not ready: %s", sn, ip, err)
        raise ConfigEntryNotReady(f"Device not ready: {err}") from err
    
    coordinator = SunlitDataUpdateCoordinator(
        hass=hass,
        sn=sn,
        ip=ip
    )
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = {
        "sn": sn,
        "ip": ip,
        "model": model,
        "coordinator": coordinator
    }
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)

    return unload_ok
