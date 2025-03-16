from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements from requirements.txt,
    while ensuring `-e .` is NOT included in install_requires.
    """
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        # Remove empty spaces and `-e .`
        requirements = [
            req.strip()
            for req in requirements
            if req.strip() and not req.startswith("-e")
        ]

    return requirements  #


setup(
    name="my_project",  #
    author="Mpampis1312",
    author_email="xarisban@gmail.com",
    packages=find_packages(where="src"),  # ✅ Ensure it finds your package
    package_dir={"": "src"},  # ✅ Defines `src/` as the package directory
    install_requires=get_requirements(
        "requirements.txt"
    ),  # ✅ Now correctly reads the file without `-e .`
)
