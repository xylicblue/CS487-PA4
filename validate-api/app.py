from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    sku: str
    qty: int

class Order(BaseModel):
    order_id: str
    items: List[Item]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/validate")
def validate(order: Order):
    # Reject any line with qty > 100
    for item in order.items:
        if item.qty > 100:
            return {"valid": False,
                    "reason": "quantity exceeds limit",
                    "order_id": order.order_id}
    return {"valid": True, "reason": "ok", "order_id": order.order_id}
