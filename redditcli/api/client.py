from __future__ import print_function
import requests
from redditcli.api import httpclient
import logging


class Client(object):

    log = logging.getLogger(__name__)

    def __init__(self, base_url, auth_url, username=None, password=None,
                 client_id=None, client_secret=None, user_agent=None, auth_token=None):

        if auth_url:
            (auth_token, expires_in, scope, token_type) = (
                self.get_auth_token(auth_url, username, password,
                                    client_id, client_secret)
            )
        self.log.debug('Initializing Client class')

        if not base_url:
            base_url = 'http://reddit.com'

        if not user_agent:
            user_agent = "python-app/0.1 by RedditCli"

        self.http_client = httpclient.HTTPClient(base_url, auth_token, user_agent)

    def get_auth_token(self, auth_url=None, username=None, password=None,
                       client_id=None, client_secret=None):

        self.log.debug('Retrieving authentication token')
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
        print(data['access_token'])
        return data['access_token'], data['expires_in'], data['scope'], data['token_type']


def getClient(base_url=None, auth_url=None, username=None,
              password=None, client_id=None, client_secret=None, user_agent=None, auth_token=None):
    return Client(
        base_url=base_url,
        auth_url=auth_url,
        username=username,
        password=password,
        client_id=client_id,
        client_secret=client_secret,
        auth_token=auth_token
    )