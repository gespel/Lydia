FROM ubuntu:latest


RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    vim \
    net-tools \
    sudo
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo 'export VISIBLE=now' >> /etc/profile

EXPOSE 2222

ENTRYPOINT ["/usr/sbin/sshd", "-D"]