from project.app import app
from project.views import *

if __name__ == "__main__":
    app.run(debug=True, port=8002)
