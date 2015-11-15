from setuptools import setup

setup(
    name='Pinyin Coach',
    version='1.0',
    py_modules=['pinyin_coach'],
    include_package_data=True,
    install_requires=[
        'click',
        'python-vlc'
    ],
    entry_points='''
        [console_scripts]
        coach=coach:cli
    ''',
)
