# src/data_ingestion.py
import pandas as pd
import numpy as np

def generate_sensor_data(n_samples=1000):
    # Generazione di timestamp con frequenza oraria
    timestamps = pd.date_range(start='2020-01-01', periods=n_samples, freq='h')
    # Simulazione dei dati con distribuzioni gaussiane
    temperature = np.random.normal(loc=75, scale=5, size=n_samples)
    vibration = np.random.normal(loc=0.5, scale=0.1, size=n_samples)
    pressure = np.random.normal(loc=100, scale=10, size=n_samples)
    # Simulazione di anomalie: se la temperatura supera una soglia, si etichetta come anomalia
    anomaly = (temperature > 80).astype(int)
    
    df = pd.DataFrame({
        'timestamp': timestamps,
        'temperature': temperature,
        'vibration': vibration,
        'pressure': pressure,
        'anomaly': anomaly
    })
    return df

if __name__ == "__main__":
    df = generate_sensor_data()
    df.to_csv('data/sensor_data.csv', index=False)
    print("Dati simulati salvati in data/sensor_data.csv")
