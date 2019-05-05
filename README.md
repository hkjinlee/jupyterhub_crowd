# JupyterHub Crowd Authenticator

[Crowd](https://www.atlassian.com/software/crowd) authenticator for [JupyterHub](https://github.com/jupyterhub).

## Installation
Install with pip:
```
pip install jupyterhub_crowd
```

## Setup

In ```jupyterhub_config.py```, add:
```
c.JupyterHub.authenticator_class = 'jupyterhub_crowd.Crowthenticator'
c.Crowthenticator.server_url = 'https://crowd.xxx.yyy/'
c.Crowthenticator.server_appname = 'foo'
c.Crowthenticator.server_password = 'bar'
c.Crowthenticator.username_from_email = True
```