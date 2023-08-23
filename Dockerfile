FROM ubuntu:latest

RUN apt update && apt install -y ca-certificates python3 python3-pip
COPY full-ca.pem /etc/pki/ca-trust/source/anchors/
RUN update-ca-certificates

CMD tail --follow /dev/null