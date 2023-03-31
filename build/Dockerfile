FROM alpine:3.17.2

RUN apk add --no-cache \
              bash \
              bind-tools \
              iptables \
              ip6tables \
              openvpn \
              tzdata \
    && rm -f  /sbin/apk \
              /usr/bin/wget \
              /usr/sbin/sendmail \
              /usr/bin/nc

COPY . /usr/local/bin

ENV KILL_SWITCH=on

ENTRYPOINT [ "entry.sh" ]
