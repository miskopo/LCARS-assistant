from setuptools import setup

setup(
    name='lcars-assistant',
    version='0.0.1',
    packages=['lcars-assistant'],
    entry_points={
        'console_scripts': [
            'lcars-assistant = lcars-assistant.__main__:main'
         ]
    })
