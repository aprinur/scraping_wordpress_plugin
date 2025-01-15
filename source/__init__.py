import os
import datetime
import tempfile
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


API = 'https://public-api.wordpress.com/rest/v1.3/marketplace/search?http_envelope=1&fields%5B%5D=blog_icon_url&fields%5B%5D=comment_count&fields%5B%5D=plugin.excerpt&fields%5B%5D=like_count&fields%5B%5D=modified&fields%5B%5D=modified_gmt&fields%5B%5D=plugin.title&fields%5B%5D=author&fields%5B%5D=plugin.author&fields%5B%5D=author_login&fields%5B%5D=blog_id&fields%5B%5D=date&fields%5B%5D=date_gmt&fields%5B%5D=permalink.url.raw&fields%5B%5D=post_id&fields%5B%5D=post_type&fields%5B%5D=slug&fields%5B%5D=plugin.tested&fields%5B%5D=plugin.stable_tag&fields%5B%5D=plugin.active_installs&fields%5B%5D=plugin.support_threads&fields%5B%5D=plugin.support_threads_resolved&fields%5B%5D=plugin.rating&fields%5B%5D=plugin.num_ratings&fields%5B%5D=plugin.icons&fields%5B%5D=plugin.store_product_monthly_id&fields%5B%5D=plugin.store_product_yearly_id&fields%5B%5D=plugin.premium_slug&fields%5B%5D=plugin.product_slug&fields%5B%5D=plugin.software_slug&fields%5B%5D=plugin.org_slug&page_handle={query}&query=&sort=active_installs&size=20&lang=en&group_id=wporg&track_total_hits=true'
DATE = datetime.datetime.now().strftime('%d-%b-%Y_%H-%M-%S')


def get_db_path():
    """
    Getting path to save the database

    args: None
    return: None
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, 'WordPress_plugins.db')
        Path(db_path).touch()
        print(f'Database will be saved in: {db_path}')
        return f'sqlite:///{db_path}'
    except:
        try:
            home_dir = str(Path.home())
            db_path = os.path.join(home_dir, "WordPress_plugins.db")
            Path(db_path).touch()
            print(f'Database will be saved in: {db_path}')
            return f"slite:///{db_path}"
        except:
            temp_dir = tempfile.gettempdir()
            db_path = os.path.join(temp_dir, 'WordPress_plugins.db')
            print(f'Database will be saved in: {db_path}')
            return f'sqlite:///{db_path}'


DB_URL = get_db_path()
engine = create_engine(DB_URL, echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)

sql_reserved_keyword = {
    "select", "insert", "update", "delete", "from", "where", "join",
    "group", "by", "order", "limit", "table", "create", "drop",
    "alter", "index", "and", "or", "not", "null", "into", "values", "all"
}
