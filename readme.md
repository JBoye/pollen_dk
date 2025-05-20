# Pollen DK

A custom Home Assistant integration that provides daily pollen forecasts for Denmark.  
Data is sourced from [Astma-Allergi Danmark](https://www.astma-allergi.dk/).

Created by ChatGPT, with a little help from @JBoye

---

## 📦 Installation

### Option 1: Manual

1. Copy the `pollen_dk` folder into your Home Assistant configuration:
`config/custom_components/pollen_dk`

2. Restart Home Assistant.

3. Go to **Settings → Devices & Services → Add Integration**, search for **Pollen DK**, and follow the setup.

### Option 2: HACS (Recommended)

1. In Home Assistant, open **HACS → Integrations → 3-dot menu → Custom repositories**.

2. Add this repository as a custom integration:
`https://github.com/JBoye/pollen_dk`

3. Search for **Pollen DK** in HACS and install it.

4. Restart Home Assistant, then add the integration via **Settings → Devices & Services**.

---

## 🌿 Features

- One sensor per pollen type
- State shows numeric pollen level
- Attributes include:
- `severity`: low / medium / high
- `in_season`, `is_ml`, `predicted`, `source_date`
- `predictions`: upcoming daily values

---

## 🌾 Supported Pollen Types

- birk (birch)
- bynke (mugwort)
- el (alder)
- elm
- græs (grass)
- hassel (hazel)
- alternaria (fungus)
- cladosporium (fungus)
