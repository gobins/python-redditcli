import requests
import requests.auth
import ConfigParser


def get_auth_token():
    config = ConfigParser.ConfigParser()
    config.read('client_secrets.ini')
    client_auth = requests.auth.HTTPBasicAuth(
        config.get('reddit_bot', 'client_id'),
        config.get('reddit_bot', 'client_secret')
    )
    post_data = {
        "grant_type": "password",
        "username": config.get('reddit_bot', 'user'),
        "password": config.get('reddit_bot', 'password')
    }
    headers = {
        "User-Agent": "python-app/0.1 by "+config.get('reddit_bot', 'user')
    }

    response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=client_auth,
        data=post_data,
        headers=headers
    )
    print response.json()


def main():
    get_auth_token()


if __name__ == "__main__":
    main()
