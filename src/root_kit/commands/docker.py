import typer
import docker
import subprocess
import uuid

from dotenv import load_dotenv
from root_kit.utils.template import generate_template

load_dotenv()
client = docker.from_env()
cn = typer.Typer(help="Manage the underlying docker container for the root-kit mysql database")

# TODO:
# - Optimize code for commands inside a function

@cn.command()
def create(
    compose_file = typer.Option(
        None, 
        "--file", 
        "-f", 
        help="supply the name and location of a custom docker-compose file"
    ),
    random_key: str = typer.Option(
        uuid.uuid4().hex[:6].upper(),
        "--key",
        "-k",
        help="custom key for a unique service name per instance -> REMEMBER YOUR KEY!"
    ) 
):
    """Create a new root-kit container"""

    if compose_file:
        result = subprocess.run(
            ["docker", "compose", "-f", compose_file, "up", "-d"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Container created with custom YAML has been created", result.stdout)
    else:
        # 
        # TODO:
        # - debug deployment to always use custom yaml and not template
        #
        unique_yaml = "../../compose-" + random_key + ".yaml"
        generate_template( custom_key=random_key, file_path=unique_yaml)
        result = subprocess.run(
            ["docker", "compose", "up", "-f", unique_yaml, "-d"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Container created!", result.stdout)
        print(f"Your custom id for the service: msyql-{random_key}")



@cn.command()
def delete(
    service_name: str = typer.Argument("mysql", help="name of the service to delete")
):
    """Delete a root-kit container"""

    try:
        result = subprocess.run(
            ["docker", "compose", "down", service_name],
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
    service_name: str = typer.Argument("mysql", help="name of the service to start")
):
    """Start a root-kit container"""

    try:
        result = subprocess.run(
            ["docker", "compose", "start", service_name],
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
    service_name: str = typer.Argument("mysql", help="name of the service to stop")
):
    """Stop a root-kit container"""

    try:
        result = subprocess.run(
            ["docker", "compose", "stop", service_name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Container stopped!", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred!", e.stderr)