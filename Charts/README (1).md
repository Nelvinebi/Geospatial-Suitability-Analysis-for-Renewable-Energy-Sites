<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Space+Mono&size=22&duration=3000&pause=1000&color=4CAF50&center=true&vCenter=true&width=700&lines=Geospatial+Suitability+Analysis;Renewable+Energy+Site+Selection;Solar+%7C+Wind+%7C+Terrain+%7C+Land+Use" alt="Typing SVG" />

<br/>

<img src="https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Renewable%20Energy%20Site%20Suitability%20Distribution.png" width="520" alt="Suitability Distribution" style="border-radius:12px;"/>

<br/><br/>

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Seaborn-Visualization-4C9BE8?style=for-the-badge"/>
<img src="https://img.shields.io/badge/GIS-Geospatial-4CAF50?style=for-the-badge&logo=qgis&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>

<br/><br/>

> **A data-driven geospatial framework that evaluates land suitability for renewable energy development using environmental and infrastructure-based indicators — computing weighted suitability scores to support solar farm and wind power site selection.**

</div>

---

## 📌 Project Overview

Renewable energy deployment requires informed spatial planning to ensure optimal resource utilization, infrastructure accessibility, and environmental sustainability.

This project simulates geospatial data and applies a **weighted suitability analysis framework** to identify potential locations for renewable energy installations such as **solar farms** and **wind power sites**.

Using Python-based data analysis and visualization techniques, candidate sites are evaluated based on environmental and spatial factors including solar irradiance, wind speed, terrain slope, land use, and proximity to infrastructure.

---

## 🧪 Features Considered

The suitability model evaluates multiple geospatial factors:

<div align="center">

| Feature | Unit | Role in Scoring |
|---|---|---|
| ☀️ Solar Irradiance | kWh/m²/day | Measures solar energy potential at a location |
| 💨 Wind Speed | m/s | Determines viability for wind energy generation |
| ⛰️ Land Slope | degrees | Flatter terrain is preferred for infrastructure |
| 🛣️ Distance to Road/Grid | km | Proximity to infrastructure reduces development cost |
| 🌱 Land Use Type | category | Determines environmental & regulatory suitability |

</div>

---

## 🧮 Methodology

The project follows a simplified geospatial suitability analysis workflow:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  1. Synthetic Data Generation                               │
│     └─ 150+ candidate site records with realistic ranges    │
│                                                             │
│  2. Feature-Based Suitability Scoring                       │
│     └─ Weighted composite score per site                    │
│                                                             │
│  3. Site Classification                                     │
│     ├─ 🟢 High Suitability    (score ≥ 0.70)               │
│     ├─ 🟡 Moderate Suitability (score 0.50–0.69)           │
│     └─ 🔴 Low Suitability     (score < 0.50)               │
│                                                             │
│  4. Data Visualization & Analysis                           │
│     └─ Charts, heatmaps, scatter plots                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Scoring formula:**

$$\text{Score} = 0.3 \times \frac{\text{Solar}}{8} + 0.3 \times \frac{\text{Wind}}{12} + 0.2 \times \left(1 - \frac{\text{Slope}}{30}\right) + 0.1 \times \left(1 - \frac{\text{Road Dist}}{50}\right) \times \text{Land Penalty}$$

---

## 📊 Data Visualizations

<details open>
<summary><b>1️⃣ Suitability Classification Distribution</b></summary>
<br/>
<div align="center">
<img src="https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Suitability%20Classification.png" width="600" alt="Suitability Classification"/>
</div>

> Displays the number of locations categorized as **High**, **Moderate**, or **Low** suitability.
</details>

---

<details>
<summary><b>2️⃣ Suitability Score Distribution</b></summary>
<br/>
<div align="center">
<img src="https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Distribution%20of%20Suitability%20Score.png" width="600" alt="Score Distribution"/>
</div>

> A histogram showing the spread of calculated suitability scores across candidate locations.
</details>

---

<details>
<summary><b>3️⃣ Feature Influence Analysis</b></summary>
<br/>
<div align="center">
<img src="https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Influence%20of%20Factors%20on%20Site%20Suitability.png" width="600" alt="Feature Influence"/>
</div>

> A bar chart illustrating how environmental variables **correlate** with the final suitability score.
</details>

---

<details>
<summary><b>4️⃣ Solar vs Wind Renewable Resource Relationship</b></summary>
<br/>
<div align="center">
<img src="https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/db29a85f3a0ba99b17f0c6b4f5867e90703e6e6d/Solar%20Vs%20Wind%20Energy%20Potential.png" width="600" alt="Solar vs Wind"/>
</div>

> A scatter plot showing the relationship between solar irradiance and wind speed — identifying areas with **hybrid renewable potential**.
</details>

---

<details>
<summary><b>5️⃣ Feature Correlation Heatmap</b></summary>
<br/>
<div align="center">
<img src="https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Feature%20Correlation%20Matrix.png" width="600" alt="Correlation Heatmap"/>
</div>

> A correlation matrix showing relationships between environmental variables used in the suitability analysis.
</details>

---

## 📂 Dataset

The generated dataset is stored in **`renewable_energy_suitability_data.xlsx`** and includes:

<div align="center">

| Column | Description |
|---|---|
| `solar_irradiance` | Solar energy potential (kWh/m²/day) |
| `wind_speed` | Wind speed at site (m/s) |
| `land_slope` | Terrain slope in degrees |
| `distance_to_road` | Distance to nearest road/grid (km) |
| `land_use_type` | Land classification (barren / agricultural / urban / forest) |
| `suitability_score` | Composite weighted score (0–1) |
| `suitability_class` | High / Moderate / Low |

</div>

> 💡 This dataset can also be imported into **GIS tools** (QGIS, ArcGIS) for further spatial mapping.

---

## 📁 Repository Structure

```
renewable-energy-suitability/
│
├── 📊 renewable_energy_suitability_data.xlsx   # Synthetic geospatial dataset
├── 🐍 suitability_analysis.py                  # Main Python analysis script
└── 📄 README.md                                # Project documentation
```

---

## 🚀 How to Run the Project

**1️⃣ Clone the Repository**
```bash
git clone https://github.com/nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites.git
cd Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites
```

**2️⃣ Install Required Libraries**
```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

**3️⃣ Run the Analysis Script**
```bash
python suitability_analysis.py
```

---

## 📈 Output

The script generates:

- ✅ Suitability **score** for each candidate site
- ✅ Suitability **classification** (High / Moderate / Low)
- ✅ Multiple **visualizations** for exploratory analysis
- ✅ A structured **Excel dataset** ready for GIS analysis

---

## 🌍 Potential Applications

<div align="center">

| Domain | Application |
|---|---|
| ⚡ Energy Planning | Renewable energy site selection & pre-feasibility |
| 🗺️ GIS Studies | Preliminary land suitability mapping |
| 🌿 Environment | Environmental impact & infrastructure planning |
| 🎓 Education | Spatial decision analysis demonstrations |

</div>

---

## 🔮 Future Improvements

- [ ] Integration with real geospatial datasets (**NASA POWER**, **OpenStreetMap**)
- [ ] Implementation of GIS libraries such as **GeoPandas** & **Folium**
- [ ] Machine learning models for automated site classification
- [ ] Development of **interactive spatial maps** (Streamlit / Dash)
- [ ] Multi-criteria decision analysis (**MCDA**) frameworks

---

## 👤 Author

<div align="center">

<img src="https://img.shields.io/badge/Agbozu%20Ebingiye%20Nelvin-Environmental%20Data%20Scientist-4CAF50?style=for-the-badge"/>

**Environmental Data Scientist | GIS | Remote Sensing | Machine Learning**

<br/>

[![Email](https://img.shields.io/badge/Email-nelvinebingiye%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nelvinebingiye@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-nelvinebi-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nelvinebi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-agbozu--ebi-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/agbozu-ebi/)

<br/>

---

<sub>⭐ If you found this project useful, consider giving it a star on GitHub!</sub>

</div>
