import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()


__version__ = '0.0.0'

REPO_NAME='chicken-disease-classification'
AUTHORUSERNAME='balaji-bhaskarr'
SRC_REPO = 'cnn_Classifier'
AUTHOR_EMAIL = 'balaji.bhaskarr@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHORUSERNAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for CNN app',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHORUSERNAME}/{REPO_NAME}',
    project_urls = {
        'Bug Tracker': f'https://github.com/{AUTHORUSERNAME}/{REPO_NAME}/issues',
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)