# Agricultural Datasets

This directory contains datasets used throughout the probability and statistics learning modules.

## Overview

All datasets are designed for educational purposes, focusing on agricultural applications. They help you understand statistical concepts through real-world farming scenarios.

## Dataset Categories

### Crop Yield Data (`crop_yield/`)
Historical crop yield information for various crops, locations, and seasons.

**Planned datasets:**
- Wheat yield across different regions
- Corn production data with weather variables
- Multi-crop yield comparisons

**Features will include:**
- Crop type
- Year/season
- Location (region, coordinates)
- Yield (tons/hectare or bushels/acre)
- Environmental factors (rainfall, temperature, etc.)

### Weather Data (`weather/`)
Historical and simulated weather patterns relevant to agricultural decisions.

**Planned datasets:**
- Daily temperature and rainfall records
- Growing season weather summaries
- Extreme weather event occurrences

**Features will include:**
- Date
- Temperature (min, max, average)
- Precipitation
- Humidity
- Solar radiation
- Wind speed

### Soil Samples (`soil_samples/`)
Soil test results from various agricultural fields.

**Planned datasets:**
- Soil chemistry analysis (NPK, pH, micronutrients)
- Soil texture classification
- Organic matter content

**Features will include:**
- Sample ID and location
- pH level
- Macronutrients (N, P, K)
- Micronutrients (Fe, Zn, Cu, Mn, etc.)
- Organic matter percentage
- Texture (sand, silt, clay percentages)

## Data Sources

Datasets in this repository are:
1. **Synthetic data**: Generated for educational clarity
2. **Open agricultural databases**: USDA, FAO, public research datasets
3. **Anonymized real data**: From agricultural research (where permissions obtained)

All datasets are used for educational purposes only.

## Usage Guidelines

### Loading Data

Most datasets are provided in CSV format:

```python
import pandas as pd

# Load crop yield data
crop_data = pd.read_csv('datasets/crop_yield/wheat_yields.csv')

# Load weather data
weather_data = pd.read_csv('datasets/weather/daily_weather.csv')

# Load soil samples
soil_data = pd.read_csv('datasets/soil_samples/soil_chemistry.csv')
```

### Dataset Conventions

- Missing values are marked as `NaN` or `-999`
- Dates follow ISO format: `YYYY-MM-DD`
- Units are specified in column names or metadata
- Categorical variables use clear labels

## Status

**Current**: This is a placeholder. Datasets will be added as topics are developed.

**Coming Soon**:
- Sample probability datasets for Topic 01
- Distribution examples for Topic 03
- Time series data for Topic 08

## Contributing Datasets

If you have agricultural datasets suitable for educational use:
1. Ensure you have rights to share the data
2. Anonymize any sensitive information
3. Document the features clearly
4. Open an issue or pull request

## Agricultural Context

These datasets help answer questions like:
- What's the probability of crop failure given weather conditions?
- How do soil properties vary across a region?
- What's the expected yield for next season?
- How reliable are our production estimates?
- What factors most influence crop outcomes?

---

**Note**: As this repository develops, this README will be updated with specific dataset information, download instructions, and detailed feature descriptions.
