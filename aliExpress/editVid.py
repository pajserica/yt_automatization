from moviepy.editor import *
from pathlib import Path
import os 
from time import sleep
import random
import openai
import pyttsx3

# replace YOUR_API_KEY with your actual API key
openai.api_key = "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"

engine = pyttsx3.init()

video_dir = Path(r"D:\pyTikTube\aliExpress")
final_dir = r"D:\pyTikTube\finalVideos\affiliate\aliExpress"
bg_sng_dir = r"D:\pyTikTube\bg_songs"
temp_files = r"D:\pyTikTube\temp_files"
# Get a list of all mp3 files in the folder
files = [f for f in os.listdir(bg_sng_dir) if os.path.isfile(os.path.join(bg_sng_dir, f)) and f.endswith(".mp3")]


def map_values(x):
    old_min = 0.56692
    old_max = 1.77769
    new_min = 1
    new_max = 1.75
    old_range = old_max - old_min
    new_range = new_max - new_min
    return (((x - old_min) * new_range) / old_range) + new_min


for fname in video_dir.iterdir():
    print(fname.name[:-4])
    video = VideoFileClip(f"{fname}")
    video = video.set_pos("center").resize(width=1080 * map_values(video.aspect_ratio))
    if video.duration > 59:
        video = video.subclip(0,59)
    else:
        video = video.subclip(0,video.duration)
    bg_image = ImageClip(r"C:\Users\PAJSER-PC\Desktop\Test Programi\aliExpress\1-1080x1920.jpg", duration=video.duration)
    print(random.choice(files))
    bg_song = AudioFileClip(f"{bg_sng_dir}\\{random.choice(files)}").volumex(0.16)

    response1 = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"write me the three word summary of the following product {fname.name}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=1,
    )
    prod_name = response1["choices"][0]["text"]
    prod_name = prod_name
    print(f"prod_name: {prod_name.strip()}")
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a funny and interesting {int(video.duration)*2} second long text for a YouTube commercial to promote the product named {prod_name}. At the end say: 'to buy this product: click the link in the description. Please like the video. Thanks'",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Print the response
    prod_text = response["choices"][0]["text"]
    
    engine.save_to_file(prod_text, f"{temp_files}\\{fname.name[:-4]}.mp3")
    engine.runAndWait()

    #print(f"{temp_files}\\{fname.name}.mp3")
    # Load the audio file
    audio1 = AudioFileClip(f"{temp_files}\\{fname.name[:-4]}.mp3")
    audio = CompositeAudioClip([bg_song, audio1]).subclip(0,video.duration)

    text_clip = TextClip("LINK TO PRODUCT: \nIN DESCRIPTION OF THIS VIDEO", font="Arial-Bold",size=(1080, 200), color="orange", bg_color="black").set_duration(video.duration)
    text_clip = text_clip.set_pos((0, 0))

    final_clip = CompositeVideoClip([bg_image, video, text_clip]).set_audio(audio).audio_fadeout(2)
    
    final_clip.write_videofile(f'{final_dir}\\{prod_name.lstrip()} #shorts.mp4')
    
    #os.remove(f"{fname.name}.mp3")