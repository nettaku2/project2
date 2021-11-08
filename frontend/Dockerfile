FROM node:14.18.1-alpine

RUN addgroup app && adduser -S -G app app
USER app

WORKDIR /app
COPY package.json .
COPY yarn.lock .
RUN ["yarn", "install"]
COPY . .

EXPOSE 3000

ENV CHOKIDAR_USEPOLLING=true

# CMD ["yarn", "start"]