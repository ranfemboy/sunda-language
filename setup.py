from setuptools import setup, find_packages

setup(
    name="sundapy",
    version="0.1.0",
    description="Basa pamrograman dumasar Python nganggo kecap Basa Sunda",
    author="Anjeun",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "sunda=sundapy.cli:main",
        ],
    },
)
