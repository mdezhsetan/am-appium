import os
from datetime import datetime

import pandas as pd


class Accounts:
    default_username = "qaaccount@gmx.com"
    default_password = "welcome20!@#"
    password = "Welcome20!"

    def __init__(self):
        self.new_username = None

    @staticmethod
    def current_time_string():
        now = datetime.now()
        return now.strftime("%Y%m%d_%H%M")

    def new_account_username(self):
        self.new_username = "test_account_" + Accounts.current_time_string() + "@qa.com"
        data = {
            'username': [self.new_username],
            'password': ['welcome20!']
        }
        df = pd.DataFrame(data)
        df.to_csv(os.getcwd() + '\\Data\\test_accounts.csv', mode='a', index=False, header=False)
        return self.new_username
