docker build . -t rew-plotter
#TODO: RUN PARALLEL (TMUX?)
docker run -it rew-plotter
$CONTAINER_NAME = 
#TODO: RUN PARALLEL
docker exec -it $CONTAINER_NAME /bin/bash
docker cp $CONTAINER_NAME:/home/0.png ./0.png
feh 0.png
