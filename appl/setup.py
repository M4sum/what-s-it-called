import sys
from app import app

if __name__ == "__main__":
    app.config['NEURAL_NET_PATH'] = sys.argv[1]
    app.run()
