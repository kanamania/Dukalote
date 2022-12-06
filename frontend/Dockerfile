FROM node:19

WORKDIR /app/frontend

COPY package.json ./

COPY ./ ./

RUN npm install -g npm@9.1.2
RUN npm i npm-run-all
RUN npm i

EXPOSE 8000
CMD ["npm", "run", "dev"]
