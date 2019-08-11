import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="napp",
    version="1.0.0",
    url="https://github.com/neoricalex/napp",
    license="BSD",
    maintainer="NEORICALEX team",
    maintainer_email="neo.webmaster.2@gmail.com",
    description="Um aplicativo em Python",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask", "python-dotenv"],
    extras_require={"test": ["pytest", "coverage"]},
)
