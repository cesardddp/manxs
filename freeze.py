from flask_frozen import Freezer
from app import app

freezer = Freezer(app)
if __name__ == "__main__":
    freezer.run(debug=True)
    #freezer.freeze(debug=True)
