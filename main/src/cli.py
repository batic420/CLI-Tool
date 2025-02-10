#!/usr/bin/env python3

import typer
from src.commands import git

app = typer.Typer()
app.add_typer(git.app, name="git")        


if __name__ == "__main__":
    app()