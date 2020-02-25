FROM python:alpine

COPY . /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]