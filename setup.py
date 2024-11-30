with open("README.md","r",encoding="utf-8") as f:
    datatext=f.read()
from setuptools import setup
 
setup(
    name='AppDT',
    version='1.7.0',
    description='(This Is A Chinese Package)此工具箱可以帮您快速构建Windows™应用程序，也可以快速生成安装包',
    long_description=datatext,
    long_description_content_type="text/markdown",
    author='xumouren225588',
    author_email='xumouren225588@163.com',
    url="https://github.com/xumouren225588",
    packages=['AppDT'],
    license='MIT',
    install_requires=[
        'pyinstaller',
        'PyQt5',
        'chardet'
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'adt=AppDT.whlcode:adt',
        ],
    },
    classifiers=[
        
        "Programming Language :: Python",
        "Operating System :: Microsoft :: Windows",
    ],
)
