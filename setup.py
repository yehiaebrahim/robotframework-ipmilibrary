#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, Command, find_packages
import sys
import os
import subprocess
sys.path.insert(0, 'src')

name = 'robotframework-ipmilibrary'
version_py = os.path.join(os.path.dirname(__file__), 'src', 'IpmiLibrary',
        'version.py')
try:
    version = subprocess.Popen(
            ['git', 'describe', '--tags', '--always', '--dirty'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT).communicate()[0].rstrip()
    with open(version_py, 'w') as f:
        f.write('# This file was autogenerated by setup.py\n')
        f.write('__version__ = \'%s\'\n' % (version,))
except (OSError, subprocess.CalledProcessError, IOError) as e:
    try:
        with open(version_py, 'r') as f:
            d = dict()
            exec(f.read(), d)
            version = d['__version__']
    except IOError:
        version = 'unknown'

version = version.decode('utf-8')

with open('README.rst') as f:
    readme = f.read()

class run_build_libdoc(Command):
    description = "Build Robot Framework library documentation"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import robot.libdoc
        except ImportError:
            print("build_libdoc requires the Robot Framework package.")
            sys.exit(-1)

        robot.libdoc.libdoc('SnmpLibrary', 'docs/SnmpLibrary.html')

def main():
    setup(name = name,
            version = version,
            description = 'IPMI Library for Robot Framework',
            long_description = readme,
            author = 'Michael Walle, Heiko Thiery',
            author_email = 'michael.walle@kontron.com, heiko.thiery@kontron.com',
            url = 'https://github.com/kontron/robotframework-ipmilibrary',
            download_url = 'https://pypi.python.org/pypi/robotframework-ipmilibrary',
            package_dir = { '' : 'src' },
            license = 'Apache License 2.0',
            classifiers = [
                'Development Status :: 4 - Beta',
                'Framework :: Robot Framework',
                'License :: OSI Approved :: Apache Software License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Testing',
            ],
            packages = find_packages(exclude="test"),
            install_requires = [ 'robotframework', 'python-ipmi' ]
    )

if __name__ == '__main__':
    main()
