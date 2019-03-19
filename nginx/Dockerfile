FROM nginx

ADD nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /var/www/static/ \
    && mkdir -p /usr/local/nginx/ \
    && mkdir -p /usr/local/nginx/ssl

WORKDIR /var/www/static/
RUN chown -R nginx:nginx /var/www/static/
