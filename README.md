# README

## 環境の構築

1. 仮想環境の作成

    python3 -m venv .venv

2. パッケージのインストール

    poetry shell  
    poetry install

3. .env の作成

    ```
    ALLOWED_HOSTS=127.0.0.1,localhost
    CORS_ALLOWED_ORIGINS=http://127.0.0.1:5173,http://localhost:5173
    ```