from flask.cli import FlaskGroup

import project


cli = FlaskGroup(project)


@cli.command("start_server")
def create_db():
    print("Starting web server")


if __name__ == "__main__":
    cli()
