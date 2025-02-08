#!/usr/bin/env python3

from dotenv import load_dotenv
import typer
import os
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
import shutil

load_dotenv()
app = typer.Typer()

@app.command()
def clone(
    branch: str = typer.Option(
        "main",
        help="Branch to pull from",
    )
):
    """Pull the latest changes from the root-kit repo"""

    try:
        typer.echo(f"Cloning {os.getenv("REMOTE_URL")} on branch {branch}...")

        if os.path.exists(os.getenv("LOCAL_DIR")):
            typer.echo(f"Directory {os.getenv("LOCAL_DIR")} already exists. Deleting...")
            shutil.rmtree(os.getenv("LOCAL_DIR"))

        Repo.clone_from(
            os.getenv("REMOTE_URL"), os.getenv("LOCAL_DIR"), branch=branch
        )

        typer.echo(f"Cloning to {os.getenv("LOCAL_DIR")} complete!")
    
    except InvalidGitRepositoryError as e:
        typer.echo(f"Invalid git repository: {e}")
    except GitCommandError as e:
        typer.echo(f"Git command error: {e}")
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}")
        

if __name__ == "__main__":
    app()