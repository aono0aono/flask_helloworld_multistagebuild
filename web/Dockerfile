FROM nginx:1.21.3

# set environment variables
ENV APP_HOME=/var/www/src \
    TZ=Asia/Tokyo

# create source directory
RUN mkdir -p $APP_HOME

# set work directory
WORKDIR $APP_HOME

COPY ./nginx /etc/nginx/

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]&& tail -f /dev/null

