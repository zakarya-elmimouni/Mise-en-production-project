# 🌦️ Prédiction de l'Humidité Relative : *Mise en production projet Data Science*

Ce projet a pour objectif de prédire l'humidité relative à partir de données météorologiques. Il s'inscrit dans une démarche de **mise en production d’un modèle de machine learning**.

<p align="center">
  <!-- Logo du haut (centré) -->
  <img src="img/ippLogo.png" alt="Logo Haut" width="25%">
  <br><br>
  <!-- Logos du bas (gauche et droite) -->
  <img src="img/S5-45_C3S_logo.png" alt="Logo Gauche" width="20%" style="margin-right: 20px;">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="img/Copernicus vecto def  Europe's eyes on Earth.png" alt="Logo Droite" width="20%" style="margin-left: 20px;">
</p>


> **Description et Contexte** :  
> L’humidité relative est une mesure de la quantité de vapeur d’eau présente dans l’air par rapport à la quantité maximale qu’il peut contenir à une température donnée. Elle est exprimée en pourcentage, où 100 % signifie que l’air est entièrement saturé de vapeur d’eau et ne peut plus en contenir davantage, ce qui peut entraîner de la condensation (comme la rosée ou le brouillard).
>  
> La capacité de l’air à contenir de l’humidité dépend de la température : un air plus chaud peut contenir davantage de vapeur d’eau, tandis qu’un air plus froid en retient moins. C’est pourquoi l’humidité semble souvent plus élevée par temps chaud, même si la quantité réelle de vapeur d’eau dans l’air n’a pas changé. Par exemple, si l’humidité relative est de 50 %, cela signifie que l’air contient la moitié de l’humidité qu’il pourrait potentiellement contenir à cette température. Une humidité relative élevée (comme 80–90 %) donne une sensation d’air lourd et humide, tandis qu’une humidité relative faible (comme 20–30 %) rend l’air sec, ce qui peut provoquer des désagréments comme la sécheresse de la peau ou des irritations.
>  
> Dans la zone géographique marocaine, l’humidité relative joue un rôle essentiel dans la prévision des sécheresses, la gestion des ressources en eau et la compréhension de la variabilité climatique. Les régions semi-arides et arides du pays sont particulièrement sensibles aux fluctuations de l’humidité, qui influencent l’humidité des sols et les rendements agricoles. Une faible humidité relative accélère l’évaporation dans les réservoirs et les systèmes d’irrigation, aggravant la pénurie d’eau. Dans les zones côtières et montagneuses, les variations d’humidité influencent la formation des nuages et les régimes de précipitations, impactant l’agriculture et la production d’énergie hydraulique. En intégrant les données d’humidité relative dans les modèles climatiques, les scientifiques et les décideurs peuvent mieux anticiper les risques de sécheresse et optimiser les stratégies de gestion de l’eau pour en atténuer les effets.
> 


 ---
 





## 📌 Objectifs

- Prétraitement et nettoyage des données météorologiques
- Entraînement d’un modèle de prédiction de l’humidité relative
- Évaluation des performances
- Déploiement du modèle via une API ou une interface web

## 🔧 Stack technique

- Python
- Pandas, NumPy
- Scikit-learn 
- MLOPS
- Docker 

## 📁 Structure du projet

## Getting started

### Install

To run a the code and test the notebooks you need to install the dependencies listed
in `requirements.txt`. You can do this with the
following command-line:

```bash
pip install -U -r requirements.txt
```

If you are using `conda`, we provide an `environment.yml` file for similar
usage.
