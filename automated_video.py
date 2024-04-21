from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, AudioFileClip
from moviepy.audio.AudioClip import CompositeAudioClip


def generate_short_video(video_path, music_path):

  # Load video clip
  video_clip = VideoFileClip(video_path)



  cut_clip = int(input('How many clips do you want to select from the video?'))

  clips = []
  for i in range(cut_clip):
    print(f'enter start and end time of clip {i} : ')
    clips.append(tuple(input().split()))

  # Shorten video clips based on interesting sections
  short_clips = []

  # Concatenate short clips with smooth transitions
  for start, end in clips:
    short_clips.append(video_clip.subclip(start, end))

  #final clip
  final_clip = concatenate_videoclips(short_clips, method='compose')

  speed_factor = final_clip.duration / 30
  final_clip = final_clip.speedx(speed_factor)
  music_clip = AudioFileClip(music_path)
  music_clip = music_clip.set_duration(final_clip.duration)

  # Add background music
  final_clip = CompositeVideoClip([final_clip]).set_audio(music_clip)
  

  # Add text overlays (example)
  # You can use moviepy.text to add text overlays at specific timings
  txt_clips = []
  texts = []
  starts = [] 
  durations = []

  print(f'the final video duration is {final_clip.duration} seconds')

  opt = input('Do you want to add text (y or n)? : ')
  if(opt == 'y' or opt == 'yes'):
     no_txt = int(input("enter a number how many texts do you want to add : "))
     for i in range(no_txt):
        texts.append(input(f'enter text {i+1} : '))
        starts.append(int(input(f'enter when to start time for this text : ')))
        durations.append(int(input(f'enter the duration in secs : ')))

  if(opt == 'y' or opt == 'yes'):
    for text,t,duration in zip(texts, starts, durations): 
      txt_clip = TextClip(text,fontsize = 40, color='white')
      txt_clip = txt_clip.set_start(t)
      txt_clip = txt_clip.set_position('center','top').set_duration(duration)
      txt_clips.append(txt_clip)
   
  video_with_text = CompositeVideoClip([final_clip] + txt_clips)

  # resizing to 9:16 aspect ratio
  video_with_text.resize((720,1280)) 

  # Write final video
  video_with_text.write_videofile("short.mp4", fps=video_clip.fps, codec="libx264", audio_codec="aac")

# Example usage (replace paths and clip timings)
video_path = "C://Users//karth//Videos//balsb1.mp4"
music_path = "C://Users//karth//Music//animal_piano.mp3"
generate_short_video(video_path, music_path)

print("Short video generated!")
