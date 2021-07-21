#!/usr/bin/env python3


import roslib
import rospy
from std_msgs.msg import Header
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
import os
import time
import cv2
import numpy as np
import sys
import nanodet_ros.nanodet
from nanodet_ros.nanodet import my_nanodet

IMAGE_WIDTH = 1280
IMAGE_HEIGHT = 720


def image_callback_1(image):
    global ros_image, nanodet_model, nanodet_result_image
    ros_image = np.frombuffer(image.data, dtype=np.uint8).reshape(image.height, image.width, -1)[...,::-1]
    nanodet_result_image = nanodet_model.detect(ros_image)
    cv2.imshow('nanodet_result', nanodet_result_image)
    cv2.waitKey(5)
    publish_image(nanodet_result_image)


def publish_image(imgdata):
    image_temp = Image()
    header = Header(stamp=rospy.Time.now())
    header.frame_id = 'map'
    image_temp.height = IMAGE_HEIGHT
    image_temp.width = IMAGE_WIDTH
    image_temp.encoding = 'rgb8'
    image_temp.data = np.array(imgdata).tostring()
    #print(imgdata)
    #image_temp.is_bigendian=True
    image_temp.header = header
    image_temp.step = 1280*3
    image_pub.publish(image_temp)


if __name__ == '__main__':
    model_dir = os.path.dirname(nanodet_ros.nanodet.__file__)
    model_path = os.path.join(model_dir, 'model/nanodet.onnx')
    clsname_path = os.path.join(model_dir, 'model/coco.names')
    nanodet_result_image = np.zeros([IMAGE_HEIGHT, IMAGE_WIDTH, 3])
    '''
    模型初始化
    '''
    nanodet_model = my_nanodet(model_path=model_path, clsname_path=clsname_path)
    '''
    ros节点初始化
    '''
    rospy.init_node('ros_nanodet')
    image_topic_1 = "/usb_cam/image_raw"
    rospy.Subscriber(image_topic_1, Image, image_callback_1, queue_size=1, buff_size=52428800)
    rospy.loginfo('detect subscriber done')
    image_pub = rospy.Publisher('/nanodet_result_out', Image, queue_size=1)
    # rospy.init_node("yolo_result_out_node", anonymous=True)
    rospy.spin()
