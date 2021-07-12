 
### Kaggle Facial Expression Recognition Challenge

 - **Related paper:  Challenges in Representation Learning: A report on three machine learning contests**
 - Link of paper: https://arxiv.org/pdf/1307.0414.pdf

- **Goal: Given a face images identify the facial expression of person 
          [angry, disgust, fear, happy, sad, surprise, , neutral]**
- Datasets: FER13 dataset
- Image size      :   48x48
- Total images  :   28709
- Dataset link    :    http://pyimg.co/a2soy


Training  parameter:

	1. Activation  function: "elu" (better accuracy)
	2. Learning rates: 1e-3(for 40 epoch), 1e-4(for 20 epoch), 1e-5(for 15 epoch)
	3. Total Epochs =  75
	4. Weight Initializer : MSRA/HE et.al (Better for VGG family network)


### steps:
1. Build datasets:
python build_dataset.py

2. Train model
> python train_recognizer.py --checkpoints checkpoints
or
<br> > python train_recognizer.py --checkpoints checkpoints --model checkpoints/epoch_40.hdf5 --start-epoch 40

3. Test accuracy:
 > python test_recognizer.py --model checkpoints/epoch_75.hdf5

4. Test : real time using webcam
 > python emotion_detector.py --cascade haarcascade_frontalface_default.xml --model checkpoints/epoch_75.hdf5

5. Test: using videos

 > python emotion_detector.py --cascade haarcascade_frontalface_default.xml  --model checkpoints/epoch_75.hdf5 --video sample.mp4

