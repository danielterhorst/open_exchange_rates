from setuptools import setup

setup(
    name='open_exchange_rates',
    version='1.0a1',
    description='An Open Exchange Rates python client',
    url='https://github.com/danielterhorst/open_exchange_rates',
    author='Daniel ter Horst',
    author_email='mail@danielterhorst.nl',
    license='GNU General Public License v2 (GPLv2)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'requests'
    ],
    packages=['open_exchange_rates'],
    zip_safe=False
)
