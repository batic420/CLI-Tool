import typer
from dotenv import load_dotenv
import docker
import subprocess

load_dotenv()
client = docker.from_env()
cn = typer.Typer()

# TODO:
# - Optimize code for commands inside a function

@cn.command()
def create(
    composeFile = typer.Argument("../../docker-compose.yml", help="location + name of the YAML file used to create the container/s")
):
    """Create a new root-kit container"""

    try:
        result = subprocess.run(
            ["docker", "compose", "-f", composeFile, "up", "-d"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("Container created!", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred!", e.stderr)

@cn.command()
def delete(
    serviceName: str = typer.Argument("mysql", help="name of the service to delete")
):
    """Delete a root-kit container"""

    try:
        result = subprocess.run(
            ["docker", "compose", "down", serviceName],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Container deleted!", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred!", e.stderr)

@cn.command()
def start(
    serviceName: str = typer.Argument("mysql", help="name of the service to start")
):
    """Start a root-kit container"""

    try:
        result = subprocess.run(
            ["docker", "compose", "start", serviceName],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Container started!", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred!", e.stderr)

@cn.command()
def stop(
    serviceName: str = typer.Argument("mysql", help="name of the service to stop")
):
    """Stop a root-kit container"""

    try:
        result = subprocess.run(
            ["docker", "compose", "stop", serviceName],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Container stopped!", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred!", e.stderr)