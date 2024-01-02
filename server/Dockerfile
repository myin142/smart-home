FROM python:3.11-slim

COPY ./requirements.txt /var/www/
COPY ./app.py /var/www/
WORKDIR /var/www

RUN apt-get update && apt-get install -y python3-dev gcc libc-dev
RUN pip install -r /var/www/requirements.txt
EXPOSE 5000

CMD ["flask","run"]

