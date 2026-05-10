# --- ETAPA 1: Construcción (Build) ---
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Instalamos las dependencias en una carpeta local al usuario
RUN pip install --user --no-cache-dir -r requirements.txt

# --- ETAPA 2: Producción (Runtime) ---
FROM python:3.11-slim
WORKDIR /app

# Copiamos solo las librerías instaladas de la etapa anterior para ahorrar espacio
COPY --from=builder /root/.local /root/.local
COPY . .

# Aseguramos que Python encuentre las librerías instaladas
ENV PATH=/root/.local/bin:$PATH

# Exponemos el puerto 5000 (donde corre Flask)
EXPOSE 5000

# Usamos Gunicorn para que la app sea más estable en producción
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
