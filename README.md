\# DDoS Traffic Detector



\## Overview



This project implements a machine learning and deep learning based DDoS traffic detection system using network traffic flow features extracted from a cybersecurity dataset.



The project compares:



\* Random Forest (traditional machine learning)

\* LSTM (sequential deep learning)



to analyze the difference between static traffic classification and temporal traffic behavior learning.



\---



\## Dataset



\* Source: Kaggle Network Traffic Dataset

\* Original dataset size: \~1.5 million rows

\* Dataset type: Static CSV network flow dataset



The dataset was preprocessed, cleaned, balanced, and sorted chronologically before training.



\---



\## Feature Engineering



Additional engineered features were created to improve attack detection:



\* Packet\_Rate

\* Time\_Diff

\* Flow statistics

\* Packet timing features

\* TCP flag behavior



Important preprocessing steps included:



\* Timestamp sorting

\* Infinite value handling

\* Missing value cleaning

\* Dataset balancing

\* Temporal sequence generation for LSTM



\---



\## Features Used



\* Total Fwd Packets

\* Total Backward Packets

\* Flow Duration

\* Flow Bytes/s

\* Flow Packets/s

\* Flow IAT Mean

\* Flow IAT Std

\* Flow IAT Max

\* Packet Length Mean

\* Packet Length Std

\* Fwd Packets/s

\* Bwd Packets/s

\* SYN Flag Count

\* ACK Flag Count

\* Packet\_Rate

\* Time\_Diff



\---



\## Models Used



\### Random Forest



The Random Forest model analyzes individual network flows independently using handcrafted statistical traffic features.



\### LSTM



The LSTM model analyzes sequential traffic behavior by learning temporal dependencies across consecutive traffic flows.



\---



\## Key Difference Between RF and LSTM



\* Random Forest learns static feature relationships from individual flows.

\* LSTM learns temporal traffic behavior across sequences of flows.



This allows the LSTM model to potentially capture evolving attack patterns and sequential anomalies.



\---



\## Technologies Used



\* Python

\* Pandas

\* NumPy

\* Scikit-learn

\* TensorFlow / Keras



\---



\## Files



\* `prepare\_data.py` → preprocessing and feature engineering

\* `random\_forest.py` → Random Forest model

\* `lstm.py` → LSTM model



\---



\## How to Run



\### 1. Install dependencies



```bash

pip install -r requirements.txt

```



\### 2. Run preprocessing



```bash

python prepare\_data.py

```



\### 3. Train Random Forest



```bash

python random\_forest.py

```



\### 4. Train LSTM



```bash

python lstm.py

```



\---



\## Future Improvements



\* Real-time packet capture integration

\* Live traffic monitoring

\* Hyperparameter tuning

\* Confusion matrix visualization

\* ROC-AUC analysis

\* Model deployment using Flask or FastAPI

\* Docker containerization



\---



\## Project Goal



The goal of this project is to explore how traditional machine learning and sequential deep learning models behave on network traffic data for DDoS attack detection.



