import re
import json
import requests
from bs4 import BeautifulSoup

re_data = r'name=\"(.*?)\".*value=\"(.*?)\"'
re_data = re.compile(re_data)

creds = json.load(open('creds.json'))

url = 'https://espacenumerique.turbo-self.com/Connexion.aspx'
session = requests.Session()

res = session.get(url)
print('Fetched login page')
payload = {k: v for k, v in re_data.findall(res.text)}
payload['ctl00$cntForm$txtLogin'] = creds['email']
payload['ctl00$cntForm$txtMotDePasse'] = creds['pass']

# Authentificate
auth = session.post(url, data = payload)

print('authentificated with status', auth.status_code)

# Pages to scrap
qr_code_url = 'https://espacenumerique.turbo-self.com/QrCode.aspx'
reservations_url = 'https://espacenumerique.turbo-self.com/ReserverRepas.aspx'

# Get reservations
soup = BeautifulSoup(session.get(reservations_url).text, 'html.parser')

# weeks = soup.find('div', {'id': 'ctl00_cntForm_divSemaines'})
weeks = soup.find_all('div', {'class': 'semaine'})

print(f'found {len(weeks)} weeks')

week = weeks[0]
days = week.find_all('li', {'class': 'day_line'})

print('found', len(days) - 1, 'days')

for day in days[1:]:
    
    date = day.find('input', {'class': 'chkDay'}).get('id')
    meals = day.find('label', {'class': 'nbRepas'})
    do_eat = 0 if not meals else meals.text
    
    print(date, do_eat)