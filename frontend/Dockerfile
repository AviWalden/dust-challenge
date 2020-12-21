FROM node:latest

RUN mkdir -p /home/frontend
WORKDIR /home/frontend

COPY package*.json /home/frontend/

RUN npm install

CMD ["npm", "start"]
