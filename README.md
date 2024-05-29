# Yang Yang Dance Simulator
GDSC 2024 - AI Team Project

## Introduciton

## Pipepline

## Dataset
### Training Data
We first extract the raw video into 2 domains:
- domainA: the pose skeleton of the dancer
- domainB: the dancer's image frame with background removed
![training data](src/training_pose2img.gif)

### Testing Data
For preparing testing data, we only need to extract the pose skeleton(domainA) of the dancer from the video.
![testing data](src/magnetic_dance2pose.gif)

## Model
We use Pix2Pix GAN model to train the data. 
### Training
### Testing

## Results
- Dance → Pose → Fish(Author: Chen-Yang Yu)
![generated video](src/magnetic_dance2pose2fish.gif)

## Contributors
- Chen-Yang Yu