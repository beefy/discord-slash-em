from setuptools import setup, find_namespace_packages


def parse_requirements(filename: str) -> list:
    """
    Read from pip requirements from txt file.
    """
    with open(filename) as f:
        return [
            r.strip() for r in f.read().splitlines()
            if r.strip() and not r.startswith("#")
        ]


setup(
    name="discord-slashem",
    version="0.0.1",
    description="",
    url="",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    install_requires=parse_requirements("requirements.txt"),
    include_package_data=True,
    zip_safe=False
)
