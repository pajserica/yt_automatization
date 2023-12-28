import os
from moviepy.editor import *

def rotate_func(t):
    if -t < 5:
        return 2*t  # Zoom-in.
    else: # 6 < t
        return -2*(duration+t)  # Zoom-out.

def moove_func(t, center):
    time1 = duration/2.1
    time2 = duration/1.9
    if -t < time1:
        return center+10*t  # Zoom-in.
    elif time1<=-t<time2:
        return center+10*-time1
    else: # 6 < t
        return center-10*(duration+t)  # Zoom-out.

duration = 10
screensize = (1080, 1920)
w,h = screensize

clip_img = (
    ImageClip('TOP_10\ London.jpg')
    .resize(height= 1920)
    #.resize()
    .set_position(lambda t: (moove_func(-t, (w - clip_img.w)/2), 'center'))
    #.rotate(lambda t: (rotate_func(-t)))
    .set_duration(duration)
    .set_fps(25)
    )

clip = CompositeVideoClip([clip_img], size=screensize)
#clip.write_videofile('test.mp4')
#clip.preview(fps=40)
clip.ipython_display(fps = 10)
#final1.write_videofile("testVid.mp4", fps=5)