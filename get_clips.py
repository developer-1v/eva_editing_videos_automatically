import os
from globals import POSSIBLE_CLIP_FOLDER_NAMES, SUPPORTED_IMAGE_TYPES, SUPPORTED_VIDEO_TYPES
from print_tricks import pt



def find_clips(clips_path):
    clips = []
    # Search for clips/cuts folders 
    for root, dirs, files in os.walk(clips_path):
        for dir_name in dirs:
            # pt(dir_name)
            if any(keyword in dir_name.lower() for keyword in POSSIBLE_CLIP_FOLDER_NAMES):
                folder_path = os.path.join(root, dir_name)
                
                for file_name in os.listdir(folder_path):
                    if file_name.lower().endswith(tuple(SUPPORTED_IMAGE_TYPES + SUPPORTED_VIDEO_TYPES)):
                        print(f"Found media file: {file_name}")
                        clips.append(folder_path)
                        break
    return clips

if __name__ == "__main__":
    cwd = os.getcwd()
    clips_path = cwd
    frames = find_clips(clips_path)
    pt(frames)