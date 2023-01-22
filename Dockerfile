FROM python

EXPOSE 5000
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN pip3 install --upgrade pip
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt
RUN mkdir /files
RUN mkdir /images
COPY . /code/
WORKDIR /code




CMD ["./start.sh"]
