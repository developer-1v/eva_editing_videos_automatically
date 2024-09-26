from print_tricks import pt

import os
import sys

from get_clips import find_clips
from gui import GUI
from get_image_frames_for_cuts import get_image_frames_for_cuts
from process_clips import process_clips
from tv_shows import cut_videos

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--gui':
            print("Started with GUI")
            # Add your GUI initialization code here
            series_path = GUI.get_series_path_from_gui()
            clips_path = GUI.get_clips_path_from_gui()
        else:
            print("Started from another script")
            series_path = sys.argv[1]
            clips_path = sys.argv[2]
    else:
        print("Started from terminal or double-click")
        cwd = os.getcwd()
        series_path = os.path.join(cwd, 'mha_flattened')
        clips_path = cwd
    
    folders_with_clips = find_clips(clips_path)
    # for folder in folders_with_clips:
    #     process_clips(folder)
    
    frames_to_cut = get_image_frames_for_cuts(folders_with_clips)
    
    cut_videos(series_path, frames_to_cut)
    pt(frames_to_cut)

if __name__ == "__main__":
    main()