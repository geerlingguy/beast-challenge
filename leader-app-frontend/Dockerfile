FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY yarn.lock ./
COPY . ./

RUN npm install
RUN yarn run build

CMD ["yarn", "start"]
