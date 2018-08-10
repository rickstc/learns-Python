FROM ubuntu:18.04 as OS
RUN apt update && apt install -y apache2 python python-pip libapache2-mod-wsgi
RUN a2dissite 000-default.conf
COPY ./docker/wsgi.conf /etc/apache2/sites-available/wsgi.conf
RUN a2ensite wsgi.conf
RUN service apache2 stop

FROM OS as PIP
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

FROM PIP
CMD ["apache2ctl", "-D", "FOREGROUND"]