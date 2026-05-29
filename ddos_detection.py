import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# Load SAME dataset
# -----------------------------
data = pd.read_csv("balanced_data.csv")

print("Dataset Loaded:", len(data))

# -----------------------------
# Features (SAME as LSTM)
# -----------------------------
features = [
    "Total Fwd Packets",
    "Total Backward Packets",
    "Flow Duration",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Flow IAT Mean",
    "Flow IAT Std",
    "Flow IAT Max",
    "Packet Length Mean",
    "Packet Length Std",
    "Fwd Packets/s",
    "Bwd Packets/s",
    "SYN Flag Count",
    "ACK Flag Count",
    "Packet_Rate",
    "Time_Diff"
]

X = data[features]
y = data["Label"]

# -----------------------------
# SAME time-based split
# -----------------------------
split_index = int(0.8 * len(X))

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# -----------------------------
# Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
print("\nRandom Forest Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\n✅ Random Forest Done")