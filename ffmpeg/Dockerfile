FROM alpine:3.12
RUN apk add --no-cache ffmpeg v4l-utils

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ./run.sh