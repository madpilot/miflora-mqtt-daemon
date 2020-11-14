from setuptools import setup
setup(
  name='miflora-mqtt-daemon',
  version='0.0.dev1',
  url='https://github.com/ThomDietrich/miflora-mqtt-daemon',
  author='Thomas Dietrich',
  author_email='thomas.dietrich@tu-ilmenau.de',
  scripts=['miflora-mqtt-daemon.py'],
  install_requires=[
    'miflora==0.6',
    'bluepy==1.3.0',
    'btlewrap==0.0.9',
    'paho-mqtt==1.4.0',
    'wheel==0.29.0',
    'sdnotify==0.3.1',
    'colorama==0.3.9',
    'Unidecode==0.4.21',
  ]
)