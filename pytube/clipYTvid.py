from pytube import YouTube
import subprocess

def convert_to_seconds(time_string):
    # Split the string into hours, minutes, and seconds
    parts = time_string.split(':')
    if len(parts) == 2:
        hours = 0
        minutes = int(parts[0])
        seconds = int(parts[1])
    elif len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
    else:
        raise ValueError('Invalid time string')

    # Convert the hours, minutes, and seconds to seconds
    return 3600 * hours + 60 * minutes + seconds

# Replace the URL with the URL of the YouTube video you want to download
url = input('input video url: ')
name = input("name of video: ")
# Set the start and end times for the part of the video you want to download
start_time = convert_to_seconds(input("write minutes:seconds start time: "))  # Start at 1 minute and 40 seconds
end_time = convert_to_seconds(input("write minutes:seconds end time: "))  # End at 2 minutes
resol = input("type resolution you want:")
print("download started")
# Download the video with pytube
yt = YouTube(url)
video = yt.streams.filter(res=resol).first().download('C:\\Users\\PAJSER-PC\\Desktop\\yt\\videos\\wholeVideos')


# Cut the video using FFmpeg
subprocess.run(['ffmpeg', '-i', video, '-ss', str(start_time), '-to', str(end_time), '-c:v', 'copy', '-c:a', 'copy', '-f', 'mp4','-y', f'C:\\Users\\PAJSER-PC\\Desktop\\yt\\videos\\shortVdeos\\{name}.mp4'])
