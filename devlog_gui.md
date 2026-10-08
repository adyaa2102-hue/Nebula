Loading an MP4 video crashed with an AttributeError on Python 3.14:
text
AttributeError: 'av.container.input.InputContainer' object has no attribute 'fast_seek' and no __dict__ for setting new attributes
Cause:
Recent updates to PyAV removed the .fast_seek property and switched the underlying C-extension layout away from dynamic dictionaries (__dict__). Legacy versions of tkVideoPlayer explicitly try to set this missing attribute on load.
Solution:
tkVideoPlayer and PyAV kept breaking on Python 3.14, so I completely ditched them. Instead, I rebuilt the video player from scratch using OpenCV (cv2) and Pillow (PIL).

