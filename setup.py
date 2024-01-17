from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='flask_todo',
    version='0.0',
    description='A To-Do List built with Flask',
    author='<Nazar>',
    author_email='<nazar.shyika.ir.2022@lpnu.ua>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)