FROM python:3.6-slim

EXPOSE 8050

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .


ENTRYPOINT python ./app.py
