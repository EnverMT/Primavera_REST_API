from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='Primavera_REST_Api',
    version='0.0.1',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=['Primavera_REST_Api'],
    url='',
    license='MIT',
    author='EnverMT',
    author_email='anvarmtg@gmail.com',
    install_requires=['requests'],
    keywords=['primavera', 'rest', 'api'],
    description='Primavera EPPM REST API client',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT",
        "Operating System :: OS Independent",
    ],
)
