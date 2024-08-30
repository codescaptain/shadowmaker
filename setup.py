from setuptools import setup, find_packages
import shadowmaker

setup(
    name='shadowmaker',
    version=shadowmaker.__version__,
    description='A simple tool for creating silhouette images using a GUI',
    author='Ahmet Kaptan',
    author_email='codescaptain@gmail.com',
    url='https://github.com/codescaptain/shadowmaker',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'opencv-python',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'shadowmaker=shadowmaker.gui:main',
        ],
    },
)
