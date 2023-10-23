FROM node:18-alpine AS builder

COPY . /app

RUN cd /app && npm install && \
	npm run build 

FROM node:18-alpine

COPY --from=builder /app/build /app/build
COPY --from=builder /app/package.json /app/

RUN cd /app && \ 
	npm install --omit=dev

WORKDIR /app

EXPOSE 3000

CMD ["node", "build/index.js"]