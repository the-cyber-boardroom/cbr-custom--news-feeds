import cbr_custom_news_feeds
from osbot_fast_api.api.Fast_API                                                            import Fast_API
from osbot_utils.utils.Files                                                                import path_combine
from cbr_custom_news_feeds.fast_api.routes.Routes__Info                                     import Routes__Info
from cbr_custom_news_feeds.providers.cyber_security.hacker_news.routes.Routes__Hacker_News  import Routes__Hacker_News



class News_Feeds__Fast_API(Fast_API):
    base_path  : str  = '/'
    enable_cors: bool = True

    def setup_routes(self):
        self.add_routes(Routes__Info)
        self.add_routes(Routes__Hacker_News)

    def path_static_folder(self):
        return path_combine(cbr_custom_news_feeds.path, 'open_api')
