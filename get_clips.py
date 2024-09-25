import os
from globals import POSSIBLE_CLIP_FOLDER_NAMES, SUPPORTED_IMAGE_TYPES, SUPPORTED_VIDEO_TYPES
from print_tricks import pt
from process_clips import process_clips

def process_images(folder_path):
    print(f"Processing images in {folder_path}")

def get_clips(clips_path):
    frames = []  # List to store starting and ending frames
    # Search for clips/cuts folders 
    for root, dirs, files in os.walk(clips_path):
        for dir_name in dirs:
            pt(dir_name)
            if any(keyword in dir_name.lower() for keyword in POSSIBLE_CLIP_FOLDER_NAMES):
                folder_path = os.path.join(root, dir_name)
                
                for file_name in os.listdir(folder_path):
                    if file_name.lower().endswith(tuple(SUPPORTED_IMAGE_TYPES + SUPPORTED_VIDEO_TYPES)):
                        print(f"Found media file: {file_name}")
                        # Assuming process_clips returns a tuple of (start_frame, end_frame)
                        result = process_clips(folder_path)
                        if result is not None:
                            start_frame, end_frame = result
                            frames.append((start_frame, end_frame))
                        break
    return frames

# ... existing code ...

if __name__ == "__main__":
    cwd = os.getcwd()
    clips_path = cwd
    frames = get_clips(clips_path)
    pt(frames)