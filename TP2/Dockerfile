FROM python:3.9-slim-buster

ENV PIP_NO_CACHE_DIR=1
RUN pip install requests==2.7.0 && \
    pip install flask==1.1.2



WORKDIR /weather

COPY .  /weather



CMD ["python", "weather.py"]
