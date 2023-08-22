FROM debian:bullseye
RUN apt update && apt install -y python3 python3-pip
CMD tail --follow /dev/null
