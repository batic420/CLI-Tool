#!/usr/bin/env python3

import typer
import os
from commands import git, docker, npm

rt = typer.Typer()

rt.add_typer(git.repo, name="repo")  
rt.add_typer(docker.cn, name="cn") 
rt.add_typer(npm.pg, name="pg")

@rt.command()
def validate():
    """Testing the install of the CLI"""

    typer.secho("CLI working as expected!", fg='green', bold=True)

@rt.command()
def deploy(
        branch: str = typer.Option(
        "main",
        help="Branch to clone from",
    ),
    working_dir: str = typer.Option(
        os.getcwd(),
        help="directory to clone the repo to"
    ),
    compose_file = typer.Option("../../docker-compose.yml", help="location + name of the YAML file used to create the container/s")
):
    """Deploy the root-kit project"""

    try:
        typer.secho("Cloning the repo to working directory...")
        git.clone(branch, working_dir)
        typer.secho("Repo cloned successfully!", fg='green')

        typer.secho("Installing npm packages...")
        npm.install(working_dir)
        typer.secho("Npm packages installed successfully!", fg='green')

        typer.secho("Creating the container for database...")
        docker.create(compose_file)
        typer.secho("Container created successfully!", fg='green')

        typer.secho("Deployment completed successfully!",fg='bright_green' , bold=True)
    except Exception as e:
        typer.secho(f"\n❌ Deployment failed: {e}", fg="red", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    rt()