### [AugLy Link:](https://ai.facebook.com/blog/augly-a-new-data-augmentation-library-to-help-build-more-robust-ai-models/)
- By **Facebook AI Research**
- A new data augmentation library to help build more robust AI models
- AugLy, a new Python library that will help AI researchers use data augmentations to evaluate and improve the robustness of their machine learning models.
- Augmentations can include a wide variety of modifications to a piece of content, ranging from recropping a photo to changing the pitch of a voice recording
- It’s important to build AI that isn’t fooled by these changes. 
- Can be used for audio, image, video, and texts
- offers more than 100 data augmentations
- **focused on things that real people on the Internet do to images and videos on platforms like Facebook and Instagram.**
- For example, this includes overlaying text, emoji, & screenshot transforms.

### **Why Augumentation:**
- Data augmentations are vital to ensure robustness of AI models. If we can teach our models to be robust to perturbations of unimportant attributes of data,
 models will learn to focus on the important attributes of data for a particular use case.
- Training models to detect near-duplicates using AugLy means we may be able to proactively prevent users from uploading content that is known to be infringing.
- example simSearchNet ----find duplicates of images
- Many of the augmentations in AugLy are informed by ways we have seen people transform content to try to evade our automatic systems.
- Usefull in case of :
   - Hatefull meme challenge
   - Deepfake

### Install 
- pip install augly

- [Github Link](https://github.com/facebookresearch/AugLy?fbclid=IwAR3Kk57L6JeQefSweFYdAOQWLonJ7ElLCAlMeAxcNAf0rfY3G9R_GSfAWNA)
