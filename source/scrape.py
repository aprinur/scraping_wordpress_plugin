import base64
import requests
import time
from source import API


def scrape_api(page_number):
    query = f'from={page_number}&alg=marketplace:search/1&session_id=z3GlL5'
    encripted_query = base64.b64encode(query.encode()).decode()
    full_api = API.format(query=encripted_query)

    try:
        respons = requests.get(full_api)
        time.sleep(2)
        if respons.status_code != 200:
            print(f'Error : {respons.status_code}')
            return
        result = respons.json()
        all_data = []
        for info in result.get('body', {}).get('data', {}).get('results', []):
            data = {
                'Name': info['fields']['plugin']['title'],
                'Release_Date': info['fields']['date'],
                'Last_Update': info['fields']['modified'],
                'Number_of_Rating': info['fields']['plugin']['num_ratings'],
                'Rating': info['fields']['plugin']['rating'],
                'Plugin_Link': info['fields']['permalink.url.raw']
            }
            all_data.append(data)
        return all_data

    except Exception as e:
        print(f'Error scraping API: {e}')
        return
