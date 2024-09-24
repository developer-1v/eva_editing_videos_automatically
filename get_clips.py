import os
import cv2

POSSIBLE_CLIP_FOLDER_NAMES = ['clips', 'cuts', 'images', 'frames']
SUPPORTED_IMAGE_TYPES = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
SUPPORTED_VIDEO_TYPES = ['.mp4', '.avi', '.mov', '.mkv']


def process_images(folder_path):
    print(f"Processing images in {folder_path}")


def is_black_frame(frame, threshold=10):
    return cv2.mean(frame)[0] < threshold

def find_first_non_black_frame(cap):
    frame_index = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            return None, frame_index
        if not is_black_frame(frame):
            return frame, frame_index
        frame_index += 1

def find_last_non_black_frame(cap, total_frames):
    frame_index = total_frames - 1
    while frame_index >= 0:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        if not ret:
            return None, frame_index
        if not is_black_frame(frame):
            return frame, frame_index
        frame_index -= 1

def process_clips(folder_path):
    print(f"Processing videos in {folder_path}")
    
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(tuple(SUPPORTED_VIDEO_TYPES)):
            video_path = os.path.join(folder_path, file_name)
            cap = cv2.VideoCapture(video_path)
            
            if not cap.isOpened():
                print(f"Error opening video file {video_path}")
                continue
            
            # Get total number of frames
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # Find the first non-black frame
            start_frame, start_frame_index = find_first_non_black_frame(cap)
            if start_frame is None:
                print(f"No non-black frames found in the beginning of {video_path}")
                cap.release()
                continue
            
            # Find the last non-black frame
            end_frame, end_frame_index = find_last_non_black_frame(cap, total_frames)
            if end_frame is None:
                print(f"No non-black frames found at the end of {video_path}")
                cap.release()
                continue
            
            # Save the start and end frames as images
            start_frame_path = os.path.join(folder_path, f"{file_name}_start_frame.png")
            end_frame_path = os.path.join(folder_path, f"{file_name}_end_frame.png")
            cv2.imwrite(start_frame_path, start_frame)
            cv2.imwrite(end_frame_path, end_frame)
            
            print(f"Saved first non-black frame to {start_frame_path} at index {start_frame_index}")
            print(f"Saved last non-black frame to {end_frame_path} at index {end_frame_index}")
            
            cap.release()



def get_clips():
    # Search for a clips folder
    for root, dirs, files in os.walk('.'):
        for dir_name in dirs:
            if any(keyword in dir_name.lower() for keyword in POSSIBLE_CLIP_FOLDER_NAMES):
                folder_path = os.path.join(root, dir_name)
                
                # Check for images or videos in the folder
                for file_name in os.listdir(folder_path):
                    if file_name.lower().endswith(tuple(SUPPORTED_IMAGE_TYPES + SUPPORTED_VIDEO_TYPES)):
                        print(f"Found media file: {file_name} in {folder_path}")
                        
                        if file_name.lower().endswith(tuple(SUPPORTED_IMAGE_TYPES)):
                            process_images(folder_path)
                        elif file_name.lower().endswith(tuple(SUPPORTED_VIDEO_TYPES)):
                            process_clips(folder_path)
                        return