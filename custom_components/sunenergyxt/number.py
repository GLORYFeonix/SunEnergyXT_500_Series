from .const import DOMAIN
from .coordinator import SunlitDataUpdateCoordinator

import async_timeout
import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from homeassistant.components.number import (
    NumberEntity,
    NumberMode
)

from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)

NUMBER_META: dict[str, dict[str, Any]] = {
    "GS": {
        "min_value": -2400,
        "max_value": 2400,
        "step": 10,
        "unit": "W",
    },
    "IS": {
        "min_value": 1,
        "max_value": 2400,
        "step": 10,
        "unit": "W",
    },
    "SI": {
        "min_value": 1,
        "max_value": 30,
        "step": 1,
        "unit": "%",
    },
    "SA": {
        "min_value": 70,
        "max_value": 100,
        "step": 1,
        "unit": "%",
    },
    "SO": {
        "min_value": 1,
        "max_value": 30,
        "step": 1,
        "unit": "%",
    },
    "PT": {
        "min_value": 30,
        "max_value": 1440,
        "step": 1,
        "unit": "min",
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

    entities: list[NumberEntity] = []

    keys = [
        "GS",
        "IS",
        "SI",
        "SA",
        "SO",
        "PT",
    ]

    for key in keys:
        entities.append(
            SunlitNumber(
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

class SunlitNumber(CoordinatorEntity[SunlitDataUpdateCoordinator], NumberEntity):
    _attr_has_entity_name = True
    _attr_mode = NumberMode.SLIDER

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

        meta = NUMBER_META.get(key, {})

        self._attr_unique_id = f"{DOMAIN}_{entry_id}_{key}"
        self._attr_translation_key = key.lower()
        self._attr_device_info = device_info

        min_value = meta.get("min_value")
        if min_value:
            self._attr_native_min_value = min_value

        max_value = meta.get("max_value")
        if max_value:
            self._attr_native_max_value = max_value

        if device_info["model"] == "SunEnergyXT 500":
            if self._key == "GS":
                self._attr_native_max_value = 800
            if self._key == "IS":
                self._attr_native_max_value = 800            
        
        step = meta.get("step")
        if step:
            self._attr_native_step = step

        unit = meta.get("unit")
        if unit:
            self._attr_native_unit_of_measurement = unit
        
    @property
    def native_value(self) -> float:
        raw = self.coordinator.data.get(self._key)
        if raw is None:
            _LOGGER.warning("None value from device")
            return None
        
        try:
            return float(raw)
        except (TypeError, ValueError):
            _LOGGER.warning("Invalid value from device: %s", raw)
            return None
        
    async def async_set_native_value(self, value: float) -> None:
        value_int = int(
            max(self._attr_native_min_value, min(self._attr_native_max_value, value))
        )
        payload = {
            "state": {
                self._key: value_int
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
                        raise RuntimeError(
                            f"HTTP {resp.status}: {text}"
                        )
        except Exception as err:
            raise

        if isinstance(self.coordinator.data, dict):
            self.coordinator.data[self._key] = value_int

        self.async_write_ha_state()