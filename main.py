import os
from dotenv import load_dotenv
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


load_dotenv()
my_app_id = int(os.environ.get("APP_ID"))
my_app_secret = os.environ.get("APP_SECRET")
my_access_token = os.environ.get("ACCESS_TOKEN")
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

my_account = AdAccount(os.environ.get("AD_ACCOUNT_ID"))
campaigns = my_account.get_campaigns()
print(campaigns)
