#!/usr/bin/env python
from setuptools import setup
import pkg_resources
import sys


try:
    if int(pkg_resources.get_distribution("pip").version.split('.')[0]) < 6:
        print('pip older than 6.0 not supported, please upgrade pip with:\n\n'
              '    pip install -U pip')
        sys.exit(-1)
except pkg_resources.DistributionNotFound:
    pass


version = sys.version_info[:2]
if version < (2, 7):
    print('thefuck requires Python version 2.7 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)
elif (3, 0) < version < (3, 5):
    print('thefuck requires Python version 3.5 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)


if sys.platform == "win32":
    scripts = ['scripts\\fuck.bat', 'scripts\\fuck.ps1']
    entry_points = {'console_scripts': [
                  'thefuck = thefuck.entrypoints.main:main',
                  'thefuck_firstuse = thefuck.entrypoints.not_configured:main']}
else:
    scripts = []
    entry_points = {'console_scripts': [
                  'thefuck = thefuck.entrypoints.main:main',
                  'fuck = thefuck.entrypoints.not_configured:main']}

setup(
    scripts=scripts,
    entry_points=entry_points,
)
