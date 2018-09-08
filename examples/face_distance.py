import face_recognition
import random 


# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.

from PIL import Image
import glob
image_path_list = []
for im_path in glob.glob('/home/sarah/Desktop/fall18/hackathon/home_depot_deep_learning/jpg/*.jpg'):
    image_path_list.append(im_path)

random_number = int(random.random() * len(image_path_list))

print(image_path_list[random_number])

# Load an output image and get encondings for it
# output_image = face_recognition.load_image_file("/home/sarah/Desktop/fall18/hackathon/home_depot_deep_learning/face_recognition/examples/obama2.jpg")
provided_image = face_recognition.load_image_file(image_path_list[random_number])
provided_image_encoding = face_recognition.face_encodings(provided_image)[0]


# Load image from the webcam
webcam_image = face_recognition.load_image_file("/home/sarah/Desktop/fall18/hackathon/home_depot_deep_learning/face_recognition/examples/obama.jpg")

# Get the face encodings for the webcam image
webcam_image_encoding = [face_recognition.face_encodings(webcam_image)[0]]

# See how far apart the webcam image is from the provided image
face_distances = face_recognition.face_distance(webcam_image_encoding, provided_image_encoding)

for i, face_distance in enumerate(face_distances):
    print("{:.2} from #{} expression".format(face_distance, i))
