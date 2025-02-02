#!/usr/bin/env python3

import typer

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

if __name__ == "__main__":
    app()