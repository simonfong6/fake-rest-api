DIRECTORY_NAME="template-python-flask"
IMAGE_NAME="domain.com.image"
CONTAINER_NAME="domain.com..container"
PORT="8000"

docker container run \
    -it \
    --rm \
    --name $IMAGE_NAME \
    --user vscode \
    --mount type=bind,source=/home/ubuntu/Projects/$DIRECTORY_NAME,target=/workspace/$DIRECTORY_NAME \
    --workdir /workspace/$DIRECTORY_NAME \
    --publish $PORT:$PORT \
    $IMAGE_NAME /bin/bash && pip3 install -r requirements.txt
