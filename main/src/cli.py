#!/usr/bin/env python3

from dotenv import load_dotenv
import typer
import os

load_dotenv()
app = typer.Typer()

@app.command()
def greet():
    test = os.getenv("TEST")
    print(f"Hello ${test}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Mr. {name}")
    else:
        print(f"Bye {name}")

@app.command()
def mdir(directory: str="default"):
    print(os.getcwd())


@app.command()
def locate():
    print(os.getcwd())

if __name__ == "__main__":
    app()