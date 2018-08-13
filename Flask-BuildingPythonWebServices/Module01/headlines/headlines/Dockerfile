FROM ubuntu:18.04 as OS
RUN apt update && apt install -y apache2 python3 python3-pip libapache2-mod-wsgi-py3
RUN a2dissite 000-default.conf
COPY ./docker/wsgi.conf /etc/apache2/sites-available/wsgi.conf
RUN a2ensite wsgi.conf
RUN service apache2 stop

FROM OS as PIP
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

FROM PIP
CMD ["apache2ctl", "-D", "FOREGROUND"]