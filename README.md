# DDoS Traffic Detector

A machine learning and deep learning based DDoS traffic detection project using network flow features extracted from traffic data.

The project compares:

* Random Forest
* LSTM

to study the difference between static traffic classification and sequential traffic behavior learning.

---

## Dataset

* Source: Kaggle network traffic dataset
* Original dataset size: ~1.5 million rows
* Dataset format: CSV traffic flow data

The dataset was:

* cleaned
* balanced
* chronologically sorted
* feature engineered

before training.

---

## Feature Engineering

Additional features created:

* `Packet_Rate`
* `Time_Diff`

Other traffic statistics and TCP flag based features were also used.

---

## Features Used

* Total Fwd Packets
* Total Backward Packets
* Flow Duration
* Flow Bytes/s
* Flow Packets/s
* Flow IAT Mean
* Flow IAT Std
* Flow IAT Max
* Packet Length Mean
* Packet Length Std
* Fwd Packets/s
* Bwd Packets/s
* SYN Flag Count
* ACK Flag Count
* Packet_Rate
* Time_Diff

---

## Models

### Random Forest

Traditional machine learning model that classifies individual traffic flows using handcrafted features.

### LSTM

Sequential deep learning model that learns temporal behavior across consecutive traffic flows.

---

## Random Forest vs LSTM

| Random Forest         | LSTM                       |
| --------------------- | -------------------------- |
| Static learning       | Sequential learning        |
| Faster training       | Slower training            |
| Interpretable         | Temporal memory            |
| Good for tabular data | Good for sequence behavior |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TensorFlow / Keras

---

## Files

```text id="zwf6s2"
prepare_data.py     -> preprocessing and feature engineering
random_forest.py    -> Random Forest model
lstm.py             -> LSTM model
```

---

## Running the Project

Install dependencies:

```bash id="zjlwm2"
pip install -r requirements.txt
```

Run preprocessing:

```bash id="8jlwm9"
python prepare_data.py
```

Train Random Forest:

```bash id="2jlwm8"
python random_forest.py
```

Train LSTM:

```bash id="8jlwm2"
python lstm.py
```

---

## Future Improvements

* Real-time packet capture
* Live traffic analysis
* ROC-AUC evaluation
* Hyperparameter tuning
* Flask/FastAPI deployment

---

## Goal

The goal of this project is to compare traditional machine learning and sequential deep learning approaches for DDoS traffic detection using engineered network traffic features.



