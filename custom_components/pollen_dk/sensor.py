import aiohttp
import json
import logging
from datetime import timedelta, date, datetime

from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed, CoordinatorEntity

from .const import (
    DOMAIN, POLLEN_URL, POLLEN_TYPES, REGION_IDS,
    POLLEN_LEVEL_INTERVALS, POLLEN_LEVEL_DESCRIPTION_IDS
)

_LOGGER = logging.getLogger(__name__)


def extract_level(data, region_id, pollen_id):
    try:
        return int(
            data["fields"][str(region_id)]["mapValue"]
            ["fields"]["data"]["mapValue"]
            ["fields"][str(pollen_id)]["mapValue"]
            ["fields"]["level"]["integerValue"]
        )
    except Exception:
        return -1


def classify_level(level, pollen_id):
    thresholds = POLLEN_LEVEL_INTERVALS.get(pollen_id, [0, 1, 2, 3])
    if level < thresholds[1]:
        return "1"
    elif level < thresholds[2]:
        return "2"
    elif level < thresholds[3]:
        return "3"
    else:
        return "3"


async def async_setup_entry(hass, entry, async_add_entities):
    region = entry.data["region"]
    region_id = REGION_IDS[region]
    session = aiohttp.ClientSession()

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="pollen_data",
        update_method=None,
        update_interval=timedelta(hours=3),
    )
    coordinator.data_raw = {}

    async def async_fetch_data():
        try:
            async with session.get(POLLEN_URL) as response:
                raw_data = await response.text()
                parsed_json = json.loads(raw_data)
                data = json.loads(parsed_json)
                coordinator.data_raw = data

                pollen_values = {}
                for pid, name in POLLEN_TYPES.items():
                    val = extract_level(data, region_id, pid)
                    pollen_values[name] = val

                _LOGGER.debug("Parsed pollen values: %s", pollen_values)
                return pollen_values

        except Exception as e:
            raise UpdateFailed(f"Error fetching pollen data: {e}")

    coordinator.update_method = async_fetch_data

    await coordinator.async_request_refresh()

    sensors = [PollenSensor(coordinator, key) for key in coordinator.data]
    async_add_entities(sensors, True)


class PollenSensor(CoordinatorEntity, Entity):
    def __init__(self, coordinator, pollen_type):
        super().__init__(coordinator)
        self._pollen_type = pollen_type

    @property
    def name(self):
        return f"Pollen {self._pollen_type}"

    @property
    def unique_id(self):
        return f"pollen_{self._pollen_type}"

    @property
    def state(self):
        return self.coordinator.data.get(self._pollen_type)
    
    @property
    def icon(self):
        icon_map = {
            "Alternaria": "mdi:bacteria",
            "Birk": "mdi:tree",
            "Bynke": "mdi:flower-pollen",
            "Cladosporium": "mdi:bacteria",
            "El": "mdi:tree",
            "Elm": "mdi:tree",
            "Græs": "mdi:grass",
            "Hassel": "mdi:leaf",
        }
        return icon_map.get(self._pollen_type, "mdi:flower")


    @property
    def extra_state_attributes(self):
        region_key = self.coordinator.config_entry.data["region"]
        region_id = REGION_IDS[region_key]
        today_str = date.today().strftime("%d-%m-%Y")
        data = self.coordinator.data_raw

        attrs = {"type": self._pollen_type}

        try:
            pollen_id = next(k for k, v in POLLEN_TYPES.items() if v == self._pollen_type)
            pollen_info = (
                data["fields"][str(region_id)]["mapValue"]
                ["fields"]["data"]["mapValue"]
                ["fields"][str(pollen_id)]["mapValue"]["fields"]
            )

            level = int(pollen_info.get("level", {}).get("integerValue", -1))
            severity = classify_level(level, pollen_id)

            attrs["in_season"] = pollen_info.get("inSeason", {}).get("booleanValue")
            attrs["level"] = level
            attrs["severity"] = POLLEN_LEVEL_DESCRIPTION_IDS.get(severity, "")
            # attrs["unit_of_measurement"] = "index"
            attrs["source_date"] = today_str

            predictions = pollen_info.get("predictions", {}).get("mapValue", {}).get("fields", {})
            pred_map = {}
            for dkey, val in predictions.items():
                pred_val = val.get("mapValue", {}).get("fields", {}).get("prediction", {}).get("stringValue", "")
                try:
                    pred_map[dkey] = int(pred_val)
                except (ValueError, TypeError):
                    pred_map[dkey] = None
                if dkey == today_str:
                    is_ml = val.get("mapValue", {}).get("fields", {}).get("isML", {}).get("booleanValue")
                    attrs["is_ml"] = is_ml
                    attrs["predicted"] = is_ml

            try:
                sorted_preds = dict(sorted(
                    pred_map.items(),
                    key=lambda x: datetime.strptime(x[0], "%d-%m-%Y")
                ))
                attrs["predictions"] = sorted_preds
            except Exception:
                attrs["predictions"] = pred_map

        except Exception as e:
            _LOGGER.debug(f"Could not extract attributes for {self._pollen_type}: {e}")

        return attrs
