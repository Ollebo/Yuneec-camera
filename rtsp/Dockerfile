FROM aler9/rtsp-simple-server AS rtsp
FROM alpine:3.12
RUN apk add --no-cache ffmpeg
COPY --from=rtsp /rtsp-simple-server /
COPY rtsp-simple-server.yml /rtsp-simple-server.yml
ENTRYPOINT [ "/rtsp-simple-server" ]