import async_timeout
import logging
from typing import Any
from datetime import timedelta, datetime, timezone

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
)

_LOGGER = logging.getLogger(__name__)

class SunlitDataUpdateCoordinator(
    DataUpdateCoordinator[dict[str, Any]]
):
    def __init__(self, hass: HomeAssistant, sn: str, ip: str) -> None:
        self._sn = sn
        self._ip = ip
        self._session = async_get_clientsession(hass)
        super().__init__(
            hass,
            _LOGGER,
            name=f"SunlitMonitor-{sn}",
            update_interval=timedelta(seconds=3),
        )

    async def _async_update_data(self) -> dict[str, Any]:
        try:
            async with async_timeout.timeout(10):
                async with self._session.get(f"http://{self._ip}/read") as resp:
                    if resp.status != 200:
                        raise RuntimeError(f"HTTP status {resp.status}")

                    data = await resp.json()

                    reported = (
                        data.get("state", {})
                        .get("reported", {})
                    )

                    if not isinstance(reported, dict):
                        raise RuntimeError("Invalid 'reported' structure in JSON")

                    self.last_success_time = datetime.now(timezone.utc)
                    _LOGGER.debug("Get raw data: %s", str(data))
                    return reported
        except Exception as err:
            _LOGGER.error("Error updating SunEnergyXT Monitor data: %s", err)
            raise
