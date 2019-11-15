from setuptools import setup

setup(
    name='iauploads',
    version='1.0.0',
    packages=['iauploads'],
    url='https://arquivo.pt',
    license='',
    author='Daniel Bicho',
    author_email='daniel.bicho@fccn.pt',
    description='Tools to upload Arquivo.pt contents for IA.',
    install_requires=[
        "internetarchive",
        "PyYAML"
    ],
    entry_points={
            'console_scripts': [
                'ia-upload=upload:main'
                'ia-generate-items=generate_ia_items:main'
            ],
    }
)
