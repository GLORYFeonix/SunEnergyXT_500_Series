from .const import DOMAIN
from .coordinator import SunlitDataUpdateCoordinator

import async_timeout
import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from homeassistant.components.switch import (
    SwitchEntity,
    SwitchDeviceClass
)

from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)

SWITCH_META: dict[str, dict[str, Any]] = {
    "LM": {
        "device_class": SwitchDeviceClass.OUTLET,
    },
    "MM": {
        "device_class": SwitchDeviceClass.OUTLET,
    },
    "PM": {
        "device_class": SwitchDeviceClass.OUTLET,
    },
}

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    config = hass.data[DOMAIN][entry.entry_id]
    sn = config["sn"]
    ip = config["ip"]
    model = config["model"]
    coordinator = config["coordinator"]

    device_info = DeviceInfo(
        identifiers={(DOMAIN, entry.entry_id)},
        name=sn,
        manufacturer="SunEnergyXT",
        model=model,
        serial_number=sn,
    )

    entities: list[SwitchEntity] = []

    keys = [
        "LM",
        "MM",
        "PM",
    ]

    for key in keys:
        entities.append(
            SunlitSwitch(
                coordinator=coordinator,
                entry_id=entry.entry_id,
                key=key,
                sn=sn,
                ip=ip,
                device_info=device_info,
                hass=hass
            )
        )

    async_add_entities(entities, True)

class SunlitSwitch(CoordinatorEntity[SunlitDataUpdateCoordinator], SwitchEntity):
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: SunlitDataUpdateCoordinator,
        entry_id: str,
        key: str,
        sn: str,
        ip: str,
        device_info: DeviceInfo,
        hass: HomeAssistant,
    ) -> None:
        super().__init__(coordinator)
        self._key = key
        self._sn = sn
        self._ip = ip
        self._session = async_get_clientsession(hass)

        meta = SWITCH_META.get(key, {})

        self._attr_unique_id = f"{DOMAIN}_{entry_id}_{key}"
        self._attr_translation_key = key.lower()
        self._attr_device_info = device_info
        self._attr_is_on = True

        device_class = meta.get("device_class")
        if device_class:
            self._attr_device_class = device_class

    @property
    def is_on(self) -> bool:
        raw = self.coordinator.data.get(self._key)
        return bool(int(raw)) if raw is not None else False

    async def async_turn_on(self, **kwargs):
        await self._async_write_switch(True)

    async def async_turn_off(self, **kwargs):
        await self._async_write_switch(False)

    async def _async_write_switch(self, is_on: bool) -> None:
        value = 1 if is_on else 0
        payload = {
            "state": {
                self._key: value
            }
        }
        try:
            async with async_timeout.timeout(5):
                async with self._session.post(
                    # f"http://SunEnergyXT_AIO_{self._sn}.local/write",
                    f"http://{self._ip}/write",
                    json=payload,
                ) as resp:
                    if resp.status != 200:
                        text = await resp.text()
                        raise RuntimeError(f"HTTP {resp.status}: {text}")
        except Exception as err:
            _LOGGER.error("Error writing switch %s: %s", self._key, err)
            raise

        if isinstance(self.coordinator.data, dict):
            self.coordinator.data[self._key] = value
        self.async_write_ha_state()