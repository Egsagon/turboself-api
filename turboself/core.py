import re
import requests
from bs4 import BeautifulSoup as Soup

from datetime import datetime
from dataclasses import dataclass

import consts


@dataclass
class Day:
    
    eat: bool
    date: datetime


class Client:
    def __init__(self, username: str, password: str, login: bool = True) -> None:
        '''
        Represensts a TurboSelf client.
        '''
        
        assert len(username) and len(password), 'Invalid credentials'
        
        self.root = 'https://espacenumerique.turbo-self.com/'
        self.session = requests.Session()
        
        self.credentials = {
            'ctl00$cntForm$txtLogin': username,
            'ctl00$cntForm$txtMotDePasse': password
        }
        
        if login: self.login()
    
    def login(self) -> bool:
        '''
        Attempts to login to the target.
        Returns whether it suceed.
        '''
        
        # Load the home page
        homepage = self.session.get(self.root + 'Connexion.aspx')
        
        # Build the payload
        data = consts.re.get_home_data.findall(homepage.text)
        payload = {k: v for k, v in data}
        
        # Send authentification
        self.session.post(self.root + 'Connexion.aspx',
                          data = payload | self.credentials)
        
        # Verify we are authentificated
        # TODO