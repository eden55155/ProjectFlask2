FROM python:latest

WORKDIR /app
COPY requirements.txtf
RUN pip install -r requirements.txt

COPY / .

EXPOSE 8080

CMD ["python", "app.py"]


