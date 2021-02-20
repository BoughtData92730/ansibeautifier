from setuptools import setup, find_packages

with open("README.md", "r") as markdown:
    long_description = markdown.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
]

setup(
    name="ansibeautifier",
    version="0.0.5",
    description="You can beautify your python command-line and GUI applications using colors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/BoughtData92730/ansibeautifier",
    author="Tarun the AnyLang Programmer",
    author_email="taruntheanylangprogrammer@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="",
    packages=find_packages(),
    install_requires=[""]
)
