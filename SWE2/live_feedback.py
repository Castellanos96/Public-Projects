import user_data
import cv2
import face_recognition
import numpy as np

# method re-used from face recognition's official tutorial website
# https://pypi.org/project/face-recognition/
# has been modified as a tool for testing
# not necessary for the project

def find_and_label():
    # Bool utility state
    process_this_frame = True
    #starts loop to find registred users in camera frame
    while True:
        #default size for standard cameras
        #encouraged by face recognition developers
        ret, frame = user_data.video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        #allows computer camera acccess
        if process_this_frame:
            #maps user faces for detection
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(user_data.known_face_encodings, face_encoding)
                name = "Unknown User"
                face_distances = face_recognition.face_distance(user_data.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = user_data.known_face_names[best_match_index]
                    print("found user: ",name)
                face_names.append(name)
        process_this_frame = not process_this_frame
        #suggested for drawing and labeling user
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #display results for user
        cv2.imshow('Test', frame)
        #used to end script
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
    #ends thhe open windows
    user_data.video_capture.release()
    cv2.destroyAllWindows()

