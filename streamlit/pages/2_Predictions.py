import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title("🤖 Prédiction de l'humidité")

st.markdown("Entrez les valeurs ci-dessous pour prédire le taux d’humidité :")

# Exemples de champs d'entrée
latitude = st.number_input("Latitude", value=45.0)
longitude = st.number_input("Longitude", value=1.0)
temperature = st.number_input("Température", value=12.0)
divergence = st.number_input("Divergence", value=0.1)
u_wind = st.number_input("U composante du vent", value=2.0)
v_wind = st.number_input("V composante du vent", value=1.0)
valid_time = st.number_input("Heure (valid_time)", value=1)

# Charger le modèle
if st.button("Prédire"):
    try:
        model = joblib.load("model.joblib")  # ou "models/model.pkl" si c'est ton chemin
        X = pd.DataFrame([{
            "latitude": latitude,
            "longitude": longitude,
            "temperature": temperature,
            "divergence": divergence,
            "u_component_wind": u_wind,
            "v_component_wind": v_wind,
            "valid_time": valid_time
        }])
        prediction = model.predict(X)[0]
        st.success(f"🌬️ L'humidité prédite est : **{prediction:.2f}%**")
    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")
