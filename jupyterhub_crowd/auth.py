from crowd import CrowdServer
from tornado import gen
from jupyterhub.auth import LocalAuthenticator
from traitlets import Unicode, Bool
import logging

class Crowthenticator(LocalAuthenticator):
    server_url = Unicode(config=True, help='Crowd Server URL')
    server_appname = Unicode(config=True, help='Crowd app name')
    server_password = Unicode(config=True, help='Crowd app password')
    username_from_email = Bool(False, config=True, help='Use email address as userid')

    @gen.coroutine
    def authenticate(self, handler, data=None):
        crowd = CrowdServer(self.server_url, self.server_appname, self.server_password)
        auth = crowd.auth_user(data['username'], data['password'])
        if auth:
            return self._get_username(auth)
        else:
            return None

    def _get_username(self, auth):
        logging.debug(auth)
        if self.username_from_email:
            return auth['email'].split('@')[0]
        else:
            return auth
