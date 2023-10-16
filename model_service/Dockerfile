FROM python:3.7

WORKDIR /app

ADD requirements.txt requirements.txt
ADD ./model ./model
ADD app.py app.py

RUN pip install -r requirements.txt

EXPOSE 8090

CMD [ "gunicorn", "--bind", "0.0.0.0:8090", "app:app"]