# Yang Yang Dance Simulator
GDSC 2024 - AI Team Project

## Introduciton

## Dataset
### Training Data
We first extract the raw video into 2 domains:
- domainA: the pose skeleton of the dancer
- domainB: the dancer's image frame with background removed

![training data](src/training_pose2img.gif)

### Testing Data
For preparing testing data, we only need to extract the pose skeleton(domainA) of the dancer from the video.
![testing data](src/magnetic_dance2pose.gif)

## Model Structure and Pipeline
We utilize Pix2Pix GAN model to train the data and generate the target domain from the source domain.
### Training Phase
![Training Pipeline](workflow/training-phase.png)
### Testing Phase
![Testing Pipeline](workflow/testing-phase.png)

## Results
- Dance → Pose → Fish(Author: Chen-Yang Yu)
![generated video](src/magnetic_dance2pose2fish.gif)

## Contributors
- Chen-Yang Yu