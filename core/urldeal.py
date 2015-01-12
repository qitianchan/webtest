__author__ = 'ChenQT'
import app
def config_urls():
    urls_tuple = (
        '/index', 'app.home.index.Index',
    )
    return urls_tuple