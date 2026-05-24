from fastapi import FastAPI

api = FastAPI()

@api.get('/')
def index():
    return {'message': "Test return api"}

# python -m uvicorn main:api --reload