FROM node:15.2.0-alpine

WORKDIR /app

RUN apk update && apk add git && npm install -g vue-cli

EXPOSE 80

CMD \
  npm install && \
  npm run serve