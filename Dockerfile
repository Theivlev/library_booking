FROM python:3.9

RUN mkdir /library_booking     

WORKDIR /library_booking   

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .


RUN chmod a+x /library_booking/docker/*.sh

# RUN alembic upgrade head

# CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]