# src/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from src.preprocessing import load_and_preprocess_data
from src.feature_engineering import add_features


def train_model(data_path):
    # Carica e preprocessa i dati
    df = load_and_preprocess_data(data_path)
    # Aggiungi feature utili
    df = add_features(df)
    
    # Definizione delle feature e del target
    features = ['temperature', 'vibration', 'pressure', 'temp_rolling_mean', 'vibration_std']
    target = 'anomaly'
    X = df[features]
    y = df[target]
    
    # Suddividi in training e test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Inizializza e allena il modello
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Valuta le performance
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.2f}")
    
    # Salva il modello addestrato
    joblib.dump(clf, '../model.pkl')
    print("Modello salvato come model.pkl")

if __name__ == "__main__":
    train_model('../data/sensor_data.csv')
