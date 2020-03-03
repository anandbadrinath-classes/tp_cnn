xhost +
docker run -it --rm \
  --name=tp_cnn \
  -v $(pwd):/tp_cnn \
  -e "DISPLAY=$DISPLAY" \
  -e QT_X11_NO_MITSHM=1 \
  -v /tmp/.X11-unix/:/tmp/.X11-unix \
  --gpus all \
  -e LD_LIBRARY_PATH=/usr/local/cuda/lib64 \
  -u=1000 \
  <nom>_tp_cnn bash
