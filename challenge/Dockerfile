From python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install flask redis

EXPOSE 5004

CMD ["python", "app.py"]