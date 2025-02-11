#!/usr/bin/env python3

import typer
from commands.git import repo

app = typer.Typer()
app.add_typer(repo, name="repo")        


if __name__ == "__main__":
    app()