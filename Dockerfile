# use base python image with python 3.6.7
FROM python:3.6.7

# add requirements.txt to the image
ADD requirements.txt /app/requirements.txt

# set working directory to /app/
WORKDIR /app/

# install python dependencies
RUN pip3 install -r requirements.txt
#RUN sudo apt-get update
#RUN sudo apt-get install gdal-bin
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
RUN adduser --disabled-password --gecos '' myuser  

