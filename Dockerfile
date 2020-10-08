FROM python:3.8-slim-buster
LABEL maintainer="Franc Rodriguez - franc@tecob.com"
RUN apt update  && apt install -y firefox-esr \
 && apt-get clean autoclean \
 && apt-get autoremove --yes \
 && rm -rf /var/lib/{apt,dpkg,cache,log}/ 
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
ADD . /resetPower
ENV PATH $PATH:/resetPower
CMD [ "python", "/resetPower/resetPowerCounter.py" ]

