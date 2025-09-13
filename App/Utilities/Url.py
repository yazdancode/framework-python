class Url:
    @staticmethod
    def current() -> str:
        return Config.BASE_URL

    @staticmethod
    def current_route() -> str:
        uri = os.environ.get('REQUEST_URI', '/')
        return uri.split('?')[0]
