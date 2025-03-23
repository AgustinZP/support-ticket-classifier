from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

model = joblib.load('model/ticket_model.pkl')

class Ticket(BaseModel):
    message: str

@app.post('/predict')
def classify(ticket: Ticket):
    prediction = model.predict([ticket.message])[0]
    return {"category": prediction}