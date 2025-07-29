# Geospatial Suitability Analysis for Renewable Energy Sites

This project simulates and evaluates site suitability for renewable energy development based on geospatial criteria such as solar irradiance, wind speed, terrain slope, proximity to infrastructure, and land use type. Synthetic data is generated and scored to classify locations into low, moderate, or high suitability.

---

## 📌 Project Overview

Renewable energy planning requires location-based decision-making. This project uses synthetic geospatial data to model the suitability of land for solar or wind energy installations. It assigns a weighted suitability score to each site and classifies them to support planning and decision-making processes.

---

## 🧪 Features Considered

- **Solar Irradiance (kWh/m²/day)** – Energy potential from sunlight.
- **Wind Speed (m/s)** – Usability of wind energy.
- **Land Slope (degrees)** – Flat areas are preferred.
- **Distance to Road/Grid (km)** – Infrastructure access.
- **Land Use Type** – Urban, agricultural, barren, or forest.

---

## 🧮 Methodology

1. **Synthetic Data Generation** (150+ points)
2. **Weighted Scoring Function** for each site
3. **Suitability Classification**:
   - High
   - Moderate
   - Low
4. **Visualization** of classification results

---

## 📊 Dataset

The generated dataset is stored in:

- `renewable_energy_suitability_data.xlsx`

This file includes all input features, computed scores, and classification labels.

---

## 📁 Repository Structure

📦 renewable-energy-suitability
├── renewable_energy_suitability_data.xlsx # Synthetic data
├── suitability_analysis.py # Main Python script
├── README.md # Project description

yaml
Copy
Edit

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/renewable-energy-suitability.git
   cd renewable-energy-suitability
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the analysis script:

bash
Copy
Edit
python suitability_analysis.py
📈 Output
Suitability classification for each site

Visual summary of distribution (bar chart)

Ready-to-use Excel dataset for mapping or further analysis

💡 Future Work
Integrate with GIS platforms (e.g., QGIS, GeoPandas)

Use real-world datasets (NASA, OpenStreetMap, etc.)

Apply machine learning for automated classification

👤 Author
Agbozu Ebingiye Nelvin
Email: [nelvinebingiye@gmail.com]
GitHub: [github.com/nelvinebi]
