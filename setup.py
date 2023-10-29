from setuptools import setup, find_packages

setup(
    name='yourflasklib',
    version='0.1',
    description='A simple Flask library for UI components',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)