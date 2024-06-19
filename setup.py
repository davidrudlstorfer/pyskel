"""Setup project."""

from setuptools import find_packages, setup


def read_requirements(req_name: str):
    """Read requirements from file.

    Args:
        req_name (str): Name of requirements file

    Returns:
        List of requirements
    """
    with open(req_name, "r") as file:
        return [
            line.strip()
            for line in file
            if line.strip() and not line.strip().startswith("#")
        ]


if __name__ == "__main__":
    setup(
        name="PySkel",
        version=1.0,
        author="David Rudlstorfer",
        packages=find_packages(),
        python_requires="==3.12.*",
        classifiers=["Programming Language :: Python :: 3.12"],
        install_requires=read_requirements("requirements.txt"),
    )
