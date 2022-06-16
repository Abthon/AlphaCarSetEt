from flask import Blueprint
from AlphaCarsET import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)