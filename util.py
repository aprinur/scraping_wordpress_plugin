import os
from __init__ import session
from db_config import Format_SQL
import base64


def open_file(filename):
    try:
        with open(filename, 'r') as f:
            parameters = f.read()
            return parameters.split('\n')
    except FileNotFoundError:
        print('File not found')
    except FileExistsError:
        print('File corrupted')


def user_input():
    while True:
        total_pages = input('Input total page to scrape: ')
        if total_pages.isdigit():
            total_pages = int(total_pages)
            return total_pages
        else:
            print('Input must be integer')


def insert_to_db(result):
    session.add(result)
    session.commit()
    print('Insert to db success')


def check_db(data):
    exist = session.query(Format_SQL).filter_by(Name=data.Name).first()
    return exist is not None


def modif_page_handle(api_key: str, ):
    page_handle_key = api_key.split('&')[32][12:]
    if '%3D%3D' in page_handle_key:
        page_handle_key = page_handle_key.replace('%3D%3D', '==')
    decoded = base64.b64decode(page_handle_key).decode()
    print(decoded)

