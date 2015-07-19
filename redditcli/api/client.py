from __future__ import print_function
import requests
from redditcli.api import httpclient


class Client(object):
    def __init__(self, base_url, auth_url, username=None, password=None,
                 client_id=None, client_secret=None, user_agent=None):

        if auth_url:
            (auth_token, expires_in, scope, token_type) = (
                self.get_auth(auth_url, username, password,
                              client_id, client_secret)
            )

        if not base_url:
            base_url = 'http://reddit.com'

        if not user_agent:
            user_agent = "python-app/0.1 by RedditCli"

        self.http_client = httpclient.HTTPClient(base_url, auth_token, user_agent)

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
