import typer
from dotenv import load_dotenv
import docker
import subprocess

load_dotenv()
client = docker.from_env()
cn = typer.Typer()

@cn.command()
def create(
    composeFile = "docker-compose.yml",
    command = "up -d"
):
    """Create a new root-kit container"""

    try:
        result = subprocess.run(
            ["docker compose", "-f", composeFile, command ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Container created!", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred!", e.stderr)
