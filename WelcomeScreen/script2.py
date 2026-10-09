import tkinter as tk
try:
    import av.container.input
    # Create a safe fallback property for fast_seek
    av.container.input.InputContainer.fast_seek = property(
        fget=lambda self: True,
        fset=lambda self, value: None
    )
except ImportError:
    pass
# ----------







from tkVideoPlayer import TkinterVideo

# Initialize root window
root = tk.Tk()
root.title("Tkinter Video Player")
root.geometry("800x600")

# Create the video player widget
# 'scaled=True' fits the video to the widget size dynamically
videoplayer = TkinterVideo(master=root, scaled=True)

# Load your video file (provide the correct path)
videoplayer.load("/Users/kajalprabhakar/Downloads/gui.mp4")

# Pack the widget to fill the window
videoplayer.pack(expand=True, fill="both")

# Start playing the video
videoplayer.play()

# Run the Tkinter event loop
root.mainloop()








