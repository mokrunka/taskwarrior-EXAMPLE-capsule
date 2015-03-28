import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import uuid

from taskwarrior_EXAMPLE_capsule import __version__ as version_string


requirements_path = os.path.join(
    os.path.dirname(__file__),
    'requirements.txt',
)
try:
    from pip.req import parse_requirements
    requirements = [
        str(req.req) for req in parse_requirements(
            requirements_path,
            session=uuid.uuid1()
        )
    ]
except ImportError:
    requirements = []
    with open(requirements_path, 'r') as in_:
        requirements = [
            req for req in in_.readlines()
            if not req.startswith('-') and
            not req.startswith('#')
        ]


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


setup(
    # CHANGEME: Set this to the name of your capsule
    name='taskwarrior-EXAMPLE-capsule',
    version=version_string,
    # CHANGEME: Set this to your capsule's project URL on github OR
    # delete this line.
    url='https://github.com/coddingtonbear/taskwarrior-EXAMPLE-capsule',
    # CHANGEME: Enter a short description of what your capsule does her
    description='This is just an example capsule',
    # CHANGEME: Enter your name (or delete this line).
    author='Your Name',
    # CHANGEME: Enter your e-mail address (or delete this line).
    author_email='your_email@somedomain.com',
    install_requires=requirements,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    packages=find_packages(),
    entry_points={
        'taskwarrior_capsules': [
            # CHANGEME: Change this such that:
            # 1) The EXAMPLE before the = sign is the name of the command
            #    as you'll execute it from the taskwarrior command-line.
            # 2) The string after the = sign is the module path to your
            #    capsule's class.
            'EXAMPLE = taskwarrior_EXAMPLE_capsule.capsule:EXAMPLE',
        ]
    },
)
