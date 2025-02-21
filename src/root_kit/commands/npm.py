import typer
import subprocess
import os

pg = typer.Typer(help="Install the required npm packages for root-kit manually with a single command")

@pg.command()
def install(
    working_dir: str = typer.Option(os.getcwd(), help="directory to install the packages to")
):
    """Install all used packages for root-kit"""

    try:
        result = subprocess.run(
            ["npm", "ci"],
            cwd=working_dir
        )

        print("Packages installed!", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred!", e.stderr)