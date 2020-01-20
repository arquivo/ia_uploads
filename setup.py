from setuptools import setup

setup(
    name='iauploads',
    version='1.3.7',
    packages=['iauploads'],
    url='https://arquivo.pt',
    license='',
    author='Daniel Bicho',
    author_email='daniel.bicho@fccn.pt',
    description='Tools to upload Arquivo.pt contents to IA.',
    install_requires=[
        "internetarchive",
        "PyYAML"
    ],
    entry_points={
            'console_scripts': [
                'ia-upload=iauploads.upload:main',
                'ia-generate-items=iauploads.generate_ia_items:main',
            ],
    }
)
