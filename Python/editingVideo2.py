# Importing required module
from moviepy import VideoFileClip
  
# uploading the video
video = VideoFileClip('E:/SMLM Reborn/Ngodingskuy Reborn/Sistem Multimedia/Video Processing and Representation/Python/output.mp4')
  
video = video.subclipped(0, 20)
#time is always in seconds
# trimming some part of the video
video = video.cutout(5, 10)

# display clip
video.ipython_display(width = 360)