# src/feature_engineering.py
import pandas as pd

def add_features(df):
    # Calcola la media mobile della temperatura su una finestra di 5 osservazioni
    df['temp_rolling_mean'] = df['temperature'].rolling(window=5).mean()
    # Calcola la deviazione standard della vibrazione su una finestra di 5 osservazioni
    df['vibration_std'] = df['vibration'].rolling(window=5).std()
    # Rimuovi le righe con valori NaN (dovuti al rolling)
    df = df.dropna()
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/sensor_data.csv', parse_dates=['timestamp'])
    df = add_features(df)
    df.to_csv('../data/sensor_data_features.csv', index=False)
    print("Dati con feature aggiunte salvati in data/sensor_data_features.csv")
