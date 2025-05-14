from setuptools import setup, find_packages

setup(
    name='myterminaleditor',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.1.1',
        'xterm==5.3.0',
        'codemirror==5.65.2',
        'requests==2.26.0',
    ],
    entry_points={
        'console_scripts': [
            'run-server=myterminaleditor.app:run_server',  # app.py의 run_server 함수 호출
        ],
    },
)
