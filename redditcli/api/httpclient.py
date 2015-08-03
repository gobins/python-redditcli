import requests
import logging

LOG = logging.getLogger(__name__)


def log_request(func):
    def decorator(self, *args, **kwargs):
        resp = func(self, *args, **kwargs)
        #LOG.debug("HTTP %s %s %d" % (resp.request.method, resp.url, resp.status_code))
        return resp
    return decorator


class HTTPClient(object):

    log = logging.getLogger(__name__)

    def __init__(self, base_api_url, user_agent, auth_token=None):
        self.log.debug('Initializing HTTPClient class.')
        self.base_api_url = base_api_url
        self.log.debug('Base API url set to: %s', self.base_api_url)
        self.log.debug('User Agent is set to: %s', user_agent)
        self.auth_token = auth_token
        self.user_agent = user_agent

    @log_request
    def get(self, url, headers=None):
        self.log.debug('Initiating GET request to: %s', self.base_api_url+url)
        headers = self._update_headers(headers)
        resp = requests.get(self.base_api_url + url, headers=headers)
        #return requests.get(self.base_api_url + url, headers=headers)
        return resp

    @log_request
    def post(self, url, body, headers=None):
        headers = self._update_headers(headers)
        content_type = headers.get('content-type', 'application/json')
        headers['content-type'] = content_type
        return requests.post(self.base_api_url + url, body, headers=headers)

    @log_request
    def _update_headers(self, headers):
        if not headers:
            headers = {}

        auth_token = headers.get('Authorization', self.auth_token)
        # TODO Not really clear what's happening here
        if auth_token:
            headers['Authorization'] = "bearer "+auth_token

        user_agent = headers.get('User-Agent', self.user_agent)
        if user_agent:
            headers['User-Agent'] = user_agent
        return headers
