import typer
from dotenv import load_dotenv
import docker
import subprocess

load_dotenv()
client = docker.from_env()
cn = typer.Typer()

@cn.command()
def create(
    composeFile = "../../docker-compose.yml",
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
        print(f"Container created!", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred!", e.stderr)

@cn.command()
def delete(
    serviceName: str = "mysql"
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
    serviceName: str = "mysql"
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
    serviceName: str = "mysql"
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