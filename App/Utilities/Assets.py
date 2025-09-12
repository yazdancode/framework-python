from constants.Constants import get_env_variable


class Assets:
    @staticmethod
    def _build_path(folder, route):
        base_url = get_env_variable("HOST").rstrip("/")
        folder_path = f"/assets/{folder}" if folder else "/assets"
        return f"{base_url}{folder_path}/{route.lstrip('/')}"

    @staticmethod
    def get(route):
        return Assets._build_path("", route)

    @staticmethod
    def css(route):
        return Assets._build_path("css", route)

    @staticmethod
    def js(route):
        return Assets._build_path("js", route)

    @staticmethod
    def img(route):
        return Assets._build_path("img", route)

    @staticmethod
    def fonts(route):
        return Assets._build_path("fonts", route)
