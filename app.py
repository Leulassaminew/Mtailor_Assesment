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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)