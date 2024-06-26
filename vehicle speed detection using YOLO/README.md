**VEHICLE AND SPEED DETECTION USING OPENCV,YOLO**

-> This system detects vehicles in a video stream.
<br>
-> YOLO (You Only Look Once) is used for real-time object detection.
<br>
-> Vehicles are detected in each frame of the video.
<br>
-> The positions of detected vehicles are tracked across subsequent frames.
<br>
-> Speed is calculated based on the change in position over time.
<br>
-> The distance traveled between frames is converted into km/h for speed estimation.
<br>
-> OpenCV handles video processing and drawing bounding boxes around detected vehicles.

**WORKING**

1. **Load YOLO Model**: The YOLO model is loaded to detect vehicles in each frame of the video stream.
2. **Object Detection and Tracking**: YOLO detects vehicles (cars and trucks) in each frame. Each detected vehicle is assigned a unique tracking ID.
3. **Perspective Transformation**: A BirdsEyeView transformation is applied to convert the camera view to a top-down view, enabling accurate speed calculation.
4. **Speed Calculation**: The speed of each tracked vehicle is calculated based on the change in its position over time. The calculated speed is displayed on the video.
5. **Detection of Speeding Vehicles**: Only vehicles exceeding speed limits (120 km/h for cars and 100 km/h for trucks) are identified and their speeds are displayed on the video along with their unique tracking IDs.

   
**EXECUTING**
<br>
1)clone the repository

2)Install the dependencies
<br>
install the required packages listed in requirements.txt using pip:

```   pip install -r requirements.txt   ```
<br>
3)Run the script
<br>

```   python app.py   ```


**FINAL OUTPUT OF THE PROJECT**


![WhatsApp Image 2024-06-26 at 20 35 21_4d56e835](https://github.com/Rishithabattu11/Rishicmr_opensource/assets/169015844/4178294c-6050-49d0-83ad-5840816652f7)



**DESCRIPTION OF OUTPUT**

In the output video, the system processes each frame to display the following:

- Vehicle Identification: Each vehicle detected in the frame is assigned a unique identifier, displayed as car1, car2, etc.
- Speed Display: The current speed of each identified vehicle is shown next to the vehicle in the frame.
- Speed Limit Exceedance: If a vehicle exceeds the speed limit (120 km/h for cars and 100 km/h for trucks), it is specifically noted in the output video.

This information is dynamically updated as the vehicles move through the frame, providing real-time speed detection and tracking.

**REAL_TIME APPLICATIONS**

<br>
1)Traffic Law Enforcement:
 Automatically detecting vehicles that exceed speed limits can be done by using  this technology to monitor roads and issue citations to drivers who violate speed regulations.
<br>

2)Road Safety and Accident Prevention:
 Monitoring vehicle speeds in real-time contributes significantly to road safety initiatives. By identifying and alerting authorities about speeding vehicles, this technology helps prevent accidents caused by excessive speed.




