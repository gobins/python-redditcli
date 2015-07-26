import logging

LOG = logging.getLogger(__name__)


class Resource(object):
    defaults = {}

    def __init__(self, manager, data):
        self.manager = manager
        self._data = data
        self._set_defaults()
        self._set_attributes()

    def _set_defaults(self):
        for k,v in self.defaults.iteritems():
            if k not in self._data:
                self._data[k] = v

    def _set_attributes(self):
        for k, v in self._data.iteritems():
            try:
                setattr(self, k, v)
            except AttributeError:
                pass