import fastapi
from fastapi import  Request ,FastAPI,status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import PlainTextResponse


#添加自定义异常处理器
class ItemNotFound(Exception):
    def __init__(self, name:str):
        self.name = name

#创建自定义异常
def global_exception_handler(app:FastAPI):
    @app.exception_handler(ItemNotFound)
    async  def item_not_found(request: Request, exc: ItemNotFound):
        return JSONResponse(status_code=404,content={"message": "Item not found","details": str(exc)})

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request, exc):
        return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return PlainTextResponse(str(exc), status_code=400)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
        )