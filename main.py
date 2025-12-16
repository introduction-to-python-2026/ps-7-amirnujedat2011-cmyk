import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Player": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Goals": [10, 15, 7, 20, 5, 12, 9, 14],
    "Assists": [5, 7, 3, 10, 2, 6, 4, 8],
    "Minutes_Played": [900, 1200, 800, 1500, 700, 1100, 950, 1300],
    "Injuries": [1, 0, 2, 1, 3, 0, 1, 0]
}

df = pd.DataFrame(data)

print("נתונים:")
print(df)

features = ["Goals", "Assists", "Minutes_Played", "Injuries"]
df_selected = df[features]

df_selected.hist(figsize=(10,8), bins=10)
plt.suptitle("Histograms של ביצועי השחקנים")
plt.tight_layout()
plt.show()

pd.plotting.scatter_matrix(df_selected, figsize=(10,10))
plt.suptitle("Scatter Matrix של ביצועי השחקנים")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df_selected.corr(), annot=True, cmap='coolwarm')
plt.title("Heatmap של קורלציות בין ביצועי השחקנים")
plt.savefig("correlation.png")
plt.show()

