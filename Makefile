# Variables
PYTHON=python
PIP=pip

# Nom du script principal
MAIN=main.py

# Tâche par défaut
all: run

# Installer les dépendances
install:
	$(PIP) install -r requirements.txt

# Exécuter le pipeline principal
run:
	$(PYTHON) $(MAIN)

# Nettoyer les fichiers temporaires
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

# Formater le code
format:
	black src/ main.py

# Vérifier la qualité du code
lint:
	flake8 src/ main.py

.PHONY: all install run clean format lint
