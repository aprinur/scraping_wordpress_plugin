from source.util import user_input, insert_to_db, check_db, save_to_file, del_db
from source.scrape import scrape_api


def main():
    total_pages, filename, sheet_title, sheet_desc = user_input()

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
    if filename:
        save_to_file(filename, sheet_title, sheet_desc)
        del_db('wordpress_plugin.db')
    print('Scraping finish')


if __name__ == '__main__':
    main()
