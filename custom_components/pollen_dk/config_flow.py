from homeassistant import config_entries
from .const import DOMAIN
import voluptuous as vol

class PollenConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Danish Pollen", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("region", default="east"): vol.In({"east": "East Denmark", "west": "West Denmark"})
            })
        )

