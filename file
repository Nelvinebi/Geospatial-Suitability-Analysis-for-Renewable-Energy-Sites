import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generate synthetic data
np.random.seed(42)
n_points = 150  # >100 points

# Simulated features
solar_irradiance = np.random.normal(loc=5.5, scale=1.0, size=n_points)  # kWh/m2/day
wind_speed = np.random.normal(loc=6.5, scale=1.5, size=n_points)        # m/s
land_slope = np.random.normal(loc=5, scale=3, size=n_points)            # degrees
distance_to_road = np.random.uniform(0, 50, size=n_points)              # km
land_use_type = np.random.choice(['barren', 'agricultural', 'urban', 'forest'], size=n_points)

# Normalize/Clip to simulate realistic values
solar_irradiance = np.clip(solar_irradiance, 2, 8)
wind_speed = np.clip(wind_speed, 2, 12)
land_slope = np.clip(land_slope, 0, 30)

# 2. Define weights for suitability criteria
# Higher irradiance, wind speed => more suitable
# Lower slope, distance, urban areas => more suitable
def calculate_suitability(row):
    score = (
        0.3 * (row['solar_irradiance'] / 8) +
        0.3 * (row['wind_speed'] / 12) +
        0.2 * (1 - row['land_slope'] / 30) +
        0.1 * (1 - row['distance_to_road'] / 50)
    )

    # Penalize land use: barren > agricultural > urban > forest
    land_use_penalty = {
        'barren': 1.0,
        'agricultural': 0.9,
        'urban': 0.7,
        'forest': 0.6
    }
    score *= land_use_penalty[row['land_use_type']]
    return round(score, 2)

# 3. Create DataFrame
df = pd.DataFrame({
    'solar_irradiance': solar_irradiance,
    'wind_speed': wind_speed,
    'land_slope': land_slope,
    'distance_to_road': distance_to_road,
    'land_use_type': land_use_type
})

# 4. Apply suitability scoring
df['suitability_score'] = df.apply(calculate_suitability, axis=1)

# 5. Classify suitability
def classify_suitability(score):
    if score >= 0.7:
        return 'High'
    elif score >= 0.5:
        return 'Moderate'
    else:
        return 'Low'

df['suitability_class'] = df['suitability_score'].apply(classify_suitability)

# 6. Display summary
print(df.head())

# 7. Plot suitability distribution
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='suitability_class', palette='viridis')
plt.title("Suitability Classification")
plt.xlabel("Suitability Level")
plt.ylabel("Number of Sites")
plt.tight_layout()
plt.show()
