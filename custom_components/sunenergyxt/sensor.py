from .const import DOMAIN
from .coordinator import SunlitDataUpdateCoordinator

import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from homeassistant.components.sensor import (
    SensorEntity,
    SensorStateClass
)

from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import EntityCategory, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

_LOGGER = logging.getLogger(__name__)

SENSOR_META: dict[str, dict[str, Any]] = {
    "WS": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "WR": {
        "unit": "dB",
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "ST": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "IW": {
        "unit": "W",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "OP": {
        "unit": "W",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "PV": {
        "unit": "W",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "PV1": {
        "unit": "W",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "PV2": {
        "unit": "W",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "PV3": {
        "unit": "W",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "PV4": {
        "unit": "W",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "II1": {
        "unit": "A",
        "scale": 0.1,
        "precision": 1,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "II2": {
        "unit": "A",
        "scale": 0.1,
        "precision": 1,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "II3": {
        "unit": "A",
        "scale": 0.1,
        "precision": 1,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "II4": {
        "unit": "A",
        "scale": 0.1,
        "precision": 1,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "VP1": {
        "unit": "V",
        "scale": 0.1,
        "precision": 1,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "VP2": {
        "unit": "V",
        "scale": 0.1,
        "precision": 1,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "VP3": {
        "unit": "V",
        "scale": 0.1,
        "precision": 1,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "VP4": {
        "unit": "V",
        "scale": 0.1,
        "precision": 1,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "GP": {
        "unit": "W",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "LP": {
        "unit": "W",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "GD1": {
        "unit": "kwh",
        "scale": 0.001,
        "precision": 3,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.TOTAL
    },
    "GD2": {
        "unit": "kwh",
        "scale": 0.001,
        "precision": 3,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.TOTAL
    },
    "LD": {
        "unit": "kwh",
        "scale": 0.001,
        "precision": 3,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.TOTAL
    },
    "SC": {
        "unit": "%",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "SC0": {
        "unit": "%",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "SC1": {
        "unit": "%",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "SC2": {
        "unit": "%",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "SC3": {
        "unit": "%",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "SC4": {
        "unit": "%",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "SC5": {
        "unit": "%",
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "ON": {
        "entity_category": EntityCategory.DIAGNOSTIC,
        "state_class": SensorStateClass.MEASUREMENT
    },
    "ES": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "BS0": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "BS1": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "BS2": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "BS3": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "BS4": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "BS5": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "AS": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "DS": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "SN": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
    "MS": {
        "entity_category": EntityCategory.DIAGNOSTIC,
    },
}

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    config = hass.data[DOMAIN][entry.entry_id]
    sn = config["sn"]
    model = config["model"]
    coordinator = config["coordinator"]

    device_info = DeviceInfo(
        identifiers={(DOMAIN, entry.entry_id)},
        name=sn,
        manufacturer="SunEnergyXT",
        model=model,
        serial_number=sn,
    )

    entities: list[SensorEntity] = []

    keys = [
        "WS",
        "WR",
        "ST",
        "IW",
        "OP",
        "PV",
        "PV1",
        "PV2",
        "PV3",
        "PV4",
        "II1",
        "II2",
        "II3",
        "II4",
        "VP1",
        "VP2",
        "VP3",
        "VP4",
        "GP",
        "LP",
        "GD1",
        "GD2",
        "LD",
        "SC",
        "SC0",
        "SC1",
        "SC2",
        "SC3",
        "SC4",
        "SC5",
        "ON",
        "ES",
        "BS0",
        "BS1",
        "BS2",
        "BS3",
        "BS4",
        "BS5",
        "AS",
        "DS",
        "SN",
        "MS",
    ]

    for key in keys:
        entities.append(
            SunlitSensor(
                coordinator=coordinator,
                entry_id=entry.entry_id,
                key=key,
                device_info=device_info,
            )
        )

    async_add_entities(entities, True)

class SunlitSensor(
    CoordinatorEntity[SunlitDataUpdateCoordinator],
    SensorEntity,
):
    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(
        self,
        coordinator: SunlitDataUpdateCoordinator,
        entry_id: str,
        key: str,
        device_info: DeviceInfo,
    ) -> None:
        super().__init__(coordinator)

        self._key = key
        meta = SENSOR_META.get(key, {})
        self._scale: float | None = meta.get("scale")
        self._precision: int | None = meta.get("precision")

        self._attr_unique_id = f"{DOMAIN}_{entry_id}_{key}"
        self._attr_translation_key = key.lower()
        self._attr_device_info = device_info

        state_class = meta.get("state_class")
        if state_class:
            self._attr_state_class = state_class

        unit = meta.get("unit")
        if unit:
            self._attr_native_unit_of_measurement = unit

    @property
    def native_value(self) -> Any:
        raw = self.coordinator.data.get(self._key)
        if raw is None:
            return None

        if self._scale is None:
            return raw

        try:
            val = float(raw) * self._scale
            if self._precision is not None:
                val = round(val, self._precision)
            return val
        except (TypeError, ValueError):
            return raw
        
    @property
    def extra_state_attributes(self):
        attrs = {}
        if self.coordinator.last_success_time:
            attrs["last_report_time"] = self.coordinator.last_success_time.isoformat()
        return attrs
