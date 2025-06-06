import torch 
from pytorch_model import Classifier, BasicBlock

model = Classifier(BasicBlock, [2, 2, 2, 2])
model.load_state_dict(torch.load('pytorch_model_weights.pth', map_location='cpu'))
model.eval()

dum_input = torch.randn(1,3, 224, 224, dtype=torch.float32)

torch.onnx.export(
    model,
    dum_input,
    "model.onnx",
    input_names=['input'],
    output_names=['output'],
    dynamic_axes= {'input' : {0: "batch_size"}, 'output': {0: 'batch_size'}},
    opset_version=11
)

print("onnx model exported")