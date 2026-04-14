from fastapi import FastAPI
from database import add_transaction, get_all_transactions, delete_transaction

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Finance Tracker API"}

@app.get("/transactions")
def list_all():
    rows = get_all_transactions()
    return {"transactions": rows}

@app.post("/add")
def add(amount: float, category: str, type: str, date: str, description: str = ""):
    add_transaction(amount, category, type, date, description)
    return {"status": "success"}

@app.delete("/delete/{tid}")
def delete(tid: int):
    delete_transaction(tid)
    return {"status": "deleted"}