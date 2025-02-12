from dotenv import load_dotenv
import typer
import os
import time
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
import shutil

load_dotenv()
repo = typer.Typer()

@repo.command()
def print():
    """Test the connection of the git python module"""

    typer.echo("Git module connected and accessible!")
    typer.echo(f"Remote URL: {os.getenv('REPO_PATH')}")

@repo.command()
def clone(
    branch: str = typer.Option(
        "main",
        help="Branch to clone from",
    )
):
    """Clone an initial copy of the root-kit repo for your project"""

    repo_path = os.getenv("REPO_PATH")
    local_dir = os.getenv("LOCAL_DIR")
    try:
        if not all([repo_path, local_dir]):
            raise ValueError("environment variables are missing!")

        if os.path.exists(local_dir):
            shutil.rmtree(local_dir)

        for _ in range(5):
            if not os.path.exists(local_dir):
                break
            time.sleep(0.1)
        else:
            raise RuntimeError(f"Failed to remove {local_dir}")
        
        Repo.clone_from(repo_path, local_dir, branch=branch)
    
    except InvalidGitRepositoryError as e:
        typer.echo(f"Invalid git repository: {e}")
    except GitCommandError as e:
        typer.echo(f"Git command error: {e}")
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}")

@repo.command()
def pull(
    branch: str = typer.Option(
        "main",
        help="Branch to pull from",
    )
):
    """Pull new changes from the root-kit repo"""

    try:
        repo = Repo(os.getenv("LOCAL_DIR"))
        origin = repo.remotes.origin

        curr_commit = repo.head.commit.hexsha
        new_pull = origin.pull(branch)[0]
        change = new_pull.commit.hexsha != curr_commit

        if change:
            commit_msg = repo.head.commit.message.strip()
            typer.echo(f"Changes pulled successfully: {commit_msg}")
        else:
            typer.echo("No changes to pull - repo is up-to-date!")

    except GitCommandError as e:
        typer.echo(f"Git command error: {e}")
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}")