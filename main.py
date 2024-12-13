from urllib.parse import parse_qs, urlsplit
from db_config import Format_SQL
from util import user_input, open_file, insert_to_db, check_db
from __init__ import URl
import requests


def scrape_api(parameters):
    for item in parameters:
        parsed_params = parse_qs(urlsplit(item).query)

        respons = requests.get(URl, parsed_params)
        data = respons.json()
        print(data)

        for info in data['body']['data']['results']:
            name = info['fields']['plugin']['title']
            release_date = info['fields']['date']
            last_update = info['fields']['modified']
            number_of_rating = info['fields']['plugin']['num_ratings']
            rating = info['fields']['plugin']['rating']
            plugin_link = info['fields']['permalink.url.raw']

            return Format_SQL(
                Name=name,
                Release_Date=release_date,
                Last_Update=last_update,
                Number_of_Rating=number_of_rating,
                Rating=rating,
                PLugin_link=plugin_link
            )


def main():
    filename = user_input()
    parameters = open_file(filename)
    result = scrape_api(parameters)
    if not check_db(result):
        insert_to_db(result)
        print(f'Plugin inserted to database: {result.Name}')
    else:
        print(f'Record already exist: {result.Name}')


# if __name__ == '__main__':
#     # scrape_api('https://public-api.wordpress.com/rest/v1.3/marketplace/search?http_envelope=1&fields%5B%5D=blog_icon_url&fields%5B%5D=comment_count&fields%5B%5D=plugin.excerpt&fields%5B%5D=like_count&fields%5B%5D=modified&fields%5B%5D=modified_gmt&fields%5B%5D=plugin.title&fields%5B%5D=author&fields%5B%5D=plugin.author&fields%5B%5D=author_login&fields%5B%5D=blog_id&fields%5B%5D=date&fields%5B%5D=date_gmt&fields%5B%5D=permalink.url.raw&fields%5B%5D=post_id&fields%5B%5D=post_type&fields%5B%5D=slug&fields%5B%5D=plugin.tested&fields%5B%5D=plugin.stable_tag&fields%5B%5D=plugin.active_installs&fields%5B%5D=plugin.support_threads&fields%5B%5D=plugin.support_threads_resolved&fields%5B%5D=plugin.rating&fields%5B%5D=plugin.num_ratings&fields%5B%5D=plugin.icons&fields%5B%5D=plugin.store_product_monthly_id&fields%5B%5D=plugin.store_product_yearly_id&fields%5B%5D=plugin.premium_slug&fields%5B%5D=plugin.product_slug&fields%5B%5D=plugin.software_slug&fields%5B%5D=plugin.org_slug&page_handle=ZnJvbT0xMDAmYWxnPW1hcmtldHBsYWNlJTNBc2VhcmNoJTJGMSZzZXNzaW9uX2lkPVFzYmYlMjhu&query=&sort=active_installs&size=20&lang=en&group_id=wporg&track_total_hits=true')
#     main()

print(scrape_api('parameter_file'))