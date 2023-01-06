# ObjectDetectionAPI
API to perform Object Detection on Image data

## Goal
The Object Detection API once deployed in a dockerfile shall receive the data input over a JSON Query and after inference generate the output and make it available in a JSON format.



## Model
The model used here is YOLOv3 trained on COCO dataset

## Build
Build the docker using:
`docker build -t od-api .`

Run the docker:
`docker run -ti --rm -p 5000:5000 od-api`


## TODO

- Update the notebooks folder with the model generating notebook for a custom dataset
- update the requirements.txt file