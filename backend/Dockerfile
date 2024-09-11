FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install -r requirements.txt

COPY backend/app backend/app

EXPOSE 8000

CMD ["uvicorn", "main:app:clinic-server-fastapi", "--host", "0.0.0.0", "--port", "8000", "--reload"]