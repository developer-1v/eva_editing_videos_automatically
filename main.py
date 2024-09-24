import os
import sys

from get_clips import get_clips




def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--gui':
            print("Started with GUI")
            # Add your GUI initialization code here
        else:
            print("Started from another script")
    else:
        print("Started from terminal or double-click")
    
    get_clips()

if __name__ == "__main__":
    main()