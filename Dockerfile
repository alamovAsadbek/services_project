# 1. Python tasvirini tanlash
FROM python:3.9-slim

# 2. Ishchi katalogni o'rnatish
WORKDIR /app

# 3. Tizim kutubxonalarini yangilash va zarur kutubxonalarni o'rnatish
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Talab qilingan Python kutubxonalarini o'rnatish
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Django ilovasini konteynerga nusxalash
COPY . /app/

# 6. Django serverini ishga tushirish (Port 8000-da)
EXPOSE 8000

# 7. Django uchun muhitni sozlash (masalan, DEBUG, DATABASE_URL va boshqalar)
ENV PYTHONUNBUFFERED=1

# 8. Django serverini ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
