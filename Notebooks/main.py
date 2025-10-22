from fastapi import FastAPI
from enum import Enum
from pymongo import MongoClient
from utils.pyMongoDbConfig import ATLAS_URI

app = FastAPI()
db = MongoClient(ATLAS_URI)
collection = db["mydatabase"]
table = collection["Products"]

@app.get("/")
async def root():
    return {"message": "Hello rrrrrorld"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    print(table.find_one({"_id": item_id}) ) 
    return list(str(x.get("price")) +" | "+ str(x.get("_id")) for x in table.find({"_id": { '$gt': item_id}}) )

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]  

@app.get('/products/{product_id}')
async def get_product_desc(product_id : int):
    return {"product def": 'This is the product '+ str(product_id)}

@app.post('/products/{product_id}')
async def set_product_desc(product_id : int):
    return {"product def": 'This is the product '+ str(product_id)}


@app.put('/products/{product_id}')
async def put_product_desc(product_id : int):
    return {"product def": 'This is the product '+ str(product_id)}



@app.delete('/products/{product_id}')
async def delete_product_desc(product_id : int):
    return {"product def": 'This is the product '+ str(product_id)}