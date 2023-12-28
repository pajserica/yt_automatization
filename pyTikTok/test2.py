import moviepy.editor as mp
import os
import re

i = 0

#Set the directory you want to start from
tiktoks_dir = r'D:\pyTikTube\ytVideos\naruto2mins'

#Set the text you want to display on top of the tiktok video
text = 'FOOTBALL TIKTOK'

def extract_number(filename):
    match = re.match(r'(\d+)(.*)', filename)
    if match:
        return (int(match.group(1)), match.group(2))
    else:
        return (float('inf'), filename)

for fname in sorted(os.listdir(tiktoks_dir), key=extract_number):


    # Load the tiktok video
    video = mp.VideoFileClip(f"{tiktoks_dir}\\{fname}")
    video = video.resize(width=1080)

    # Create a text clip with the desired text and font size
    text_clip = mp.TextClip(text, fontsize=60, color='white')

    # Set the duration of the text clip to be the same as the video
    text_clip = text_clip.set_duration(video.duration)

    # Create a blank image to place the text on top of
    blank_image = mp.ImageClip("1-1080x1920.jpg", duration=video.duration)

    combined = mp.clips_array([[text_clip], [video]]).set_position((0, (blank_image.h - video.h) / 2))
    # Combine the text image with the tiktok video
    final_clip = mp.CompositeVideoClip([blank_image, combined])

    # Save the final composite video to a file
    final_clip.write_videofile(f'D:\\pyTikTube\\finalVideos\\final{i}.mp4')
    i = i + 1
    print("delete VID")
    #os.remove(fname)
