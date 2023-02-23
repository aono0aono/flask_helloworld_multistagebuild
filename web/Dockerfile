FROM nginx:1.23-alpine

# set environment variables
ENV TZ=Asia/Tokyo

COPY ./nginx /etc/nginx/

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]&& tail -f /dev/null

