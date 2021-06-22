from augly.image import aug_np_wrapper, overlay_emoji
import augly.image as imaugs
import numpy as np
import augly.utils as utils
import cv2
import os
from PIL import Image
def emoji_overlay(img_path):
    '''
    modify imgae by over lapping emoji on image
    
    '''
    np_image = cv2.imread(img_path)
    # pass in function arguments as kwargs
    np_aug_img = aug_np_wrapper(np_image, overlay_emoji, **{'opacity': 0.5, 'y_pos': 0.45})

    cv2.imshow("img", np_aug_img)
    cv2.waitKey(0)

# Get input image, scale it down to avoid taking up the whole screen
input_img_path = "img1.jpg"
input_img = Image.open(input_img_path)

aug_perspective = imaugs.PerspectiveTransform(sigma=20.0)
camera_pil_perspective = aug_perspective(input_img)
camera_pil_perspective.show()

aug_aspect = imaugs.RandomAspectRatio()
camera_pil_aspect = aug_aspect(input_img)
camera_pil_aspect.show()


aug_saturation = imaugs.Saturation(factor=5.0)
camera_pil_sat = aug_saturation(input_img)
camera_pil_sat.show()


camera_pil_overlay_stripes = imaugs.overlay_stripes(input_img, line_type='dashed', line_opacity=0.5, line_color=(120, 0, 200), line_angle=25.0)
camera_pil_overlay_stripes.show()


#if __name__ ==  "__main__":
    #emoji_overlay("img2.jpg")