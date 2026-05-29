import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("Syn.csv", low_memory=False)
data.columns = data.columns.str.strip()

print("Original Dataset:", len(data))

# -----------------------------
# Timestamp handling
# -----------------------------
data["Timestamp"] = pd.to_datetime(data["Timestamp"], errors='coerce')
data = data.sort_values(by="Timestamp")

# -----------------------------
# Feature Engineering
# -----------------------------
data["Flow Duration"] = data["Flow Duration"].replace(0, 1)
data["Packet_Rate"] = data["Total Fwd Packets"] / data["Flow Duration"]

data["Time_Diff"] = data["Timestamp"].diff().dt.total_seconds()
data["Time_Diff"] = data["Time_Diff"].fillna(0)
data["Time_Diff"] = data["Time_Diff"].clip(upper=10)

# -----------------------------
# Clean Data
# -----------------------------
data.replace([np.inf, -np.inf], np.nan, inplace=True)
data.fillna(0, inplace=True)

# -----------------------------
# Encode Labels
# -----------------------------
data["Label"] = data["Label"].apply(lambda x: 0 if x == "BENIGN" else 1)

# -----------------------------
# Balance Dataset (COMMON)
# -----------------------------
benign = data[data["Label"] == 0]
attack = data[data["Label"] == 1]

min_samples = min(len(benign), len(attack))

benign_sampled = benign.sample(n=min_samples, random_state=42)
attack_sampled = attack.sample(n=min_samples, random_state=42)

balanced_data = pd.concat([benign_sampled, attack_sampled])
balanced_data = balanced_data.sort_values(by="Timestamp").reset_index(drop=True)

print("Balanced Dataset:")
print(balanced_data["Label"].value_counts())

# -----------------------------
# Save
# -----------------------------
balanced_data.to_csv("balanced_data.csv", index=False)

print("✅ Balanced dataset saved as balanced_data.csv")