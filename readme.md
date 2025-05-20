# Danish Pollen (`pollen_dk`)

Custom Home Assistant integration that provides daily pollen forecasts for Denmark.  
Supports East and West Denmark regions, with sensors for multiple pollen types.

---

## 📦 Installation

### Option 1: Manual

1. Copy the `pollen_dk` folder into:
config/custom_components/

2. Restart Home Assistant.

3. Go to **Settings → Devices & Services → Add Integration**, search for **Danish Pollen**, and follow the setup.

---

### Option 2: HACS (Recommended)

1. In HACS, go to **Integrations → 3-dot menu → Custom repositories**.

2. Add this repository URL as an integration:
https://github.com/JBoye/pollen_dk

3. Click **Add**, then install **Danish Pollen** from HACS.

4. Restart Home Assistant and add the integration via **Settings → Devices & Services**.

---

## 🧾 Features

- One sensor per pollen type
- Numeric pollen level as sensor `state`
- Attributes include:
- `severity`: low, medium, high
- `predictions`: upcoming values sorted by date
- `in_season`, `is_ml`, `source_date`, etc.

No API key required.

---

## 🧰 Supported Pollen Types

- birk (birch)
- bynke
- el (alder)
- elm
- græs (grass)
- hassel (hazel)
- alternaria
- cladosporium