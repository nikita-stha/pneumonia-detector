from flask.cli import FlaskGroup

from project.main import app

cli = FlaskGroup(app)


@cli.command("start_server")
def create_db():
    print("Starting web server")


if __name__ == "__main__":
    cli()
