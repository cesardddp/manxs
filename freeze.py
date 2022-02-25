from flask_frozen import Freezer
from app import app

freezer = Freezer(app, with_no_argument_rules=False, log_url_for=False)

if __name__ == "__main__":
    freezer.freeze()
