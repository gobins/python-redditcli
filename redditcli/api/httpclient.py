import requests
import logging

LOG = logging.getLogger(__name__)


def log_request(func):
    def decorator(self, *args, **kwargs):
        resp = func(self, *args, **kwargs)
        LOG.debug("HTTP %s %s %d" % (resp.request.method, resp.url, resp.status_code))
        return resp
    return decorator


class HTTPClient(object):
    def __init__(self, base_url, user_agent, auth_token=None):
        self.base_url = base_url
        self.auth_token = auth_token
        self.user_agent = user_agent

    @log_request
    def get(self, url, headers=None):
        headers = self._update_headers(headers)
        return requests.get(self.base_url + url, headers=headers)

    @log_request
    def post(self, url, body, headers=None):
        headers = self._update_headers(headers)
        content_type = headers.get('content-type', 'application/json')
        headers['content-type'] = content_type
        return requests.post(self.base_url + url, body, headers=headers)

    @log_request
    def _update_headers(self, headers):
        if not headers:
            headers = {}

        auth_token = headers.get('Authorization', "bearer "+ self.auth_token)
        # TODO Not really clear what's happening here
        if auth_token:
            headers['Authorization'] = auth_token

        user_agent = headers.get('User-Agent', self.user_agent)
        if user_agent:
            headers['User-Agent'] = user_agent
