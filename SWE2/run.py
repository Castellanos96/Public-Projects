import threading
import cv2
import face_recognition
import lock
import user_data
import numpy as np

def swift_lock(user_name):

    sc_lock = False
    counter = 0
    # Bool utility state
    process_this_frame = True
    #starts loop to find registred users in camera frame

    while True:
        #default size for standard cameras
        #encouraged by face recognition developers
        ret, frame = user_data.video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        #print("SC STATUS TEST")
        if sc_lock is False:
            sc_lock = threading.Timer(lock.lock_timer, lock.lock_screen, (True,))
            sc_lock.start()

        counter += 1
        #allows computer camera acccess
        if process_this_frame:
            #maps user faces for detection
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(user_data.known_face_encodings, face_encoding)
                name = "Unregistered User"

                face_distances = face_recognition.face_distance(user_data.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                #print("found user:",name)

                if matches[best_match_index]:
                    #print(matches[best_match_index])
                    name = user_data.known_face_names[best_match_index]
                    print(name, "found ",counter,"times")
                    lock.lock_screen(False)
                    sc_lock.cancel()
                    sc_lock = False
                face_names.append(name)
        process_this_frame = not process_this_frame