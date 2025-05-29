FROM python:3.13-slim

# 作業ディレクトリの設定
WORKDIR /app

# システムの依存関係をインストール
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Pythonの依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY src/ ./src/
COPY tests/ ./tests/

# ポート8000を公開
EXPOSE 8000

# FastAPIアプリケーションを起動
CMD ["uvicorn", "src.frameworks.web.main:app", "--host", "0.0.0.0", "--port", "8000"] 