FROM python:3.11-slim

RUN apt-get update && apt-get install -y python3-dev gcc libc-dev

COPY ./requirements.txt /var/www/
RUN pip install -r /var/www/requirements.txt

COPY ./app.py /var/www/

WORKDIR /var/www
EXPOSE 5000

CMD ["flask","run", "--host", "0.0.0.0"]

