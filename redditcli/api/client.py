from __future__ import print_function
import requests
import logging

from redditcli.api import httpclient
from redditcli.api import account


class Client(object):

    log = logging.getLogger(__name__)

    def __init__(self, base_api_url, auth_url, username=None, password=None,
                 client_id=None, client_secret=None, user_agent=None, auth_token=None):

        if auth_url:
            (auth_token, expires_in, scope, token_type) = (
                self.get_auth_token(auth_url, username, password,
                                    client_id, client_secret)
            )
        self.log.debug('Initializing Client class')

        if not base_api_url:
            base_api_url = 'https://oauth.reddit.com'

        if not user_agent:
            user_agent = "python-app/0.1 by RedditCli"

        self.http_client = httpclient.HTTPClient(base_api_url, user_agent, auth_token)

        #Create all Resource Managers
        self.account = account.AccountManager(self)

    def get_auth_token(self, auth_url=None, username=None, password=None,
                       client_id=None, client_secret=None):

        client_auth = requests.auth.HTTPBasicAuth(
            client_id,
            client_secret
        )
        post_data = {
            "grant_type": "password",
            "username": username,
            "password": password
        }
        headers = {
            "User-Agent": "python-app/0.1 by RedditCli"
        }

        response = requests.post(
            auth_url,
            #"https://www.reddit.com/api/v1/access_token",
            auth=client_auth,
            data=post_data,
            headers=headers
        )
        data = response.json()
        return data['access_token'], data['expires_in'], data['scope'], data['token_type']


def getClient(base_api_url=None, auth_url=None, username=None,
              password=None, client_id=None, client_secret=None, user_agent=None, auth_token=None):
    log = logging.getLogger(__name__)
    return Client(
        base_api_url=base_api_url,
        auth_url=auth_url,
        username=username,
        password=password,
        client_id=client_id,
        client_secret=client_secret,
        auth_token=auth_token
    )