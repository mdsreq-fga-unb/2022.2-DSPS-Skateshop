from fastapi import FastAPI


app = FastAPI()


@app.get("/healthy", include_in_schema=False)
def healthy_route():
    return {"message": "OK"}
