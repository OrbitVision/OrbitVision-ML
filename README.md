## 🚧 CURRENTLY UNDER DEVELOPMENT
*In data testing phase*

---

# OrbitVision-ML: SGP4 Orbit Correction using Machine Learning

OrbitVision-ML is a machine learning-based framework designed to mitigate the prediction degradation of the analytical SGP4 propagation model. By leveraging a Multi-Layer Perceptron (MLP) combined with Gaussian Error Linear Units (GELU) and solar weather indices, this model acts as a hybrid physical-learned corrector to predict and fix SGP4 orbital errors.

---

## 🚀 Objective
Analytical orbit propagation models like SGP4 drift over time due to unmodeled space perturbations (e.g., Solar Radiation Pressure, geomagnetic storms). This project trains a neural network to predict the 3D position residuals ($\Delta X, \Delta Y, \Delta Z$), effectively correcting the SGP4 output toward high-precision reference orbits.

## 📊 Datasets
The model blends orbital mechanics data with environmental space weather metrics:
*   **TLE (Two-Line Element Sets):** Historical Space-Track data used as the baseline input for SGP4 propagation.
*   **SP3 (Standard Product 3):** High-precision, exact historical satellite ephemerides used as the ground-truth reference dataset.
*   **Space Weather Indices:** Dynamic solar activity metrics including the **$F_{10.7}$ Solar Radio Flux** and geomagnetic indices (**$Kp$ / $Ap$**) to model Solar Radiation Pressure (SRP) variations.

## 🧠 Model Architecture
*   **Core:** Gated/Residual Multi-Layer Perceptron (MLP).
*   **Activation Function:** `GELU` (Gaussian Error Linear Unit) for smooth gradient flow in continuous physics modeling.
*   **Features:** SGP4 state vectors matched with cyclical time encodings ($\sin/\cos$ of Mean Anomaly and time) alongside sliding-window solar weather inputs.
*   **Target Output:** The network directly predicts the error vector:
    $$\text{Position}_{\text{Corrected}} = \text{Position}_{\text{SGP4}} + \text{Prediction}_{\text{MLP}}(\Delta)$$

---

## 📈 Baseline SGP4 Error Analysis

Before ML correction, SGP4 exhibits a classic anelastic drift and phase mismatch due to aging TLE data.

### Cumulative 3D Distance Error (Residual)
As the TLE age increases, SGP4 suffers from long-term orbit degradation. The cyclic humps represent the period of the satellite's orbit.

<img width="1852" height="970" alt="image" src="https://github.com/user-attachments/assets/79a09d41-ccda-423b-9b5b-db3265071675" />
