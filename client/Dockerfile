#Followed https://www.freecodecamp.org/news/how-to-dockerize-a-react-application/

FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

