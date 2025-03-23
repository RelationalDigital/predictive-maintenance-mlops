import os
import pandas as pd

def load_and_preprocess_data(filename='sensor_data.csv'):
    # Determina la directory dello script corrente
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Costruisci il percorso completo verso la cartella data
    filepath = os.path.join(script_dir, '..', 'data', filename)
    df = pd.read_csv(filepath, parse_dates=['timestamp'])
    # Normalizzazione della temperatura (come esempio)
    df['temperature_norm'] = (df['temperature'] - df['temperature'].mean()) / df['temperature'].std()
    return df

if __name__ == "__main__":
    df = load_and_preprocess_data()
    print(df.head())
