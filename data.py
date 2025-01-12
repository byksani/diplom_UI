class Urls:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE = f'{MAIN_PAGE}login'
    FORGOT_PASSWORD = f'{MAIN_PAGE}forgot-password'
    RESET_PASSWORD = f'{MAIN_PAGE}reset-password'
    FEED = f'{MAIN_PAGE}feed'
    PROFILE_PAGE = f'{MAIN_PAGE}account/profile'
    ORDER_HISTORY = f'{MAIN_PAGE}account/order-history'

class Requests:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    REGISTER = f"{BASE_URL}/auth/register"
    LOGIN = f"{BASE_URL}/auth/login"
    USER = f"{BASE_URL}/auth/user"
    ORDERS = f"{BASE_URL}/orders"

class Ingredients:
    DEFAULT_INGREDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
