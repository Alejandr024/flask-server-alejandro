# Usamos una imagen oficial de Python ligera
FROM python:3.14-slim

# Instalamos uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1. Copiamos nuestro archivo de dependencias AL CONTENEDOR
COPY pyproject.toml .

# 2. Sincronizamos el proyecto. 
# uv creará automáticamente un entorno virtual y descargará Flask
RUN uv sync

EXPOSE 5000

# 3. Ejecutamos nuestra app usando 'uv run' para que use el entorno virtual
CMD ["uv", "run", "python", "app/main.py"]