import logging
import json

log = logging.getLogger(__name__)


class Resource(object):
    resource_name = 'Nothing'
    defaults = {}

    def __init__(self, manager, data):
        log.debug('Initializing Resource class')
        self.manager = manager
        self._data = data
        self._set_defaults()
        self._set_attributes()

    def _set_defaults(self):
        for k, v in self.defaults.iteritems():
            if k not in self._data:
                self._data[k] = v

    def _set_attributes(self):
        for k, v in self._data.iteritems():
            try:
                setattr(self, k, v)
            except AttributeError:
                pass

    def __str__(self):
        vals = ", ".join(["%s='%s'" % (n, v) for n, v in self._data.iteritems()])

        return "%s [%s]" % (self.resource_name, vals)


class APIException(Exception):
    def __init__(self, error_code=None, error_message=None):
        log.debug('Initializing APIException.')
        super(APIException, self).__init__(error_message)
        self.error_code = error_code
        self.error_message = error_message


def _check_items(obj, searches):
    try:
        return all(getattr(obj, attr) == value for (attr, value) in searches)
    except AttributeError:
        return False


def get_json(response):
    json_function = getattr(response, 'json', None)
    if callable(json_function):
        return response.json()
    else:
        return json.loads(response.content)


def extract_json(response, response_key):
    if response_key is not None:
        return get_json(response)[response_key]
    else:
        return get_json(response)


class ResourceManager(object):
    resource_class = None

    def __init__(self, client):
        log.debug('Initializing Base ResourceManager')
        self.client = client

    def find(self, **kwargs):
        return [i for i in self.list() if _check_items(i, kwargs.items())]

    def _ensure_not_empty(self, **kwargs):
        for name, value in kwargs.iteritems():
            if value is None or (isinstance(value, str) and len(value) == 0):
                raise APIException('%s is missing field "%s"' % (self.resource_class.__name__, name))

    def _copy_if_defined(self, data, **kwargs):
        for name, value in kwargs.iteritems():
            if value is not None:
                data[name] = value

    def _create(self, url, data, response_key=None, dump_json=True):
        if dump_json:
            data = json.dumps(data)

        resp = self.client.http_client.post(url, data)

        if resp.status_code != 201:
            self._raise_api_exception(resp)

        return self.resource_class(self, extract_json(resp, response_key))

    def _get(self, url, response_key=None):
        resp = self.client.http_client.get(url)
        if resp.status_code == 200:
            return self.resource_class(self, extract_json(resp, response_key))

    def _raise_api_exception(self, resp):
        try:
            error_data = get_json(resp).get("faultstring")
        except ValueError:
            error_data = resp.content
        raise APIException(error_code=resp.status_code, error_message=error_data)