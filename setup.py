import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='jupyterhub_crowd',
	version='0.0.2',
	author='Jin, Heonkyu',
	author_email='heonkyu.jin@gmail.com',
	description='Crowd authenticator for JupyterHub',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/hkjinlee/jupyterhub_crowd',
	packages=setuptools.find_packages(),
	install_requires=[
		'jupyterhub',
		'Crowd',
	],
	classifiers=[
		"Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],	
)