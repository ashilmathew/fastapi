from fastapi import FastAPI
from models import user_model, post_model, comment_model
from database import engine
from routes import auth_routes, post_routes, admin_routes

user_model.Base.metadata.create_all(bind=engine)
post_model.Base.metadata.create_all(bind=engine)
comment_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(post_routes.router)
app.include_router(admin_routes.router)
