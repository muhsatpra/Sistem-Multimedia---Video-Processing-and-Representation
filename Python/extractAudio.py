import moviepy.editor

# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip("E:/SMLM Reborn/Ngodingskuy Reborn/Sistem Multimedia/Video Processing and Representation/Python/output.mp4")

audio = video.audio

# Replace the parameter with the location along with filename
audio.write_audiofile("E:/SMLM Reborn/Ngodingskuy Reborn/Sistem Multimedia/Video Processing and Representation/Python/sample.mp3")