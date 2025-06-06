import onnxruntime as ort
from PIL import Image
import numpy as np

class ImagePreprocessor:
    def __init__(self):
        self.mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
        self.std = np.array([0.229, 0.224, 0.225], dtype=np.float32)

    def preprocess(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image = image.resize((224, 224))
        image = np.array(image).astype(np.float32)
        image = image / 255.0
        image = (image - self.mean) / self.std
        image = image.transpose(2, 0, 1)
        return np.expand_dims(image, axis=0).astype(np.float32)

class ONNXClassifier:
    def __init__(self, model_path="model.onnx"):
        self.session = ort.InferenceSession(model_path)

    def predict(self, input_array):
        inputs = {self.session.get_inputs()[0].name: input_array}
        output = self.session.run(None, inputs)
        return int(np.argmax(output[0]))
