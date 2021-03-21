FROM python:3.6
MAINTAINER JeanneBM

COPY . /PyCalculator
WORKDIR /PyCalculator

RUN pip install -r requirements.txt

CMD ["app.py"]

EXPOSE 5000/tcp
