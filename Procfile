web: export UPLOAD_FOLDER=app/uploads
web: export NEURAL_NET_MODEL_PATH=app/model/model_weights.h5
web: gunicorn app:setup
web: python setup.py $PORT
