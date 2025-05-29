"""FastAPIアプリケーションのメインモジュール"""

from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

# FastAPIアプリケーションの初期化
app = FastAPI(
    title="CreateDataAgent API",
    description="Clean ArchitectureベースのCreateDataAgent API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {"message": "CreateDataAgent API is running"}


@app.get("/health")
async def health_check():
    """ヘルスチェックエンドポイント"""
    return {"status": "healthy"}


# カスタムOpenAPIスキーマ
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="CreateDataAgent API",
        version="1.0.0",
        description="Clean ArchitectureベースのCreateDataAgent API",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi 