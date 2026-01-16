import os

class Config:
    API_ID = int(os.getenv("API_ID", 20366634))
    API_HASH = os.getenv("API_HASH", '72095ec36984aa9ceb0dbaa9cec31559')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '8277167999:AAEuiEqwdpl3m0ZzRaaGgkTwHGFEIjFQn28')
