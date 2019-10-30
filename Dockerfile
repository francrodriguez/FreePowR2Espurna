FROM ubuntu:18.04
LABEL maintainer="Franc Rodriguez - franc@tecob.com"
RUN apt update
RUN apt install -qy python3 whois python3-pip firefox
COPY requirements.txt /tmp/
RUN pip3 install --requirement /tmp/requirements.txt
ADD . /resetPower
ENV PATH $PATH:/resetPower
CMD [ "python3", "/resetPower/storedata.py" ]
CMD [ "python3", "/resetPower/resetPowerCounter.py" ]

