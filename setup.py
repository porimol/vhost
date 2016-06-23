from setuptools import setup

setup(
    name = "VirtualHost",
    version = "0.0.2",
    py_modules = "VirtualHost",
    install_requires = [
        'Click'
    ],
    packages=['VirtualHost'],
    entry_points = '''
        [console_scripts]
        vhost=VirtualHost.vhost:main
    ''',
    author = "P.C ROY",
    author_email = "p.c_roy@yahoo.com",
    description = ("Apache(linux) virtual host creator"),
    license = "MIT",
    keywords = ["vhost", "virtual host"],
    url = "https://github.com/porimol/vhost",
)