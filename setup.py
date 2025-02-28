from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-package",
    version="0.0.1",
    author="Daelton",
    author_email="danben84@gmail.com",
    description="A package to process images",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbengp/dio-pacote-processamento-imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)