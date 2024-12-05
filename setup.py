from setuptools import setup, find_packages

setup(
    name='Fathipy',
    version='1.0',
    packages=find_packages(),
    install_requires=["numpy","PyQt5"],
    description=' Clases para representar y manipular vectores, partículas del modelo estándar.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Fathima Viviana Lopez Nataren',
    author_email='fath.nataren@ciecnias.unam.mx',
    url='https://github.com/Fath1710/Fathipy_package',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
     python_requires=">=3.8",
     entry_points={
        'console_scripts': [
            'Fathipy_gui = Fathipy.gui:main',
        ],
    },
)

