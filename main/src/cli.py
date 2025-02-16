#!/usr/bin/env python3

import typer
from commands.git import repo
from commands.docker import cn
from commands.npm import pg

app = typer.Typer()
app.add_typer(repo, name="repo")  
app.add_typer(cn, name="cn") 
app.add_typer(pg, name="pg")     


if __name__ == "__main__":
    app()