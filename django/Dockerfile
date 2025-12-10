FROM python:3.11-slim

#EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app/ ./app/

WORKDIR /app/app

RUN python manage.py collectstatic --noinput || true

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
