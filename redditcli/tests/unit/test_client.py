import testtools

from redditcli.api import httpclient
from requests_mock.contrib import fixture


class TestClient(testtools.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()
        self.responses = self.useFixture(fixture.Fixture())
        self.enpoint = 'http://localhost:8000'
        self.project_id = 'project_id'
        self.httpclient = httpclient.HTTPClient('http://localhost:8000','test_agent','12345')


class WhenTestingClientInit(TestClient):

    def test_update_header(self):
        c = self.httpclient