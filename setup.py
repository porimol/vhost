from setuptools import setup

setup(
    name = "VirtualHost",
    version = "1.1",
    py_modules = "vhost",
    install_requires = [
        'Click'
    ],
    entry_points = '''
        [console_scripts]
        vhost=vhost.vhost:main
    ''',
    author = "P.C ROY",
    author_email = "p.c_roy@yahoo.com",
    description = ("Apache(linux) virtual host creator"),
    license = "MIT",
    keywords = ["vhost", "virtual host"],
    url = "https://github.com/porimol/vhost",
    download_url = 'https://github.com/porimol/vhost/archive/master.zip',
)