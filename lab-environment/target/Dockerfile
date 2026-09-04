FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    iproute2 \
    iputils-ping \
    net-tools \
    curl \
    python3 \
    openssh-server \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash operator && \
    echo "operator:operator123" | chpasswd && \
    useradd -m -s /bin/bash auditor && \
    echo "auditor:auditor123" | chpasswd

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 22 80

ENTRYPOINT ["/entrypoint.sh"]
