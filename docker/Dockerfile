FROM ubuntu:18.04

MAINTAINER kashiraWork


RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install build-essential
RUN apt-get -y install git python3 wget python3-pip

RUN pip3 install jinja2

RUN git clone https://github.com/kashiraWork/wsgi_dev

EXPOSE 80

WORKDIR wsgi_dev
CMD ["python3", "multi_response_wsgi_server.py", "jinja2_wsgi_app_by_function:application"]
#CMD python3 multi_response_wsgi_server.py jinja2_wsgi_app_by_function:application
