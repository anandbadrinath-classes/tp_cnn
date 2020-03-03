FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.6 \
    python3-pip \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-dev

WORKDIR /tp_cnn
ADD . /tp_cnn
RUN pip3 install --upgrade pip
RUN pip3 install setuptools
RUN pip3 install -r requirements-gpu.txt

CMD bash