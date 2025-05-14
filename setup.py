from setuptools import setup, find_packages

setup(
    name='myterminaleditor',
    version='0.1.0',
    author='lihuiruo',
    author_email='lihuiruo@gmail.com',  # 본인의 이메일로 수정
    description='A custom web-based terminal and code editor module',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lihuiruo/myterminaleditor',
    packages=find_packages(),  # myterminaleditor 폴더 포함
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Python 버전
    install_requires=[
        'flask',  # 필요에 따라 Flask나 다른 웹 프레임워크 추가
        # 필요한 다른 패키지 추가
    ],
    entry_points={
        'console_scripts': [
            'myterminal = myterminaleditor.cli:main',  # 커맨드라인 진입점 (선택)
        ],
    },
)
