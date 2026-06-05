from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Create FASTAPI app
app = FastAPI(
    title="Fraud Detection API",
    version="1.0"
)

templates = Jinja2Templates(
    directory="templates"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

model = joblib.load("models/xgboost_fraud_model.pkl")

amount_scaler = joblib.load("models/amount_scaler.pkl")

time_scaler = joblib.load("models/time_scaler.pkl")

# Create Input Schema
# FastAPI uses Pydantic for validation
class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

# create prediction endpoint
@app.post("/predict")
def predict(transaction: Transaction):

    data = transaction.dict()

    df = pd.DataFrame([data])

    # Scale Amount
    df["Amount"] = amount_scaler.transform(
        df[["Amount"]]
    )

    # Scale Time
    df["Time"] = time_scaler.transform(
        df[["Time"]]
    )

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "fraud_probability": float(probability)
    }

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/test")
def test():
    return {"message": "test route works"}