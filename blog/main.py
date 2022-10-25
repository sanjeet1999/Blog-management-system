from fastapi import FastAPI
from routers import blog,user,authentication
from database import engine

import schemas, models
app = FastAPI()

app.include_router(authentication.router)
models.Base.metadata.create_all(engine)
app.include_router(blog.router)
app.include_router(user.router)

