FROM python:3.6-slim

EXPOSE 8050

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY setup.py /app/setup.py
RUN pip install -e .

COPY . /app

ENTRYPOINT python ./app.py
