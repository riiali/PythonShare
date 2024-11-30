import pandas as pd
import matplotlib.pyplot as plt

file_name = "energy_shelly_results.csv"
data = pd.read_csv(file_name)

print("Loaded data:")
print(data.head())

validator_data = data[data["Pattern"] == "Validator"]
non_validator_data = data[data["Pattern"] == "NonValidator"]

validator_stats = validator_data.describe()
non_validator_stats = non_validator_data.describe()

print("\nValidator stats:")
print(validator_stats)

print("\nNonValidator stats:")
print(non_validator_stats)

total_energy_comparison = {
    "Validator": validator_data["Aenergy Total (kWh)"].sum(),
    "NonValidator": non_validator_data["Aenergy Total (kWh)"].sum(),
}

print("\nTotal energy comparison (kWh):")
print(total_energy_comparison)

comparison_df = pd.DataFrame({
    "Pattern": ["Validator", "NonValidator"],
    "Total Energy (kWh)": [
        total_energy_comparison["Validator"],
        total_energy_comparison["NonValidator"]
    ],
    "Average Apower (W)": [
        validator_data["Apower (W)"].mean(),
        non_validator_data["Apower (W)"].mean()
    ],
    "Average Voltage (V)": [
        validator_data["Voltage (V)"].mean(),
        non_validator_data["Voltage (V)"].mean()
    ],
    "Average Current (A)": [
        validator_data["Current (A)"].mean(),
        non_validator_data["Current (A)"].mean()
    ]
})

print("\nComparison table:")
print(comparison_df)

plt.figure(figsize=(8, 5))
plt.bar(comparison_df["Pattern"], comparison_df["Total Energy (kWh)"])
plt.title("Total Energy Comparison (kWh)")
plt.ylabel("Total Energy (kWh)")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(comparison_df["Pattern"], comparison_df["Average Apower (W)"])
plt.title("Average Power (Apower) Comparison")
plt.ylabel("Average Power (W)")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(comparison_df["Pattern"], comparison_df["Average Voltage (V)"])
plt.title("Average Voltage Comparison")
plt.ylabel("Average Voltage (V)")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(comparison_df["Pattern"], comparison_df["Average Current (A)"])
plt.title("Average Current Comparison")
plt.ylabel("Average Current (A)")
plt.show()
