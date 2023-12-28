from moviepy.editor import *
import os
import random

i = 0
part = 1

# Open the file in read mode
with open(r"C:\Users\PAJSER-PC\Desktop\Test Programi\pyTikTok\questions.txt", "r") as file:
  # Read all the lines in the file into a list
  lines = file.readlines()
  # Select a random line from the list
  question = random.choice(lines)
  print(question)




# Set the directory you want to start from
#tiktoks_dir = 'D:\\pyTikTube\\tiktoks\\shortFails'
tiktoks_dir = r'D:\pyTikTube\ytVideos\naruto2mins'

for dirName, subdirList, fileList in os.walk(tiktoks_dir):
    for fname in fileList:
        
        video2 = VideoFileClip(f"{tiktoks_dir}\\{fname}")
        video2 = video2.subclip(0, video2.duration - 12)

        black_image = ImageClip(r"C:\Users\PAJSER-PC\Desktop\Test Programi\pyTikTok\1-1080x1920.jpg", duration=video2.duration)
        # make 1 row of title
        if(len(fname) < 16):
            text_clip = TextClip(fname[:-4], font="Arial-Bold",size=(1080, 100), color="orange", bg_color="black").set_duration(video2.duration)
            text_clip = text_clip.set_pos((0, (black_image.h - video2.h) / 2.8))
        else:
            pos = fname.find(" ", (len(fname) // 2) - 5, (len(fname) // 2) + 5)

            # Divide the string into two equal parts
            if pos != -1:
                first_part = fname[:pos]
                second_part = fname[pos+1:]
            else:
                print("No space character found in the string.")

            text_clip1 = TextClip(first_part, font="Arial-Bold",size=(1080, 100), color="orange", bg_color="black").set_duration(video2.duration)
            text_clip2 = TextClip(second_part[:-4], font="Arial-Bold",size=(1080, 100), color="orange", bg_color="black").set_duration(video2.duration)
            text_clip = clips_array([[text_clip1], [text_clip2]]).set_pos((0, (black_image.h - video2.h) / 2.8 - 100))
        # Create a black image of size 1080 x 1920 pixels

        video2 = video2.resize(width = 1400).set_pos(((black_image.w - video2.w) / 2, (black_image.h - video2.h) / 2.8))
        
        #question on the end:
        pos1 = question.find(" ", (len(fname) // 2) - 5, (len(fname) // 2) + 5)
        if pos1 != -1:
            first_part1 = question[:pos1]
            second_part1 = question[pos1+1:]
        else:
            print("No space character found in the string.")
        quest_clip1 = TextClip(first_part1, font="Arial-Bold",size=(1080, 100), color="orange", bg_color="black").set_duration(video2.duration).set_position('center')
        quest_clip2 = TextClip(second_part1, font="Arial-Bold",size=(1080, 150), color="orange", bg_color="black").set_duration(video2.duration).set_position('center')

        sm_text = TextClip("FOR MORE VIDEOS", font="Arial-Bold",size=(1080, 150), color="white", bg_color="black").set_duration(video2.duration).set_position('center')
        sub_text = TextClip("SUBSCRIBE", font="Arial-Bold",size=(800, 200), color="white", bg_color="red").set_duration(video2.duration).set_position('center')
        quest_clip = clips_array([[quest_clip1], [quest_clip2], [sm_text], [sub_text]]).set_pos((0, (black_image.h - video2.h) / 2.8 + video2.h))
        
        #like_text = TextClip("pls LIKE VIDEO", font="Arial-Bold",size=(400, 80), color="white", bg_color="blue").set_duration(video2.duration)
        
        #like_text = like_text.set_pos(((black_image.w - like_text.w), 30)).rotate(6)
        duration = video2.duration
        start_time = 0
        end_time = 59

        while duration > end_time:
            
            what_part = TextClip(f"PART: {part}", font="Arial-Bold",size=(350, 200), color="white").set_duration(video2.duration)
            what_part = what_part.set_pos(((black_image.w - what_part.w) / 4, 50)).rotate(-13)
            # Overlay the two input videos on top of the black image
            final_clip = CompositeVideoClip([black_image,video2, text_clip, quest_clip, what_part])
            final_clip.subclip(start_time, end_time).write_videofile(f'D:\\pyTikTube\\finalVideos\\anime\\video-{i}_part-{part}.mp4')
            
            part += 1
            start_time = end_time
            if duration > start_time + 59:
                end_time += 59
            else:
                end_time = duration

        final_clip.subclip(start_time, duration).write_videofile(f'D:\\pyTikTube\\finalVideos\\anime\\video-{i}_part-{part}.mp4')
        part = 0
        print(f"clip [{fname}] order {i} finished")
        #os.remove(f"{tiktoks_dir}\\{fname}")
        i = i + 1

print("Making clips finished!")