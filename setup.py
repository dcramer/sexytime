from setuptools import setup, find_packages

setup(name='sexytime',
    version='0.1.0',
    description='',
    author='DISQUS',
    install_requires=['pytz'],
    license='Apache License 2.0',
    tests_require=['nose', 'unittest2'],
    test_suite='nose.collector',
    url='http://www.disqus.com',
    packages=find_packages(),
    include_package_data=True,
)
