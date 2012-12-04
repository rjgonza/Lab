try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = {
	'description': 'ex48',
	'author': 'Ramon Gonzalez',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'rjgonza@gmail.com.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'ex48'
}

setup(**config)
