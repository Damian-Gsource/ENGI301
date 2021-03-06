import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print('frame: width = {0} height = {1}'.format(frame_width,frame_height))
frame_width = 320
frame_height = 240
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 10, (frame_width,frame_height))

print('Camera Set Up')

try:
  while(True):
    ret, frame = cap.read()
  
    if ret == True: 
      
      # Write the frame into the file 'output.avi'
      out.write(frame)
      print('Frame Written')
      
      # Display the resulting frame    
      #cv2.imshow('frame',frame)
  
      # Press Q on keyboard to stop recording
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
    # Break the loop
    else:
      break  

except KeyboardInterrupt:
  pass

# When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
#cv2.destroyAllWindows() 
