import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Exploration des données météo (depuis S3)")

st.markdown("**Entrez les informations de votre bucket S3 pour charger les données météo.**")

uploaded_file = st.file_uploader("Chargez un fichier CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :", df.head())
    st.write("Statistiques descriptives :", df.describe())

import streamlit as st
import pandas as pd
import plotly.express as px
import s3fs


class S3DataLoader:
    def __init__(self, bucket: str, endpoint_url: str = "https://minio.lab.sspcloud.fr"):
        self.bucket = bucket
        self.endpoint_url = endpoint_url
        self.fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": endpoint_url})

    def load_csv(self, file_path: str) -> pd.DataFrame:
        # Chargement du CSV depuis S3
        with self.fs.open(f"s3://{self.bucket}/{file_path}") as f:
            df = pd.read_csv(f)

        # Affichage recap
        print(f"\nRésumé du fichier: {file_path}")
        print("-" * 50)
        print(f"Nombre de lignes: {df.shape[0]}")
        print(f"Nombre de variables: {df.shape[1]}")
        print("-" * 50)
        print()

        return df


# Inputs S3
bucket = st.text_input("Nom du bucket S3", value="mon-bucket")
file_path = st.text_input("Chemin du fichier CSV", value="data/weather_data.csv")

if st.button("📥 Charger les données depuis S3"):
    try:
        loader = S3DataLoader(bucket=bucket)
        df = loader.load_csv(file_path)

        st.success("✅ Données chargées avec succès depuis S3 !")
        st.write("Aperçu des données :", df.head())

        # Visualisation simple
        if "temperature" in df.columns and "humidity" in df.columns:
            st.subheader("🌡️ Température vs Humidité")
            fig = px.scatter(df, x="temperature", y="humidity", color="valid_time", title="Température vs Humidité")
            st.plotly_chart(fig)

        st.subheader("📈 Moyenne d'humidité par heure (valid_time)")
        if "valid_time" in df.columns and "humidity" in df.columns:
            mean_by_hour = df.groupby("valid_time")["humidity"].mean().reset_index()
            fig = px.line(mean_by_hour, x="valid_time", y="humidity", markers=True)
            st.plotly_chart(fig)
        st.subheader("📊 Statistiques descriptives")
        st.dataframe(df.describe())

        # Scatter plot
        if "temperature" in df.columns and "humidity" in df.columns:
            st.subheader("🌡️ Température vs Humidité")
            fig = px.scatter(df, x="temperature", y="humidity", color="valid_time", title="Température vs Humidité")
            st.plotly_chart(fig)

        # Line plot (par heure)
        if "valid_time" in df.columns and "humidity" in df.columns:
            st.subheader("📈 Moyenne d'humidité par heure")
            df["valid_time"] = pd.to_datetime(df["valid_time"])
            df["hour"] = df["valid_time"].dt.hour
            mean_by_hour = df.groupby("hour")["humidity"].mean().reset_index()
            fig = px.line(mean_by_hour, x="hour", y="humidity", markers=True)
            st.plotly_chart(fig)

        # Distributions
        st.subheader("📥 Distributions des variables numériques")
        num_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
        if num_cols:
            selected = st.multiselect("Choisissez des variables", num_cols, default=num_cols[:2])
            for col in selected:
                st.write(f"Distribution de **{col}**")
                plt.figure(figsize=(6, 3))
                sns.histplot(df[col], kde=True, bins=30, color='skyblue')
                plt.title(f"Distribution de {col}")
                st.pyplot()
        else:
            st.info("Aucune colonne numérique à afficher.")

    except Exception as e:
        st.error(f"❌ Erreur lors du chargement : {e}")
