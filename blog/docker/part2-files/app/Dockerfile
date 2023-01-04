FROM python:3.9

COPY . /app
WORKDIR /app

RUN python3 -m pip install --upgrade pip
RUN pip install flask

EXPOSE 5000/tcp

CMD ["python3", "main.py"]