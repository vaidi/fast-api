from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.routes.base import router as base_router
from app.routes.user import router as user_router
from app.routes.item import app as item_router
from app.routes.content import router as content_router
from app.database.session import engine
from app.models import user, content
from app.database.redis_client import redis_client
from dependencies import get_token_header
from expections import handlers
import uvicorn

# 创建数据库表
user.Base.metadata.create_all(bind=engine)
content.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Project", version="0.1.0",dependencies=[Depends(get_token_header)], description="FastAPI Project")

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#处理全局异常
handlers.global_exception_handler(app)


app.include_router(item_router)
# 包含路由
app.include_router(base_router)
app.include_router(user_router)
app.include_router(content_router)

@app.on_event("startup")
async def startup_event():
    # 测试Redis连接
    try:
        redis_client.ping()
        print("Redis connected successfully")
    except Exception as e:
        print(f"Redis connection error: {e}")

@app.on_event("shutdown")
async def shutdown_event():
    redis_client.close()
    print("Redis connection closed")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)