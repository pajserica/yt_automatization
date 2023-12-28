from moviepy.editor import *
import os
from pathlib import Path
import numpy as np

EFFECT_DURATION = 0.3
CLIP_DURATION = 3
STRT_CLIP_DUR = 5
t = 1

def rotate_func(t):
    time1 = CLIP_DURATION/2
    if -t < time1:
        return 2+1*t  # Zoom-in.
    else: # 6 < t
        return 2+-1*(CLIP_DURATION + t)  # Zoom-out.

def moove_func(t, center):
    time1 = CLIP_DURATION/2.1
    time2 = CLIP_DURATION/1.9
    if -t < time1:
        return center+40*t  # Zoom-in.
    elif time1<=-t<time2:
        return center+40*-time1
    else: # 6 < t
        return center-40*(CLIP_DURATION+t)  # Zoom-out.

def zoom_in_out(t):
    return  1+0.5*np.sin(t/12)


video_dir = Path(r"C:\Users\PAJSER-PC\Desktop\Test Programi\TOP_10")

clip_list = [fname for fname in video_dir.iterdir() if fname.match('*.jpg')]

path = os.path.join(os.getcwd(), 'TOP_10')
clips = [ImageClip(f"{path}\{fname.name}")
.set_duration(CLIP_DURATION)
.resize(height=2000)
for fname in clip_list
]


start_vid = (VideoFileClip(f"{path}\\earth_space.mp4")
    .subclip(15,20)
    .set_position("center")
    .resize(height=2000)
    .rotate(lambda t: 0+1*t)
    .set_duration(STRT_CLIP_DUR)

)



text_clip = TextClip(txt=f"{clip_list[0].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[0].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

# For the first clip we will need it to start from the beginning and only add ((1080 - text_clip.w), 1500)
# slide out effect to the end of it
clip1 = CompositeVideoClip(
    [clips[0], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 0).resize(zoom_in_out)

text_clip = TextClip(txt=f"{clip_list[1].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[1].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

clip2 = CompositeVideoClip(
    [clips[1], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 1).resize(zoom_in_out)

text_clip = TextClip(txt=f"{clip_list[2].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[2].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

clip3 = CompositeVideoClip(
    [clips[2], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 2).resize(zoom_in_out)

text_clip = TextClip(txt=f"{clip_list[3].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[3].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

clip4 = CompositeVideoClip(
    [clips[3], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 3).resize(zoom_in_out)

text_clip = TextClip(txt=f"{clip_list[4].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[4].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

clip5 = CompositeVideoClip(
    [clips[4], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 4).resize(zoom_in_out)

text_clip = TextClip(txt=f"{clip_list[5].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[5].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

clip6 = CompositeVideoClip(
    [clips[5], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 5).resize(zoom_in_out)

text_clip = TextClip(txt=f"{clip_list[6].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[6].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

clip7 = CompositeVideoClip(
    [clips[6], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 6).resize(zoom_in_out)

text_clip = TextClip(txt=f"{clip_list[7].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[7].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

clip8 = CompositeVideoClip(
    [clips[7], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 7).resize(zoom_in_out)

text_clip = TextClip(txt=f"{clip_list[8].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[8].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

clip9= CompositeVideoClip(
    [clips[8], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 8).resize(zoom_in_out)

text_clip = TextClip(txt=f"{clip_list[9].name[:-4]}",
                    size=(.8*1080, 0),
                    font="Arial-Bold",
                    color="black").set_position("center")
im_width, im_height = text_clip.size
color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(255, 255, 255))
txt = CompositeVideoClip([color_clip, text_clip]).set_position(((clips[9].w - color_clip.w)/2, 1400)).set_duration(CLIP_DURATION)

clip10 = CompositeVideoClip(
    [clips[9], txt]
    
).set_position("center").rotate(lambda t: rotate_func(-t)).set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * 9).resize(zoom_in_out)



videos = (
    [start_vid]+[clip1] + [clip2] +[clip3]+[clip4]+[clip5]+[clip6]+[clip7]+[clip8]+
    # For all other clips in the middle, we need them to slide in to the previous clip and out for the next one
     [clip9] + [clip10]
)


video = CompositeVideoClip(videos, size=(1080, 1920))

'''video.write_videofile(
    "final_clip.mp4",
    codec="libx264",
    audio_codec="aac",
    preset="ultrafast",
    fps=24,
    threads=24,
    ffmpeg_params=["-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2", "-pix_fmt", "yuv420p"],
)'''
video.ipython_display(fps = 24)
#video.preview(fps = 20)
#r"C:\Users\PAJSER-PC\Desktop\Test Programi\TOP_10\ London.jpg"

'''+ [
        (
            CompositeVideoClip(
                [clip.fx(transfx.slide_in, duration=EFFECT_DURATION, side="right")]
            )
            .rotate(rotate_func)
            .set_start( STRT_CLIP_DUR + (CLIP_DURATION - EFFECT_DURATION) * idx+2)
            
            .set_position("center")
            .resize(zoom_in_out)
        )
            # set start to 1 since we start from second clip in the original array
        for idx, clip in enumerate(clips[1:-1], start=1)
    ]
    +'''