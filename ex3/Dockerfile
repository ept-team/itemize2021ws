# sudo docker build -t ex3 .
# sudo docker run -d -p 8886:8886 --rm -it ex3

FROM ubuntu:20.04

RUN apt-get update

RUN useradd -d /home/edc/ -m -p edc -s /bin/bash edc
RUN echo "edc:edc" | chpasswd

WORKDIR /home/edc

COPY ynetd .
COPY flag.txt /opt/flag
COPY ex3 .

RUN chown -R root:root /home/edc
RUN chmod  -R a+rx /home/edc
USER edc
CMD ./ynetd -p 8886 ./ex3
