import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Application Humidity",
    page_icon="💧",
    layout="wide"
)

st.title("🌦️ Prédiction de l'Humidité Relative : Mise en production projet Data Science")

st.markdown("""
Cette application vous permet d'explorer les données météo et de tester un modèle de prédiction d'humidité.

Utilisez le menu à gauche pour naviguer entre les différentes pages.
    - 🏠 Présentation
    - 📊 Analyse descriptive
    - 🤖 Outil de prédiction
    """
)



# Paths vers les images dans le dossier 'img'
logo_haut = Path("img/ippLogo.png")
logo_gauche = Path("img/S5-45_C3S_logo.png")
logo_droite = Path("img/Copernicus vecto def  Europe's eyes on Earth.png")


st.markdown(
    """
    Bienvenue dans notre application de démonstration !  
    Utilisez le menu de gauche pour naviguer entre les différentes sections :
    - 🏠 Présentation
    - 📊 Analyse descriptive
    - 🤖 Outil de prédiction
    """
)

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(str(logo_haut), width=200)

st.markdown("### Description et Contexte")

st.markdown(
    """
> L’humidité relative est une mesure de la quantité de vapeur d’eau présente dans l’air par rapport à la quantité maximale qu’il peut contenir à une température donnée.
> 
> La capacité de l’air à contenir de l’humidité dépend de la température : un air plus chaud peut contenir davantage de vapeur d’eau, tandis qu’un air plus froid en retient moins. 
> 
> Dans la zone géographique marocaine, l’humidité relative joue un rôle essentiel dans la prévision des sécheresses, la gestion des ressources en eau et la compréhension de la variabilité climatique.
"""
)

col_g, col_d = st.columns(2)
with col_g:
    st.image(str(logo_gauche), width=150)
with col_d:
    st.image(str(logo_droite), width=150)

st.markdown("---")

# ---- Objectifs ----
st.header("📌 Objectifs")

st.markdown(
    """
- Prétraitement et nettoyage des données météorologiques  
- Entraînement d’un modèle de prédiction de l’humidité relative  
- Évaluation des performances  
- Déploiement du modèle via une API ou une interface web  
"""
)

# ---- Stack technique ----
st.header("🔧 Stack technique")

st.markdown(
    """
- **Langage** : Python  
- **Librairies** : Pandas, NumPy, Scikit-learn  
- **MLOps** : MLflow  
- **Containerisation** : Docker  
"""
)

# ---- Structure du projet ----
st.header("📁 Structure du projet")

st.code(
"""
├── data
│   ├── raw
│   ├── processed
│   └── ...
├── notebooks
├── src
│   ├── data
│   ├── models
│   ├── features
│   └── visualization
├── app
│   └── pages
├── requirements.txt
├── setup.py
└── main.py
└── train.py

""",
language="bash"
)

# ---- Getting Started ----
st.header("🚀 Getting Started")

st.subheader("Install")

st.markdown("Pour exécuter le code et tester les notebooks :")

st.code("pip install -U -r requirements.txt", language="bash")


