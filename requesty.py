import requests

with open('websites.txt', 'r') as file:
    websites = file.read().splitlines()
    print(websites)  
    for i in websites:
        website_status = requests.get(i)
        website_status = website_status.status_code
        if website_status == 200:
            print('Strona istnieje.')
        else:
            print('Brak dostępu')