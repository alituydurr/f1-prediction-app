import streamlit as st
import pandas as pd
from joblib import load
import os

# Constants for user inputs
circuits = {
    "Bahrain Grand Prix": 3,
    "Saudi Arabian Grand Prix": 77,
    "Australian Grand Prix": 1,
    "Emilia Romagna Grand Prix": 21,
    "Miami Grand Prix": 79,
    "Spanish Grand Prix": 4,
    "Monaco Grand Prix": 6,
    "Azerbaijan Grand Prix": 73,
    "Canadian Grand Prix": 7,
    "British Grand Prix": 9, 
    "Austrian Grand Prix": 70,
    "French Grand Prix": 34,
    "Hungarian Grand Prix": 11,
    "Belgian Grand Prix": 13,
    "Dutch Grand Prix" :  39,
    "Italian Grand Prix": 14,
    "Singapore Grand Prix": 15,
    "Japanese Grand Prix" : 22,
    "United States Grand Prix": 69,
    "Mexico City Grand Prix": 32,
    "São Paulo Grand Prix" : 18,
    "Abu Dhabi Grand Prix" : 24,
    "Qatar Grand Prix": 78,
    "Las Vegas Grand Prix": 80,
    "Chinese Grand Prix": 17,
}  
drivers = {
    "Lewis Hamilton": 1,
    "Fernando Alonso": 4,
    "Sebastian Vettel": 20,
    "Pierre Gasly": 842,
    "Nico Hülkenberg": 807,
    "Sergio Pérez": 815,
    "Daniel Ricciardo": 817,
    "Valtteri Bottas": 822,
    "Max Verstappen": 830,
    "Carlos Sainz": 832,
    "Esteban Ocon": 839,
    "Lance Stroll": 840,
    "Charles Leclerc": 844,
    "Lando Norris": 846,
    "George Russell": 847,
    "Alexander Albon": 848,
    "Nicholas Latifi": 849,
    "Yuki Tsunoda": 852,
    "Mick Schumacher": 854,
    "Guanyu Zhou": 855,
    "Nyck de Vries": 856,
    "Oscar Piastri": 857,
    "Logan Sargeant": 858,
    "Liam Lawson": 859,
    "Oliver Bearman": 860,
}

constructors = {
    "Mercedes": 131,
    "Red Bull": 214,
    "Ferrari": 117,
    "Aston Martin": 9,
    "McLaren": 1,
    "Alpine": 51,
    "Alfa Romeo": 210,
    "Haas": 6,
    "AlphaTauri": 213,
    "Williams": 3,
}  

# Prediction Page
st.title("Formula 1 Tahmin Uygulaması")
st.write("Lütfen yarış verilerini girerek tahmini görmek için gerekli bilgileri doldurun.")

# User input selections
circuit_name = st.selectbox("Pist Seçimi (Circuit)", list(circuits.keys()))
driver_name = st.selectbox("Sürücü Seçimi (Driver)", list(drivers.keys()))
constructor_name = st.selectbox("Takım Seçimi (Constructor)", list(constructors.keys()))
grid = st.number_input("Başlangıç Sırası (grid)", min_value=1, step=1, value=10)
pit_stop_time = st.number_input("Pit Stop Süresi (saniye)", min_value=0.0, step=0.1, value=25.0)

# Map user selections to IDs
circuit_id = circuits[circuit_name]
driver_id = drivers[driver_name]
constructor_id = constructors[constructor_name]

# Prediction button
tahmin_butonu = st.button("Tahmin Yap")

if tahmin_butonu:
    try:
        # Convert pit stop time to milliseconds
        pit_stop_time_ms = pit_stop_time * 1000
        # Create a DataFrame from user inputs
        user_input = pd.DataFrame({
            "circuitId": [circuit_id],
            "driverId": [driver_id],
            "constructorId": [constructor_id],
            "grid": [grid],
            "pit_stop_time": [pit_stop_time_ms]
        })

        # Model dosyasının yolunu belirleme
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(BASE_DIR, "..", "models", "race_outcome_model.pkl")

        # Load the trained model
        model = load(model_path)
       
       
        # Make a prediction
        prediction = model.predict(user_input)

        # Display the prediction result
        if prediction[0] == 1:
            st.success(f"🚥 {driver_name} bu yarışı tahmini olarak KAZANIR! 🏆")
        else:
            st.info(f"{driver_name}, yarışı kazanamaz ama önemli bir performans sergileyebilir.")
    except FileNotFoundError:
        st.error("Model dosyası bulunamadı. Lütfen modelinizi 'race_outcome_model.pkl' olarak kaydedin ve doğru yere yükleyin.")
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
