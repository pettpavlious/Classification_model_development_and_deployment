# Classification Model Development and Model deployment

## Description

The current project is an example of an end to end process of a classification model development along with the model deployment

## Getting Started

The classification_model_development.ipynb showcases the end to end process of the model development along with the model extraction.

The model.bin contains the extracted model after optimisation.

The predict.py is the process of deploying the model.

The requests.ipynb to test that the model works and provides results once the model is deployed.

The Dockerfile used to initialise the process.

The gender-prediction.csv which includes the data used to train and test the model

### Installing

In order to start the project using Docker you can run:

docker build -t gender-model .

