import requests
from requests.auth import HTTPBasicAuth
import bs4
from bs4 import BeautifulSoup
#Logging In with Pass and Username

response = requests.get('https://academia.srmist.edu.in/'
,auth=HTTPBasicAuth('aj7719@srmist.edu.in','AJ##SRM2480'))


# #The Object
# print(response)
#
# #Parse the Content
# soup = BeautifulSoup(response,"html.parser")
# print(soup.prettify())