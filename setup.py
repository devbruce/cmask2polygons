import os
from setuptools import setup


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(ROOT_DIR, 'README.md')

setup(
    name='cmask2polygons',
    author='devbruce',
    author_email='bruce93k@gmail.com',
    description='Convert Color label mask to Polygons per class',
    long_description=open(README_PATH, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    version='1.1.3',
    url='https://github.com/DevBruce/cmask2polygons',
    py_modules=['cmask2polygons'],
    keywords=['mask', 'polygon'],
    python_requires='>=3.6.5',
    install_requires=['numpy>=1.19.0', 'opencv-python>=4.3.0.36'],
)
