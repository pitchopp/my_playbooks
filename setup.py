from setuptools import setup


setup(
    name='vps-playbooks',
    version='0.1.0',
    description='ansible playbooks for vps setup',
    author='Amine Sghir',
    author_email='sghir.ma@gmail.com',
    packages=['vps_playbooks'],
    install_requires=[
        'ansible^7.3.0'
    ]
)