import os


def open_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print('File not found')
    except FileExistsError:
        print('File corrupted')


def user_input():
    while True:
        name = input('Input filename: ')
        if os.path.exists(name):
            return name
        else:
            print("File doesn't exist in folder Scraping_Wordpress_plugin")


def insert_to_db(result):
    session.add(result)
    session.commit()
    print('Insert to db success')


def check_db(data):
    exist = session.query(Format_SQL).filter_by(Name=data.Name).first()
    return exist is not None