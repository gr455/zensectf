FROM php:7.2-apache

COPY php /var/www/html
RUN mkdir -p /home/wow/y0u/4re/almost/th3Re
COPY flag.txt /home/wow/y0u/4re/almost/th3Re/flag.txt

RUN unlink /var/log/apache2/access.log
RUN chown -R root /home
RUN chown -R root /var/www


RUN chmod -R 755 /home
RUN chmod -R 755 /var/www/