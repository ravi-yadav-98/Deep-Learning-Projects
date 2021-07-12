# import the necessary packages
from keras.callbacks import BaseLogger
import matplotlib.pyplot as plt
import numpy as np
import json
import os

class TrainingMonitor(BaseLogger):
	def __init__(self, figPath, jsonPath=None, startAt=0):
		# store the output path for the figure, the path to the JSON
		# serialized file, and the starting epoch
		super(TrainingMonitor, self).__init__()
		self.figPath = figPath
		self.jsonPath = jsonPath
		self.startAt = startAt

	def on_train_begin(self, logs={}):
		# initialize the history dictionary
		self.H = {}

		# if the JSON history path exists, load the training history
		if self.jsonPath is not None:
			if os.path.exists(self.jsonPath):
				self.H = json.loads(open(self.jsonPath).read())

				# check to see if a starting epoch was supplied
				if self.startAt > 0:
					# loop over the entries in the history log and
					# trim any entries that are past the starting
					# epoch
					for k in self.H.keys():
						self.H[k] = self.H[k][:self.startAt]

	def on_epoch_end(self, epoch, logs={}):
		# loop over the logs and update the loss, accuracy, etc.
		# for the entire training process
		for (k, v) in logs.items():
			l = self.H.get(k, [])
			l.append(v)
			self.H[k] = l

		# check to see if the training history should be serialized
		# to file
		if self.jsonPath is not None:
			f = open(self.jsonPath, "w")
			f.write(json.dumps(self.H))
			f.close()

		# ensure at least two epochs have passed before plotting
		# (epoch starts at zero)
		if len(self.H["loss"]) > 1:
			# plot the training loss and accuracy
			N = np.arange(0, len(self.H["loss"]))
			plt.style.use("ggplot")
			# plt.figure()
			# plt.plot(N, self.H["loss"], label="train_loss")
			# plt.plot(N, self.H["val_loss"], label="val_loss")
			# plt.subplot(1,2,2)
			# plt.plot(N, self.H["acc"], label="train_acc")
			# plt.plot(N, self.H["val_acc"], label="val_acc")
			# plt.title("Training Loss and Accuracy [Epoch {}]".format(
			# 	len(self.H["loss"])))
			# plt.xlabel("Epoch #")
			# plt.ylabel("Loss/Accuracy")
			# plt.legend()
			f = plt.figure(figsize=(20,14))
			ax = f.add_subplot(121)
			ax2 = f.add_subplot(122)
			ax.plot(N, self.H["loss"], label="train_loss")
			ax.plot(N, self.H["val_loss"], label="val_loss")
			#ax.grid()
			ax.set_title("Training Loss [Epoch {}]".format(len(self.H["loss"])))
			ax.legend(['train_loss','val_loss'])
			ax.set_ylabel("Train/val loss")
			ax.set_xlabel("Epoch #")
			ax2.plot(N, self.H["accuracy"], label="train_accuracy")
			ax2.plot(N, self.H["val_accuracy"], label="val_accuracy")
			#ax2.grid()
			ax2.set_title("Training Accuracy [Epoch {}]".format(len(self.H["loss"])))
			ax2.legend(['train_acc','val_acc'])
			ax2.set_xlabel("Epoch #")
			ax2.set_ylabel("train/val accuracy")
			# save the figure
			#plt.grid()
			plt.savefig(self.figPath)
			plt.close()