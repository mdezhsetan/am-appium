import os
from datetime import datetime

import pandas as pd

from Resources.base_page import BasePage


class Accounts(BasePage):

    def current_time_string(self):
        now = datetime.now()
        return now.strftime("%Y%m%d_%H%M%S")

    def new_account_username(self):
        self.new_username = "test" + self.current_time_string() + "@qa.com"
        data = {
            'username': [self.new_username],
            'password': ['welcome20!']
        }
        df = pd.DataFrame(data)
        df.to_csv(os.getcwd() + '\\Data\\test_accounts.csv', mode='a', index=False, header=False)
        return self.new_username
