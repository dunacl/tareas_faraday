from flask import Flask
from flask_autoindex import AutoIndex
import pathlib

app = Flask(__name__)
parent_path = pathlib.Path(__file__).parent.absolute()

app = Flask(__name__)
AutoIndex(app, browse_root=parent_path)

if __name__ == "__main__":
  app.run('0.0.0.0', 80)