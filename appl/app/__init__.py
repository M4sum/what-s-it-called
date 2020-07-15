import os
from flask import Flask

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

from app import views

app.run(host='0.0.0.0', port=port, debug=True)

