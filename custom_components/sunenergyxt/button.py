from .const import DOMAIN
from .coordinator import SunlitDataUpdateCoordinator

import async_timeout
import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from homeassistant.components.button import (
    ButtonEntity,
    ButtonDeviceClass
)

from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)

BUTTON_META: dict[str, dict[str, Any]] = {
    "RT": {
        "device_class": ButtonDeviceClass.RESTART,
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

    entities: list[ButtonEntity] = []

    keys = [
        "RT",
    ]

    for key in keys:
        entities.append(
            SunlitButton(
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

class SunlitButton(CoordinatorEntity[SunlitDataUpdateCoordinator], ButtonEntity):
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

        meta = BUTTON_META.get(key, {})

        self._attr_unique_id = f"{DOMAIN}_{entry_id}_{key}"
        self._attr_translation_key = key.lower()
        self._attr_device_info = device_info

        device_class = meta.get("device_class")
        if device_class:
            self._attr_device_class = device_class

    async def async_press(self) -> None:
        payload = {
            "state": {
                self._key: 1
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
            _LOGGER.error("Error pressing button %s: %s", self._key, err)
            raise