FROM python:3.9-slim-buster

RUN pip install flask
RUN pip install --no-cache-dir requests==2.7.0


WORKDIR /weather

COPY .  /weather



CMD ["python", "weather.py"]
