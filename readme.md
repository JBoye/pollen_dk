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

## Sample card (Show all pollen types in season
![Skærmbillede 2025-05-20 kl  13 52 57](https://github.com/user-attachments/assets/d1993b07-2341-42bb-9575-8afb39bf23bf)

```
type: horizontal-stack
cards:
  - type: gauge
    entity: sensor.pollen_birk
    severity:
      green: 0
      yellow: 20
      red: 100
    needle: true
    max: 200
    visibility:
      - condition: state
        entity: sensor.pollen_birk_level
        state_not: out_of_season
  - type: gauge
    entity: sensor.pollen_graes
    needle: true
    min: 0
    max: 60
    severity:
      green: 0
      yellow: 10
      red: 50
    visibility:
      - condition: state
        entity: sensor.pollen_graes_level
        state_not: out_of_season
  - type: gauge
    entity: sensor.pollen_alternaria
    severity:
      green: 0
      yellow: 20
      red: 100
    needle: true
    max: 200
    visibility:
      - condition: state
        entity: sensor.pollen_alternaria_level
        state_not: out_of_season
  - type: gauge
    entity: sensor.pollen_bynke
    severity:
      green: 0
      yellow: 10
      red: 50
    needle: true
    max: 70
    visibility:
      - condition: state
        entity: sensor.pollen_bynke_level
        state_not: out_of_season
  - type: gauge
    entity: sensor.pollen_cladosporium
    severity:
      green: 0
      yellow: 2000
      red: 6000
    needle: true
    max: 7000
    visibility:
      - condition: state
        entity: sensor.pollen_cladosporium_level
        state_not: out_of_season
  - type: gauge
    entity: sensor.pollen_el
    severity:
      green: 0
      yellow: 10
      red: 50
    needle: true
    max: 200
    visibility:
      - condition: state
        entity: sensor.pollen_el_level
        state_not: out_of_season
  - type: gauge
    entity: sensor.pollen_elm
    severity:
      green: 0
      yellow: 10
      red: 50
    needle: true
    max: 80
    visibility:
      - condition: state
        entity: sensor.pollen_elm_level
        state_not: out_of_season
  - type: gauge
    entity: sensor.pollen_hassel
    severity:
      green: 0
      yellow: 5
      red: 15
    needle: true
    max: 40
    visibility:
      - condition: state
        entity: sensor.pollen_hassel_level
        state_not: out_of_season

```

