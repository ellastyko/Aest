FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3.9 
RUN apt-get install -y git curl
RUN apt-get -y install python3-pip

WORKDIR /server

ADD server .
COPY src db emails ./
ADD requirements.txt .

RUN pip3 install -r requirements.txt 

CMD ["python3.9", "server"]





# docker build -t python-imdb .
# docker run -t -i python-imdb