import os
import sys

from get_clips import get_clips
from gui import GUI

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
    
    frames = get_clips(clips_path)
    print("Retrieved frames:", frames)

if __name__ == "__main__":
    main()