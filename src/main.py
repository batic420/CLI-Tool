#!/usr/bin/env python3

import typer
import os

app = typer.Typer()

@app.command()
def greet(name: str):
    print(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Mr. {name}")
    else:
        print(f"Bye {name}")

@app.command()
def mdir(directory: str="default"):
    print(os.getcwd())

if __name__ == "__main__":
    app()