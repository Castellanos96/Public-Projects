import os # https://docs.python.org/3/library/os.html
import cv2 # https://pypi.org/project/opencv-python/
import face_recognition #https://pypi.org/project/face-recognition/

#project path
pjt_path = os.getcwd()

#Bool utility state
process_this_frame = True

# Utility list used for encoding process
face_names = []
face_locations = []
face_encodings = []
known_face_names = []
user_folder_paths = []
known_face_encodings = []

#list of dir used inside curent file
dir_list = [f for f in os.listdir(pjt_path) if os.path.isdir(os.path.join(pjt_path, f))]

#get names of know users
for item in dir_list:
    if item == '__pycache__' or item == 'venv' or item == '.idea' or item == 'dlib' :
       pass
    else:
        known_face_names.append(item)

# get known users folder paths
for name in known_face_names:
    #create path to user folder
    temp_folder = os.getcwd() + "/" + name
    #append path to list of paths
    user_folder_paths.append(temp_folder)

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# encode all known users faces using algo
for path in user_folder_paths:
    # move into user file
    os.chdir(path)
    #print("user path",path)
    #take first sample in dir
    sample = os.listdir(path)[0]
    # Load a sample picture and learn how to recognize it.
    user_image = face_recognition.load_image_file(sample)
    #print("user image",user_image)
    user_face_encoding = face_recognition.face_encodings(user_image)[0]
    #append encoding to face encoding list
    known_face_encodings.append(user_face_encoding)