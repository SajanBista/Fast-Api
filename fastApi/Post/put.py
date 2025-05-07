from fastapi import FastAPI
from pydantic import BaseModel

# Define model item
class Item(BaseModel):
    name: str
    description: str

# Define items at application start
items = {"bananas": "Yellow fruit."}

app = FastAPI()

@app.put("/items")
def update_item(item: Item):
    name = item.name
    # Update the description
    items[name] = item.description
    return {"message": "Item updated", "item": {name: items[name]}}