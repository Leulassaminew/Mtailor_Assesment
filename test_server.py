import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--image", type=str, required=True)
parser.add_argument("--url", type=str, required=True)
args = parser.parse_args()

with open(args.image, "rb") as f:
    response = requests.post(f"{args.url}/predict", files={"file": f})
    print(response)
