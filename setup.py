from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='Duke',
    version='0.0.1',
    packages=['duke', 'duke.test'],
    install_requires=requirements,
    license='Proprietary',
    test_suite='',
    classifiers=[
        'License :: Other/Proprietary License'
    ]
)
