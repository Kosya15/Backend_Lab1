FROM python:3.10.8-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENV FLASK_APP=project/views.py

CMD ["flask", "run", "--host", "0.0.0.0", "-p", "5000"]