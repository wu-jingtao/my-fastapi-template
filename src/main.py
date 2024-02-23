import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .controllers.index import router as index_router

app = FastAPI()

# 从环境变量中获取是否开启文档的值，默认为 True
enable_docs = os.environ.get("ENABLE_DOCS", "True").lower() == "true"

if not enable_docs:
    app.docs_url = None
    app.redoc_url = None

# 配置静态文件路径
app.mount("/statics", StaticFiles(directory="src/statics"), name="static")

# 配置路由
app.include_router(index_router, prefix="")
