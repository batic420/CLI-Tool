import typer
import subprocess
import os

pg = typer.Typer()

@pg.command()
def install(
    workingDir: str = typer.Argument(os.getcwd(), help="directory to install the packages to")
):
    """Install all used packages for root-kit"""

    try:
        result = subprocess.run(
            ["npm", "ci"],
            cwd=workingDir
        )

        print("Packages installed!", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred!", e.stderr)