from moviepy.editor import *
from pathlib import Path
import os 
from time import sleep
from pyttsx3 import engine


images_dir = Path(r"D:\pyTikTube\aliExpress")
final_dir = r"D:\pyTikTube\finalimages\affiliate\aliExpress"
bg_sng_dir = r"D:\pyTikTube\bg_songs"
temp_files = r"D:\pyTikTube\temp_files"
# Get a list of all mp3 files in the folder
#files = [f for f in os.listdir(bg_sng_dir) if os.path.isfile(os.path.join(bg_sng_dir, f)) and f.endswith(".mp3")]
with open("requests.txt", "r") as f:
    request = f.read().strip().upper()

def map_values(x):
    old_min = 0.56692
    old_max = 1.77769
    new_min = 1
    new_max = 1.75
    old_range = old_max - old_min
    new_range = new_max - new_min
    return (((x - old_min) * new_range) / old_range) + new_min


for fname in images_dir.iterdir():
    
    image = ImageClip(fname)
    image = image.set_pos("center").resize(width=1080 * map_values(image.aspect_ratio))
    
    if image.duration > 59:
        image = image.subclip(0,59)
    else:
        image = image.subclip(0,image.duration)
    bg_image = ImageClip(r"C:\Users\PAJSER-PC\Desktop\Test Programi\aliExpress\1-1080x1920.jpg", duration=image.duration)
    bg_song = AudioFileClip(f"{bg_sng_dir}\\{bg_song}").volumex(0.16)

    # Print the response
    prod_text = "This is {}"
    
    engine.save_to_file(prod_text, f"{temp_files}\\{fname.name[:-4]}.mp3")
    engine.runAndWait()

    #print(f"{temp_files}\\{fname.name}.mp3")
    # Load the audio file
    audio1 = AudioFileClip(f"{temp_files}\\{fname.name[:-4]}.mp3")
    audio = CompositeAudioClip([bg_song, audio1]).subclip(0,image.duration)

    text_clip = TextClip("LINK TO PRODUCT: \nIN DESCRIPTION OF THIS image", font="Arial-Bold",size=(1080, 200), color="orange", bg_color="black").set_duration(image.duration)
    text_clip = text_clip.set_pos((0, 0))

    final_clip = CompositeimageClip([bg_image, image, text_clip]).set_audio(audio).audio_fadeout(2)
    
    final_clip.write_imagefile(f'{final_dir}\\{prod_name.lstrip()} #shorts.mp4')
    
    #os.remove(f"{fname.name}.mp3")