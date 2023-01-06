# YOLO ObjectDetectionAPI in Docker
API endpoints to run object detection using YOLOv3. The user can send an image to the API endpoint and the detected results will be received as response.


## Goal
The goal of this project is to test and demonstrate the AI-Serving concept, by deploying the Object Detection model as a docker image, so that any application can be interacted with this docker by making a POST request at the API endpoint with an image data and can receive the detection results as the response. 

Object Detection API once deployed in a dockerfile shall receive the data input over a JSON Query and after inference generate the output and make it available in a JSON format.

The API has been developed in FastAPI and made available as docker. 

## Model
For the initial implementation a YOLOv3 model trainied on COCO dataset has been used in this configuration. This can detect the 80 different classes of objects as given in the COCO. The model weights can be downloaded from "https://pjreddie.com/media/files/yolov3.weights"


## Build the Docker
During the docker build, the YOLOv3 weights have been downloaded and integrated to the image. 

Build and tag the docker image using:
`docker build -t od-api .`

After sucessfull building, run the docker using:
`docker run -ti --rm -p 5000:5000 od-api`

## API Endpoints

#### Endpoint `/`

Gives a health message in JSON format as follows
` "message":"Welcome to object detection API" `

#### Endpoint `/detect/`

This return a JSON file in the format `"classes":ordered_classes, "counts":object_count` , where the  `ordered_classes` is a list of detected objects in the given image and the `object_count` gives the total count of each classes.
This endpoint can be custom configured to get the `confidence scores` or `x,y,w,h` cordinates of each bounding box. 

This can even exteneded to send an imagedata including all the detection results as response.

## Usage
After deploying the docker locally, one can make a POST request using the `curl` command:

`curl -X POST -F "file=@/path/to/image.jpg" http://localhost:5000/detect/` and gives the JSON data in the above mentioned format as response.


## Notes
The latest OpenCV version 4.7 is having bugs and therefore the OpenCV version 4.6 has been used for the inference 

## TODO

- Extend the detect endpoint to send detected image and cordinates also. 
- Update the notebooks folder with the model generating notebook for a custom dataset
