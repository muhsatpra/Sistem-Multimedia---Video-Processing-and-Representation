from moviepy import *

clip = VideoFileClip('E:/SMLM Reborn/Ngodingskuy Reborn/Sistem Multimedia/Video Processing and Representation/Python/output.mp4')
clip1 = clip.subclipped(0, 10)
clip1.write_videofile('outputEdited.mp4',codec='libx264')