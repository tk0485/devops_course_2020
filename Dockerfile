FROM python
RUN apt update && \
    apt install ssh -y && \
    apt install default-jre -y && \
    apt install default-jdk -y && \
    apt-get -qq clean    \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -ms /bin/bash jenkins
RUN systemctl enable ssh
RUN echo 'jenkins:jenkins' | chpasswd
ADD ./code /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 22
CMD /etc/init.d/ssh start ; python webapp.py
