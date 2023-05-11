Swift Unlock 

Swift Unlock is a facial recognition biometric software that deals with static images captured from a video
to allow access to a desktop. 

Users can create profiles on their computers that capture images of them,
which will be used for authentication. The device locks if authentication fails.

The software will detect a face, “read” the facial features,
and use an algorithm to verify the face by encoding it into a facial signature
and comparing it with the user’s pre-analyzed facial patterns. 

If a match is not found, desktop locks the user out. 
It will be unlocked once the user is back in the frame.



The project folder for Swift Unlock is shared on Canvas. The project was developed primarily on Linux for ease of access to lock/unlock the device it is running on. Swift Unlock can detect and recognize faces on MacOS, but due to the high level of security on Mac systems, the lock/unlock portion of the project was restricted to Linux. 
To run this project, you will need to download the project folder where the virtual environment is already configured to include the necessary libraries. You will need a Linux operating system (highly recommended), or a virtual machine with ubuntu version 20 or higher, and python 3.8. Next, you will need to install the screensaver tool GNOME(https://linuxconfig.org/how-to-install-gnome-on-ubuntu-20-04-lts-focal-fossa), this tool will be used to lock and unlock the device. Then, install pyCharm (https://www.jetbrains.com/help/pycharm/installation-guide.html) community edition and move the project folder into pyCharm which should let you run the software as will be described below, as all other packages are included in the virtual environment of the project folder.

Running/Using Swift Unlock
1.	Download the project folder and move it into pyCharm.
2.	Launch pycharm (on terminal) with command pycharm-community or simply click the pyCharm icon.
3.	Move the project folder into a pyCharm project directory.
4.	Run the project script main.py. As a first-time user, to create your profile, 
	select the “Create Profile” button on the GUI displayed. 
	This will prompt you for a username and will open the camera to take sample pictures
	and save them into a directory used for comparison at the next login attempt. 
	Enter your username, and once the camera opens, click the space bar when you are ready to take a picture. 
	Once you’re done, press the ESC key to close this window.
5.	Now, run the main.py script again and click on “Face ID” button which will prompt you to enter your username
	for authentication. Enter the username you used to create your profile.
	The camera will now turn on and the software will look for a match on the profile. 
	If you are not in the camera frame within 10 seconds, the computer will be locked. 
	Otherwise, the computer will remain unlocked. 


