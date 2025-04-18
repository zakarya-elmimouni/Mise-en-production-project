.PHONY: data train test clean

data:
	python src/data/make_dataset.py

train:
	python src/models/train_model.py

predict:
	python src/models/predict_model.py

visualize:
	python src/visualization/visualize.py

clean:
	rm -rf models/*
	rm -rf reports/*
