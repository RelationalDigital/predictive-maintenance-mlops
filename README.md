# 🤖 Predictive Maintenance MLOps

![Python](https://img.shields.io/badge/Python-3.8-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> A robust machine learning system for detecting anomalies in industrial sensor data using advanced feature engineering and Random Forest classification.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running with Python](#running-with-python)
  - [Running with Docker](#running-with-docker)
- [Data Pipeline](#data-pipeline)
- [Model Architecture](#model-architecture)
- [Performance](#performance)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

This project implements a predictive maintenance system that uses machine learning to detect anomalies in industrial sensor data. The system processes temperature, vibration, and pressure readings, engineers relevant features, and trains a Random Forest classifier to identify potential equipment failures before they occur.

Perfect for manufacturing environments, energy plants, or any industrial setting where equipment monitoring is critical.

## ✨ Features

- **Data Simulation**: Generate realistic sensor data with built-in anomaly patterns
- **Preprocessing Pipeline**: Automated data normalization and cleaning
- **Feature Engineering**: Extract meaningful patterns from raw sensor data
- **Anomaly Detection**: Machine learning model to predict equipment failures
- **Performance Metrics**: Built-in accuracy evaluation
- **Docker Support**: Easy deployment in any environment
- **Modular Design**: Well-organized codebase for easy extension

## 📂 Project Structure

```
predictive-maintenance-mlops/
├── data/                 # Data storage directory (created on first run)
├── src/                  # Source code
│   ├── __init__.py       # Package marker
│   ├── data_ingestion.py # Data generation module
│   ├── preprocessing.py  # Data cleaning and normalization
│   ├── feature_engineering.py # Feature creation module
│   └── train_model.py    # Model training and evaluation
├── tests/                # Unit tests
│   └── test_preprocessing.py # Tests for preprocessing module
├── .github/              # GitHub configuration
│   └── workflows/        # CI pipeline configurations
├── .gitignore            # Git ignore rules
├── .gitattributes        # Git attributes configuration
├── Dockerfile            # Docker configuration
├── main.py               # Main execution script
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## 📋 Requirements

The project requires the following Python packages:

- numpy
- pandas
- scikit-learn
- matplotlib
- joblib
- pytest
- flask
- kafka-python

All dependencies are listed in `requirements.txt`.

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/RelationalDigital/predictive-maintenance-mlops.git
cd predictive-maintenance-mlops
```

### Using pip (virtual environment recommended)

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Using Docker

```bash
# Build the Docker image
docker build -t predictive-maintenance .
```

## 🎮 Usage

### Running with Python

To generate data, process it, and train the model:

```bash
python main.py
```

The script will:
1. Generate synthetic sensor data
2. Preprocess and normalize the data
3. Add engineered features
4. Train a Random Forest model
5. Save the trained model as `model.pkl`
6. Print the model's accuracy

### Running with Docker

```bash
# Run the container
docker run predictive-maintenance

# To mount a volume for data persistence
docker run -v $(pwd)/data:/app/data predictive-maintenance
```

## 🔄 Data Pipeline

The data pipeline consists of four main stages:

1. **Data Ingestion**: Generates/collects timestamped sensor readings
   - Temperature (°F)
   - Vibration (mm/s)
   - Pressure (kPa)
   - Anomaly labels

2. **Preprocessing**: Cleans and normalizes the data
   - Parses timestamps
   - Normalizes temperature values
   - Handles missing values

3. **Feature Engineering**: Creates additional features from raw data
   - Rolling temperature averages
   - Vibration standard deviation
   - Additional domain-specific features

4. **Model Training**: Trains and evaluates the anomaly detection model
   - Random Forest Classifier
   - Performance evaluation
   - Model persistence

## 🧠 Model Architecture

The anomaly detection system uses a Random Forest Classifier with the following configuration:

- 100 decision trees
- Features: temperature, vibration, pressure, rolling averages, and standard deviations
- Binary classification: normal operation (0) vs. anomaly (1)
- Train/test split: 80% training, 20% testing

## 📊 Performance

The model is evaluated using accuracy as the primary metric. Typical performance on the synthetic dataset exceeds 90% accuracy, making it suitable for real-world industrial applications.

Additional metrics like precision, recall, and F1-score can be easily incorporated by modifying the `train_model.py` script.

## 🧪 Testing

Run the test suite to verify the system's components:

```bash
pytest tests/
```

The test suite validates:
- Data preprocessing functionality
- Feature engineering correctness
- Model training and evaluation

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code passes all tests and follows the established coding style.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with ❤️ by [Raffaele Zarrelli](https://github.com/Sarracin0) from [Relational Digital](https://github.com/RelationalDigital) 

⭐ Star this repository if you find it useful!

Keywords: predictive maintenance, anomaly detection, machine learning, IoT, industrial sensors, equipment monitoring