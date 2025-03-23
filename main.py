# main.py

import os
import logging

# Importiamo le funzioni dai moduli presenti in src
from src.data_ingestion import generate_sensor_data
from src.preprocessing import load_and_preprocess_data
from src.feature_engineering import add_features
from src.train_model import train_model

def main():
    # Configura il logging per il debug
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Determina la root del progetto (dove si trova main.py)
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    # Assicurati che la cartella data esista nella root
    data_dir = os.path.join(project_root, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        logging.info("Cartella 'data' creata: %s", data_dir)
    
    # Percorso per il file dei dati
    sensor_data_file = os.path.join(data_dir, 'sensor_data.csv')
    
    # 1. Genera e salva i dati simulati
    logging.info("Generazione dei dati simulati...")
    df = generate_sensor_data()
    df.to_csv(sensor_data_file, index=False)
    logging.info("Dati salvati in: %s", sensor_data_file)
    
    # 2. Preprocessing: Carica e normalizza i dati
    logging.info("Esecuzione del preprocessing...")
    df_preprocessed = load_and_preprocess_data(sensor_data_file)
    logging.debug("Anteprima dei dati preprocessati:\n%s", df_preprocessed.head())
    
    # 3. Feature Engineering: Aggiungi nuove feature al dataset
    logging.info("Aggiunta delle feature al dataset...")
    df_features = add_features(df_preprocessed)
    sensor_data_features_file = os.path.join(data_dir, 'sensor_data_features.csv')
    df_features.to_csv(sensor_data_features_file, index=False)
    logging.info("Dati con feature salvati in: %s", sensor_data_features_file)
    
    # 4. Training del modello: Si riutilizza il modulo di training che si occupa di
    # caricare i dati, eseguire preprocessing e feature engineering internamente e addestrare il modello.
    # Se preferisci, puoi modificare train_model per ricevere direttamente df_features.
    logging.info("Addestramento del modello...")
    train_model(sensor_data_file)  # Il modulo train_model richiama load_and_preprocess_data e add_features internamente
    logging.info("Modello addestrato e salvato correttamente.")

if __name__ == '__main__':
    main()
