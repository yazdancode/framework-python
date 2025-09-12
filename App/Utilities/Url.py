from configs.Config import Config


class Url:
    @staticmethod
    def base_url() -> str:
        return Config.BASE_URL
