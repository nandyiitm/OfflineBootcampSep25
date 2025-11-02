# My MAD2 project

## Backend

To run `backend`:

```
cd backend # entering backend directory
python -m venv venv # creating virtual environment
source venv/bin/activate # activating virtual environment
pip install -r requirements.txt # installing dependencies
python app.py # running the backend application
```

## Frontend

Open another terminal and change directory to `frontend` and run:

```
cd frontend
npm install
npm run dev
```

## BackendJobs
make sure redis and mailhog is working in background

### Celery Worker
```
celery -A celery_app.celeryApp worker --loglevel=info
# for windows add --pool=solo
```
### Celery Beat
```
celery -A celery_app.celeryApp beat --loglevel=info
```