# EdisonWebVideoProcessed
Use Intel Edison to serve live streaming video and display it normal and filtered

Run this simply with 

# python LiveStreamProcessed.py

It has several dependencies: openCV and Flask

You can install OpenCV on Edison by first sourcing AlexT's amazing opkg repo:

http://alextgalileo.altervista.org/edison-package-repo-configuration-instructions.html

And then installing with 

$ opkg install python-opencv

Dependencies will be dragged in automatically.  

You can install Flask by first installing pip

# wget https://bootstrap.pypa.io/get-pip.py
# python get-pip.py
# pip install flask


