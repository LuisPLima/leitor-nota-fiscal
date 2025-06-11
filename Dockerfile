FROM python:3.10-slim

# Instalar dependências do sistema para o Playwright
RUN apt-get update && apt-get install -y \
    wget curl gnupg \
    libnss3 libatk-bridge2.0-0 libcups2 libxcomposite1 libxrandr2 libxdamage1 \
    libxfixes3 libxrender1 libxext6 libxtst6 libglib2.0-0 libgtk-3-0 \
    libasound2 libx11-xcb1 libxss1 libpci3 libdrm2 libgbm1 fonts-liberation \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Diretório do app
WORKDIR /app

# Copiar arquivos e instalar dependências Python
COPY backend/ /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m playwright install

# Comando de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
