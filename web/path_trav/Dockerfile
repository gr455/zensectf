FROM php:7.2-apache

COPY php /var/www/html
RUN mkdir -p /var/www/html/flag
COPY flag.txt /var/www/html/flag/flag.txt

RUN unlink /var/log/apache2/access.log

RUN chown -R root /home
RUN chown -R root /var/www


RUN chmod -R 755 /home
RUN chmod -R 755 /var/www/
