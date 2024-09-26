from print_tricks import pt

import os

from globals import SUPPORTED_IMAGE_TYPES

def get_image_frames_for_cuts(folders_with_clips):
    frames = []
    pt(folders_with_clips)
    start_images = {}
    end_images = {}
    
    for folder in folders_with_clips:
        for filename in os.listdir(folder):
            if not any(filename.endswith(ext) for ext in SUPPORTED_IMAGE_TYPES):
                continue  # Skip unsupported file types
            
            full_path = os.path.join(folder, filename)
            
            if "start" in filename:
                base_name = filename.replace("_start_frame.png", "")
                start_images[base_name] = full_path
            elif "end" in filename and "ending" not in filename:
                base_name = filename.replace("_end_frame.png", "")
                end_images[base_name] = full_path
            elif "end" in filename:
                base_name = filename.replace("_end_frame.png", "")
                end_images[base_name] = full_path
    
    for base_name in start_images:
        if base_name in end_images:
            frames.append((start_images[base_name], end_images[base_name]))
        else:
            raise ValueError(f"Missing end image for start image: {start_images[base_name]}")
    
    for base_name in end_images:
        if base_name not in start_images:
            raise ValueError(f"Missing start image for end image: {end_images[base_name]}")
    
    return frames