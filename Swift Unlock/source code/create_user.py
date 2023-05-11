import os
import cv2
import user_data

pjt_path = os.getcwd()

def user_dir(user_name):
    user_folder_path = os.getcwd() + "/" + user_name
    return user_folder_path

def new_userFolder(user_name):
   new_folder = user_name
   current_directory = os.getcwd()
   final_directory = os.path.join(current_directory, new_folder)
   if not os.path.exists(final_directory):
      os.makedirs(final_directory)

def capture(user_name):

    user_folder_path = user_dir(user_name)
    new_userFolder(user_name)

    print("Use the spacebar key to capture pictures")
    print("If you'd like to exit, press the ESC key")

    cam = user_data.video_capture
    cv2.namedWindow("test")
    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing window...")
            break

        elif k%256 == 32:
            # SPACE pressed
            #move into user folder dir
            os.chdir(user_folder_path)
            #creating image name for user
            img_name = user_name+"_{}.png".format(img_counter)
            #saving user's sample image
            cv2.imwrite(img_name, frame)
            #confirmation message for image being created
            print("{} written!".format(img_name))
            #used to create naming sequence
            img_counter += 1
            #move back to project dir
            os.chdir(pjt_path)
    cam.release()
    cv2.destroyAllWindows()
    exit()


