import moviepy.editor as mp
video = input("Please enter the path to video: ")
video = mp.VideoFileClip(video)
dst = input("Please enter the output directory: ")
dst = f'{dst}/converted.mp3'
video.audio.write_audiofile(dst)
