from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
import sys
import time

subscription_key = os.environ['kkk']
endpoint = os.environ['xxx']

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

remote_image_url = input("Qual a URL da imagem? ")
print("")

'''
Describe an Image - remote
This example describes the contents of an image with the confidence score.
'''
# Call API
description_results = computervision_client.describe_image(remote_image_url)
tags_result_remote = computervision_client.tag_image(remote_image_url)
detect_domain_results_landmarks = computervision_client.analyze_image_by_domain("landmarks", remote_image_url)
print("===== Detect Domain-specific Content - Remote =====")
print("")
print("Landmarks in the remote image:")
if len(detect_domain_results_landmarks.result["landmarks"]) == 0:
    print("No landmarks detected.")
else:
    for landmark in detect_domain_results_landmarks.result["landmarks"]:
        print(landmark["name"])

print("")
# Get the captions (descriptions) from the response, with confidence level
print("Description of remote image: ")
print("")
if len(description_results.captions) == 0:
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
print()
print("Tags in the remote image: \n")
if len(tags_result_remote.tags) == 0:
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()
