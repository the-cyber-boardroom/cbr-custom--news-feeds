from osbot_fast_api.api.Fast_API                        import Fast_API
from cbr_custom_news_feeds.fast_api.routes.Routes__Info import Routes__Info


class News_Feeds__Fast_API(Fast_API):
    base_path  : str  = '/'
    enable_cors: bool = True

    def setup_routes(self):
        self.add_routes(Routes__Info)
