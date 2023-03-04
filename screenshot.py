                           # import  file PIL and pyscreenshot using pip install 
  
import PIL   # pip install pillow
import pyscreenshot  # pip install pyscreenshot 
image = pyscreenshot.grab()  # capture image using grab and save the value in the image variable 

image.show()   # to show the image after the screenshot 

image.save('screen.png')   # to save the image using the file name  
