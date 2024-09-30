from flask import Flask
from routes import init_routes  # Import init_routes from the routes module

app = Flask(__name__)

# Initialize the routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)

import sys
print(sys.path)
