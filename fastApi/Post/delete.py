from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str

class SuccessMessage():
    message : str

# Define items at application start
items = {"apples", "oranges", "bananas"}

app = FastAPI()


@app.delete("/items")
def delete_item(item: Item):
    name = item.name
    # Check if the item exists before deleting
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items.remove(name)
    return SuccessMessage(message = f"Item '{name}' deleted successfully")