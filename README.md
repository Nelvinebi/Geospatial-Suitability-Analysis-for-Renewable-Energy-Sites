# Geospatial Suitability Analysis for Renewable Energy Sites

![Pie chart](https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Renewable%20Energy%20Site%20Suitability%20Distribution.png)

A data-driven geospatial analysis project that evaluates land suitability for renewable energy development using environmental and infrastructure-based indicators. The project generates synthetic spatial datasets, computes suitability scores, and visualizes results to support renewable energy site selection.

## 📌 Project Overview

Renewable energy deployment requires informed spatial planning to ensure optimal resource utilization, infrastructure accessibility, and environmental sustainability.

This project simulates geospatial data and applies a weighted suitability analysis framework to identify potential locations for renewable energy installations such as solar farms and wind power sites.

Using Python-based data analysis and visualization techniques, candidate sites are evaluated based on environmental and spatial factors including solar irradiance, wind speed, terrain slope, land use, and proximity to infrastructure.

The workflow demonstrates how geospatial suitability analysis can support renewable energy planning and decision-making.

## 🧪 Features Considered

The suitability model evaluates multiple geospatial factors:

Feature	Description
Solar Irradiance (kWh/m²/day)	Measures solar energy potential at a location
Wind Speed (m/s)	Determines viability for wind energy generation
Land Slope (degrees)	Flatter terrain is preferred for infrastructure installation
Distance to Road/Grid (km)	Proximity to infrastructure reduces development cost
Land Use Type	Determines environmental and regulatory suitability
🧮 Methodology

The project follows a simplified geospatial suitability analysis workflow:

Synthetic Geospatial Data Generation
Over 150 candidate site records are simulated using realistic environmental ranges.

Feature-Based Suitability Scoring
Each site receives a weighted suitability score based on environmental and infrastructure factors.

Site Classification
Locations are categorized into:

High Suitability

Moderate Suitability

Low Suitability

Data Visualization & Analysis
Multiple charts are generated to explore relationships between renewable energy resources and site suitability.

📊 Data Visualizations

The analysis includes several visualizations to interpret suitability results.

1️⃣ Suitability Classification Distribution

![Suitability Classification](https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Suitability%20Classification.png)

Displays the number of locations categorized as High, Moderate, or Low suitability.

2️⃣ Suitability Score Distribution

![Suitability Score](https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Distribution%20of%20Suitability%20Score.png)

A histogram showing the spread of calculated suitability scores across candidate locations.

3️⃣ Feature Influence Analysis

![Feature Influence Analysis](https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Influence%20of%20Factors%20on%20Site%20Suitability.png)

A bar chart illustrating how environmental variables correlate with the final suitability score.

4️⃣ Renewable Resource Relationship

![Solar vs Wind](https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/db29a85f3a0ba99b17f0c6b4f5867e90703e6e6d/Solar%20Vs%20Wind%20Energy%20Potential.png)

A scatter plot showing the relationship between solar irradiance and wind speed, identifying areas with hybrid renewable potential.

5️⃣ Correlation Heatmap

![Correlation Heatmap](https://github.com/Nelvinebi/Geospatial-Suitability-Analysis-for-Renewable-Energy-Sites/blob/b21a6edcdb58d1d689fd50cd1f744defdd4953b1/Feature%20Correlation%20Matrix.png)

A correlation matrix showing relationships between environmental variables used in the suitability analysis.

These visualizations help interpret how different factors influence renewable energy site selection.

📊 Dataset

The generated dataset is stored in:

renewable_energy_suitability_data.xlsx

The dataset includes:

Environmental features

Infrastructure distance

Computed suitability score

Suitability classification label

This dataset can also be imported into GIS tools for further spatial mapping.

📁 Repository Structure
renewable-energy-suitability
│
├── renewable_energy_suitability_data.xlsx   # Synthetic geospatial dataset
├── suitability_analysis.py                  # Main Python analysis script
├── README.md                                # Project documentation
🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/renewable-energy-suitability.git
cd renewable-energy-suitability
2️⃣ Install Required Libraries
pip install pandas numpy matplotlib seaborn openpyxl
3️⃣ Run the Analysis Script
python suitability_analysis.py
📈 Output

The script generates:

Suitability score for each candidate site

Suitability classification (High / Moderate / Low)

Multiple visualizations for exploratory analysis

A structured Excel dataset for further GIS analysis

🌍 Potential Applications

This analytical workflow can support:

Renewable energy site planning

Preliminary GIS-based land suitability studies

Environmental and infrastructure planning

Educational demonstrations of spatial decision analysis

🔮 Future Improvements

Potential extensions of this project include:

Integration with real geospatial datasets (NASA POWER, OpenStreetMap, etc.)

Implementation of GIS libraries such as GeoPandas

Machine learning models for automated site classification

Development of interactive spatial maps

Multi-criteria decision analysis (MCDA) frameworks

👤 Author

Agbozu Ebingiye Nelvin
Environmental Data Scientist | GIS | Remote Sensing | Machine Learning

📧 Email: nelvinebingiye@gmail.com
🔗 GitHub: https://github.com/nelvinebi
🔗 LinkedIn: https://www.linkedin.com/in/agbozu-ebi/

