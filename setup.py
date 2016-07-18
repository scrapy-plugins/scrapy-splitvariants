from setuptools import setup

setup(
    name='scrapy-splitvariants',
    version='0.1.0',
    license='BSD',
    description='Scrapy spider middleware to split an item into multiple items on a multi-valued key',
    author='Scrapinghub',
    author_email='info@scrapinghub.com',
    url='http://github.com/scrapy-plugins/scrapy-splitvariants',
    packages=['scrapy_splitvariants'],
    platforms=['Any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=['scrapy']
)
