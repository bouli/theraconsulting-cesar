# Thera Consulting - Cesar Cardoso - Data Engineering


This project uses [Docker Compose](https://docs.docker.com/compose/) to manage the containers and [Prisma](https://www.prisma.io/) to manage the db.

## Usage
Initiate the DB instance with Docker Compose
```shell
docker compose up -d
```

Create the DB using Prisma
```shell
npx prisma db push
```

>You can use the legacy [prisma python client](https://pypi.org/project/prisma/) if you want.
>The only difference is that you don't need the "npx" command.

You can visualize/manipulate your data using the command
```shell
npx prisma studio
```
