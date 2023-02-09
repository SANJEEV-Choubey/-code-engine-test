from fastapi import FastAPI

app = FastAPI(title='Hello World',
              description='It is a hello world test for code engine ',
              version=0.1,
              docs_url='/docs',
              redoc_url='/redoc')


@app.get("/")
async def root():
    return {"message": "Hello World update"}