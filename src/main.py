#!/usr/bin/env python3

import datetime as dt
from picamera import PiCamera
from gps_utils import parseGPS, createFilenames, convertToMP4 

# globals
VIDEO_LENGTH = (60 * 10) # in seconds
VIDEO_RATE = 25 # framerate

def main():
    recording_path = "/home/carpi/Recordings/"
    logging_path = "/home/carpi/Dashcam/Logs/"
    gps_dict = {
        "Date" : "xx/xx/xxxx",
        "Time" : "xx:xx:xx"
    }
    
    # initialize the camera and grab a reference 
    camera = PiCamera() 
    camera.resolution = (1280, 720) 
    camera.framerate = VIDEO_RATE
    camera.rotation = 90
    camera.start_preview() 

    try: 
        while True:
            start = dt.datetime.now()
            gps_dict["Date"] = dt.datetime.strftime(start, "%d/%m/%Y")
            gps_dict["Time"] = dt.datetime.strftime(start, "%H:%M:%S")
            record_file, log_file = createFilenames(recording_path, logging_path)
            # start recording using piCamera API
            camera.start_recording(record_file) 
             
            while (dt.datetime.now() - start).seconds < VIDEO_LENGTH: 

                # Overlay the data on each frame
                text = f"{gps_dict['Date']} {gps_dict['Time']}"
                camera.annotate_text = text

            print("Stopped " + record_file)
            camera.stop_recording()
            print("Converting to MP4...")
            convertToMP4(record_file, VIDEO_RATE)
            print("Finished with recording!")

    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print("\nDone.\nExiting.")

if __name__ == "__main__":
    main()
