import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Input
from tensorflow.keras.callbacks import EarlyStopping

# -----------------------------
# Load SAME dataset
# -----------------------------
data = pd.read_csv("balanced_data.csv")

print("Dataset Loaded:", len(data))

# -----------------------------
# Features (SAME as RF)
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

X = data[features].values
y = data["Label"].values

# -----------------------------
# SAME time-based split
# -----------------------------
split_index = int(0.8 * len(X))

X_train_raw = X[:split_index]
X_test_raw = X[split_index:]

y_train_raw = y[:split_index]
y_test_raw = y[split_index:]

# -----------------------------
# Normalize
# -----------------------------
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train_raw)
X_test_scaled = scaler.transform(X_test_raw)

# -----------------------------
# Sequence Creation
# -----------------------------
def create_sequences(X, y, seq_length=20):
    X_seq, y_seq = [], []

    for i in range(len(X) - seq_length):
        X_seq.append(X[i:i+seq_length])
        y_seq.append(y[i+seq_length-1])

    return np.array(X_seq), np.array(y_seq)

SEQ_LENGTH = 20

X_train, y_train = create_sequences(X_train_scaled, y_train_raw)
X_test, y_test = create_sequences(X_test_scaled, y_test_raw)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

# -----------------------------
# LSTM Model
# -----------------------------
model = Sequential([
    Input(shape=(SEQ_LENGTH, len(features))),
    LSTM(64),
    Dropout(0.2),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# -----------------------------
# Early Stopping
# -----------------------------
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

# -----------------------------
# Train
# -----------------------------
model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=64,
    validation_split=0.2,
    callbacks=[early_stop]
)

# -----------------------------
# Evaluate
# -----------------------------
loss, accuracy = model.evaluate(X_test, y_test)
print("\nLSTM Accuracy:", accuracy)

# -----------------------------
# Predictions
# -----------------------------
y_pred = (model.predict(X_test) > 0.5).astype(int)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\n✅ LSTM Done")