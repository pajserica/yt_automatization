import moviepy.editor as mp
import os
import random
import re
from time import sleep

i = 0

# Set the directory you want to start from
tiktoks_dir = 'D:\\pyTikTube\\tiktoks\\football'

reactions_dir = 'D:\\pyTikTube\\Reactions\\crReact'

react_files = os.listdir(reactions_dir)



def extract_number(filename):
    match = re.match(r'(\d+)(.*)', filename)
    if match:
        return (int(match.group(1)), match.group(2))
    else:
        return (float('inf'), filename)


for fname in sorted(os.listdir(tiktoks_dir), key=extract_number):
    #os.remove(f"{tiktoks_dir}\\{fname}")
    
    random_file = random.choice(react_files)
    file_path = os.path.join(reactions_dir, random_file)

    video1 = mp.VideoFileClip(file_path)
    video2 = mp.VideoFileClip(f"{tiktoks_dir}\\{fname}")
    #if(video2.duration > 40):
        #os.remove(f"{tiktoks_dir}\\{fname}")
        #continue
    # Load the two input videos
    for k in range(10):
        if(video1.duration < video2.duration):
            random_file = random.choice(react_files)
            file_path = os.path.join(reactions_dir, random_file)
            print(f"trying: {random_file}")

            video1 = mp.VideoFileClip(file_path)
            video2 = mp.VideoFileClip(f"{tiktoks_dir}\\{fname}")
            
        else:
            print("breaking") 
            break

    
    # Set the durations of the input videos to be equal
    duration = min(video1.duration, video2.duration)
    video1 = video1.set_duration(duration)
    video2 = video2.set_duration(duration).set_pos("center")

    # Create a black image of size 1080 x 1920 pixels
    black_image = mp.ImageClip(r"C:\Users\PAJSER-PC\Desktop\Test Programi\pyTikTok\1-1080x1920.jpg", duration=duration)
    temp_image = mp.ImageClip(r"C:\Users\PAJSER-PC\Desktop\Test Programi\pyTikTok\1-1080x1920.jpg", duration=duration)

    # Resize the input videos to fit within the width of the black image
    width = 541
    aspect_ratio = video1.aspect_ratio
    height = int(width / aspect_ratio)
    video1 = video1.resize(width=width, height=height)
    temp_image = temp_image.resize(width=width, height=height)
    
    video2 = video2.resize(height = height)
    
    video2 = mp.CompositeVideoClip([temp_image,video2])

    combined = mp.clips_array([[video1, video2]])
    combined = combined.set_pos((((black_image.w - combined.w) / 2), (black_image.h - combined.h) / 2))
    
    # Overlay the two input videos on top of the black image
    final_clip = mp.CompositeVideoClip([black_image,combined])

    # Save the composite video to a file
    #if(video2.aspect_ratio < 0.6):
    final_clip.write_videofile(f'D:\\pyTikTube\\finalVideos\\crReact\\final{i}.mp4')
    i = i + 1
    print("delete VID")
    #sleep(10)
    



