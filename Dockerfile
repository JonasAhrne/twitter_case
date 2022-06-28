FROM python:3.9

WORKDIR /app

add . /app

RUN pip install -r ./requirements.txt

CMD ["python3", "./main.py"]




