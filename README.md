# carla

The my_script.py file is my carla client code, it was made by taking one of the example files and modifying to for my use.
I have given the car 2 sensors, one in third person and one on the dash. The camera on the dash records in 1920p
The recording is output with the speed on the car in batches of 20 frames into a series of binary file

These binary files are taken by the make_video.py script and processed into an mp4 video and a txt file that shows the speed of the car
In each frame in kph
