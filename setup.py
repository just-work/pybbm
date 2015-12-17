from setuptools import setup, find_packages

setup(
    version='0.16.1-enot17',
    description='PyBB Modified. Django forum application',
    long_description=open('README.rst').read(),
    author='Pavel Zhukov',
    author_email='gelios@gmail.com',
    name='pybbm',
    url='http://www.pybbm.org/',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['pybb/templates', 'pybb/static']},
    install_requires=[
        'django-annoying',
    ],
    test_suite='runtests.runtests',
    license="BSD",
    keywords="django application forum board",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
