from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import joblib


app = FastAPI(title="Alzheimer's Prediction API")


templates = Jinja2Templates(directory="templates")


model = joblib.load("model/xgb_alzheimer_model.pkl")
scaler = joblib.load("model/minmax_scaler.pkl")


@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": None})


@app.post("/", response_class=HTMLResponse)
async def form_post(
    request: Request,
    mmse: float = Form(...),
    functional_assessment: float = Form(...)
):
    features = np.array([[mmse, functional_assessment]])
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)[0]
    result = "Alzheimer's Detected" if prediction == 1 else "No Alzheimer's"
    return templates.TemplateResponse("form.html", {"request": request, "result": result})
