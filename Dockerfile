FROM python:3.9

RUN pip install scikit-learn==1.0.2 numpy==1.25 flask gunicorn pandas xgboost 

WORKDIR /app

COPY ["model.bin", "predict.py","./"]

EXPOSE 8888

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]