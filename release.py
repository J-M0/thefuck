#!/usr/bin/env python
from subprocess import call
import re

with open('setup.cfg', 'r') as sf:
    lines = sf.readlines()

for i, line in enumerate(lines):
    match = re.match(r"version = (\d+)\.(\d+)", line)
    if match:
        major, minor = match.groups()
        version = "{}.{}".format(major, int(minor) + 1)
        lines[i] = "version = {}\n".format(version)
        break

with open('setup.cfg', 'w') as sf:
    sf.writelines(lines)

call('git pull', shell=True)
call('git commit -am "Bump to {}"'.format(version), shell=True)
call('git tag {}'.format(version), shell=True)
call('git push', shell=True)
call('git push --tags', shell=True)

call('rm -rf dist/*', shell=True)
call('pyproject-build')
call('twine upload dist/*', shell=True)
