# import libraries
import glob
import tqdm
import os

PATH = "INPUT FOLDER"
# extension
et = "pptx"  # or ppt
files = list(glob.glob(f"{PATH}/**/*.{et}", recursive=True))
for f in tqdm.tqdm(files):
    command = f'unoconv -f pdf \"{f}\"'
    os.system(command)
