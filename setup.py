from setuptools import setup, find_packages

setup(
    name="root-kit",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "typer",
        "gitpython",
        "python-dotenv",
        "docker",
        "subprocess",
        "os",
        "shutil",
        "time"
    ],
    entry_points={
        "console_scripts": [
            "root-kit=src.cli:app"
        ]
    }
)