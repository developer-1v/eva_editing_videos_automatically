import cv2
import os
import psutil
import shelve
from collections import defaultdict
from print_tricks import pt
from globals import SUPPORTED_VIDEO_TYPES
from tqdm import tqdm

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        # Check memory usage and yield if necessary
        if psutil.virtual_memory().percent > 80:  # Adjust threshold as needed
            yield frames
            frames = []
    if frames:
        yield frames
    cap.release()

def find_repetitive_sequences(videos_folder, sequence_length=5, save_interval=1000):
    sequences_dict = defaultdict(list)
    video_files = [f for f in os.listdir(videos_folder) if any(f.endswith(ext) for ext in SUPPORTED_VIDEO_TYPES)]
    pt(video_files)
    
    with shelve.open('sequences_db') as db:
        for video_file in video_files:
            video_path = os.path.join(videos_folder, video_file)
            pt(video_path)
            
            for frames in extract_frames(video_path):
                for i in tqdm(range(len(frames) - sequence_length + 1), f'{video_file} frames'):
                    sequence = tuple(cv2.imencode('.jpg', frame)[1].tobytes() for frame in frames[i:i + sequence_length])
                    sequences_dict[sequence].append((video_file, i))
                
                # Save to disk periodically
                if len(sequences_dict) >= save_interval:
                    for seq, locs in sequences_dict.items():
                        if seq in db:
                            db[seq].extend(locs)
                        else:
                            db[seq] = locs
                    sequences_dict.clear()  # Clear in-memory dictionary to free up RAM

        # Save any remaining sequences
        for seq, locs in sequences_dict.items():
            if seq in db:
                db[seq].extend(locs)
            else:
                db[seq] = locs

    # Load repetitive sequences from disk
    repetitive_sequences = {seq: locs for seq, locs in db.items() if len(set(loc[0] for loc in locs)) >= 3}

    return repetitive_sequences

def main(path_to_series):
    repetitive_sequences = find_repetitive_sequences(path_to_series)
    
    for sequence, locations in repetitive_sequences.items():
        print(f"Repetitive sequence found in:")
        for video_file, frame_index in locations:
            print(f" - {video_file} at frame {frame_index}")

if __name__ == "__main__":
    video_path = os.path.join(os.getcwd(), 'videos_for_testing', 'compiled_videos_for_testing_generating_clips')
    pt(video_path)
    
    main(video_path)