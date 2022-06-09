from setuptools import find_packages, setup

setup(
    name='python',
    version='1.0.0',
    packages=find_packages(),   # パッケージディレクトリを自動で見つけ出す
    include_package_data=True,  # その他のファイルを含めるかの設定.別途MANIFEST.inを作成する
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)