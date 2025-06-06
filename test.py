from model import ImagePreprocessor,ONNXClassifier

images = [
    "images/n01440764_tench.jpeg","images/n01667114_mud_turtle.JPEG"
]

preprocessor = ImagePreprocessor()
classifier = ONNXClassifier("model.onnx")

for path in images:
    input_tensor = preprocessor.preprocess(path)
    prediction = classifier.predict(input_tensor)
    print(f"{path} prediction is f{prediction}")