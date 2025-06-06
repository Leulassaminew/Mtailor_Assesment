import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--image", type=str, required=True)
parser.add_argument("--url", type=str, required=True)
args = parser.parse_args()

headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0SWQiOiJwLWJmMzhmY2U4IiwibmFtZSI6IiIsImRlc2NyaXB0aW9uIjoiIiwiZXhwIjoyMDY0NzQ1NDY3fQ.D5JEwqjz_41w3TSN94QwxjV7EN7_tcs4G9HE8lSykz3w5Nfeu507cCGgntKRQtJbhcrFEHFKjcqrPnDGzkrSwru74dnpfgKaP4N64tXUEZ3LreJwZYaBLng4SjfHMeCIkGXves24NrekzMNWJkSMGgsvqo4iStbgIIyoGowUdH__rdzlgA1vl7TjkvM0cOuy5lwp8I5Kh8s6dMch7iIoUt2JEGj1hwNaVN0U4vndCaZwD8kaQrzAcoNUgyBpAjW-NgsZasdRh6ahrnRoJ7d8dV44a2PbeJbBIweDUKgIDdA2V17RsLjQ4oEX_cZNZZJlL6jj-E4TEW55SbDBacXNHA'
}

files = {'file': ('filename.jpg', open(args.image, 'rb'),'image/jpeg') }
response = requests.post(f"{args.url}/predict", headers=headers, files=files)
print(response.text)
print(response)