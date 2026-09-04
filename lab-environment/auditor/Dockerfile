FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm-256color

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    iproute2 \
    iputils-ping \
    dnsutils \
    net-tools \
    curl \
    wget \
    tcpdump \
    tshark \
    lsof \
    strace \
    ltrace \
    procps \
    htop \
    mc \
    git \
    vim \
    nano \
    jq \
    python3 \
    python3-pip \
    bsdmainutils \
    ca-certificates \
    file \
    binutils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

CMD ["/bin/bash"]
