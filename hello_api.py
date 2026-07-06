from fastapi import FastAPI

app = FastAPI()
saved = {}

@app.post("/")
def post_data(data: dict):
    saved["item"] = data
    return {"message": "post", "usr_data": data}

@app.get("/")
def get_data():
    return {"message": saved.get("item", {})}

@app.put("/")
def put_data(data: dict):
    saved["item"] = data
    return {"message": "Replaced", "dat": data}

@app.patch("/")
def patch_data(data: dict):
    if "item" in saved:
        saved["item"].update(data)
        return {"message": "patrched", "patched_data": saved["item"]}
    return {"error": "Nothing to PATCH, POST something first"}

@app.delete("/")
def delete_data(data: dict):
    if "item" in saved:
        removed = saved.pop("item")
        return {"message": "deleted", "removed": removed}
    return {"message": "Nothing to delete"}
