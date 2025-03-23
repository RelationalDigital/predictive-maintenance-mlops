import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import load_and_preprocess_data

def test_temperature_norm_exists():
    test_data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sensor_data.csv')
    df = load_and_preprocess_data(test_data_path)
    assert 'temperature_norm' in df.columns
