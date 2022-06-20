from bs4 import BeautifulSoup
import requests



page_request = requests.get(f'https://newweb.nepalstock.com.np/live-market',verify=False)
print(page_request)