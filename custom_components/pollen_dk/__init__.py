from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.exceptions import ConfigEntryNotReady
import aiohttp
import json

from .const import DOMAIN, POLLEN_URL

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(POLLEN_URL) as response:
                raw_data = await response.text()
                json.loads(json.loads(raw_data))  # sanity check
    except Exception as e:
        raise ConfigEntryNotReady(f"Initial pollen data not available: {e}")

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True
