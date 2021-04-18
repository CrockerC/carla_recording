# carla

Requirements:
	Note: All development was done on the pre-compiled release of Carla. So requirements are based on that.
	Carla’s quickstart linked here: https://carla.readthedocs.io/en/latest/start_quickstart/
	Copy of the requirements with some notes and additions below
	
	•	Any 64-bit OS
	•	A powerful GPU, Carla recommends the server GPU to be at least “6 GB”, which is a bit overgeneralized. An RTX 3080 was used for our development. However GPU requirement is dependent on your usage. 
	•	A powerful CPU is also needed for smooth operation. An AMD 3700x was used for our development. High single core performance is preferable over high core count.
	•	Carla recommends 20 GB of disk space, however your requirements will vary wildly based on your recording needs. I recommend at least 200 GB of free space. 
	•	A fast SSD is recommended, as saving raw image data takes up an extreme amount of disk speed
	•	Python. Carla supports python 2 as well as python 3.7, however our development was done on python 3.7
	•	Carla recommends two TCP ports and a good network connection, however depending on your image and video settings in the recording, an extremely fast network connection (2.5 Gb/s or higher) will be needed if running the client and server of separate machines
	•	The, pygame, numpy, opencv2, and pillow python modules
Recommendations and notes:

	•	The video recording can use an extreme amount of disk speed, in my initial tests recording at 2560x1920 @ 20fps showed 375 MB/s of disk usage. I did it like this because processing the images into a video took too much CPU which would slow the simulator to a crawl, making it unusable. Depending on your settings and computer hardware, you could move the video processing to realtime. 
Installation:

	Follow the installation instructions here: 	https://carla.readthedocs.io/en/latest/start_quickstart/
	And then download our code, the folder can be placed anywhere on your computer.



Usage:

Basic usage of the script is “python3 manual_control_with_recording.py”, which will default to using Carla’s town 3. Use the “r” key on your keyboard to start and stop recording
	manual_control_with_recording.py arguments: 

	•	-v or –verbose, prints debug information
	•	--host, IP of the host server (default: 127.0.0.1)
	•	-p or –port, TCP port to use (defaults: 2000)
	•	-a or –autopilot, enable autopilot
	•	--res, window resolution (defaults: 1280x720)
	•	--filter, actor filter (default: "vehicle.*")
	•	--rolename, actor role name (default: "hero")
	•	--gamma, gamma correction of the camera (default: 2.2)
	•	-m or –map, map to drive around on (default: Town03)

If you want to change the resolution of the recording or time step of the simulation, go to line 159-162.
Note that increasing the resolution will reduce the performance of the simulation and increase the disk usage. 

Then use the command “python3 make_video.py 0” to create the video. Where 0 is the video number. 
make_video.py arguments:

	•	 Argument 0, is the id of the video (must be an integer, no default)
make_video.py takes the raw data outputted by the manual_control script, downscales (CAN ONLY DOWNSCALE) and converts it to an mp4 video as well as giving a .txt file with the speed of the car in every frame

event_sequences.py:
	file contains a set of weather parameters, as well as a class which contains a single variable called self.seq. This is a list of events that the user can fire off using the number pad “0” key. Simply follow the format of the examples already in the file if you want to define your own.


If you want to do further customization, refer to the Carla docs here https://carla.readthedocs.io/en/latest/


