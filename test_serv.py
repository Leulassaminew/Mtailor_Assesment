import requests
import json

url = "https://api.cortex.cerebrium.ai/v4/p-bf38fce8/mtailor1/predict"
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0SWQiOiJwLWJmMzhmY2U4IiwibmFtZSI6IiIsImRlc2NyaXB0aW9uIjoiIiwiZXhwIjoyMDY0NzQ1NDY3fQ.D5JEwqjz_41w3TSN94QwxjV7EN7_tcs4G9HE8lSykz3w5Nfeu507cCGgntKRQtJbhcrFEHFKjcqrPnDGzkrSwru74dnpfgKaP4N64tXUEZ3LreJwZYaBLng4SjfHMeCIkGXves24NrekzMNWJkSMGgsvqo4iStbgIIyoGowUdH__rdzlgA1vl7TjkvM0cOuy5lwp8I5Kh8s6dMch7iIoUt2JEGj1hwNaVN0U4vndCaZwD8kaQrzAcoNUgyBpAjW-NgsZasdRh6ahrnRoJ7d8dV44a2PbeJbBIweDUKgIDdA2V17RsLjQ4oEX_cZNZZJlL6jj-E4TEW55SbDBacXNHA'
}


#response = requests.request("GET", url, headers=headers)
#response = requests.post(url, headers=headers)
#print(response.text)
#print(response)



#files = [('file', open('images/n01440764_tench.jpeg', 'rb'))]

path = 'images/n01440764_tench.jpeg'
files = {'file': ('filename.jpg', open(path, 'rb'),'image/jpeg') }
response = requests.post(url, headers=headers, files=files)
print(response.text)
