FROM python:3.9.23

WORKDIR /seed

COPY seed/* .
RUN pip install -r requirements.txt

CMD ["./seed.sh"]
