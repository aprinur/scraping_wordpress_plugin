import json
from urllib.parse import parse_qs, urlsplit
from db_config import Format_SQL
from util import user_input, open_file, insert_to_db, check_db
from __init__ import URl, API
import requests
import time
import base64


def scrape_api(page_number):

    query = f'from={page_number}&alg=marketplace:search/1&session_id=z3GlL5'
    encripted_query = base64.b64encode(query.encode()).decode()
    full_api = API.format(query=encripted_query)

    try:
        respons = requests.get(full_api)
        time.sleep(2)
        if respons.status_code != 200:
            print(f'Error : {respons.status_code}')
            return []
        result = respons.json()
        all_data = []

        for info in result.get('body', {}).get('data', {}).get('results', []):

            all_data.append(Format_SQL(
                Name=info['fields']['plugin']['title'],
                Release_Date=info['fields']['date'],
                Last_Update=info['fields']['modified'],
                Number_of_Rating=info['fields']['plugin']['num_ratings'],
                Rating=info['fields']['plugin']['rating'],
                Plugin_Link=info['fields']['permalink.url.raw']
            ))

        return all_data
    except Exception as e:
        print(f'Error scraping API: {e}')
        return []


def main():
    total_pages = user_input()
    for i in range(0, total_pages * 20, 20):
        results = scrape_api(i)
        if not results:
            print('No data available')
            break

        for result in results:
            if not check_db(result):
                insert_to_db(result)
                print(f'Plugin inserted to database: {result.Name}')
            else:
                print(f'Record already exist: {result.Name}')


if __name__ == '__main__':
    main()
