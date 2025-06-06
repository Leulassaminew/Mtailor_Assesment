from fastapi import FastAPI, File, UploadFile
from model import ImagePreprocessor, ONNXClassifier
import uvicorn
import numpy as np

app = FastAPI()
preprocessor = ImagePreprocessor()
classifier = ONNXClassifier("model.onnx")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    with open("temp.jpg", "wb") as f:
        f.write(contents)
    input_tensor = preprocessor.preprocess("temp.jpg")
    prediction = classifier.predict(input_tensor)
    return {"prediction": prediction}

@app.post("/hello")
def hello():
    return {"message": "Hello Cerebrium!"}

@app.get("/health")
def health():
    return "OK"
