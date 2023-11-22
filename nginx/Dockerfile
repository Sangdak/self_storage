FROM jwilder/nginx-proxy:1.3

RUN { \
      echo 'client_max_body_size 100M;'; \
    } > /etc/nginx/conf.d/custom.conf

COPY default_location /etc/nginx/vhost.d/default_location
