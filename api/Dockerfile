FROM ubuntu:latest

WORKDIR /home/api

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev build-essential

RUN mkdir -p /home/api
WORKDIR /home/api

COPY requirements.txt /home/api
RUN python3 -m pip install -r /home/api/requirements.txt

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
