FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
      letsencrypt \
      ca-certificates

WORKDIR /root
COPY docker-entrypoint.py docker-entrypoint.py
RUN chmod +x docker-entrypoint.py
ENTRYPOINT ["python","/root/docker-entrypoint.py"]
