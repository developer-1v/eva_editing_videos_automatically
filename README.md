SPEEDUP:
- We convert all frames to grayscale & make them down to a small small nuber. 
- Save that number as a dictionary key and the frame as the value (is there a more compact way of doing this?)
- When we look at the cut frames, we look for matching 

Solve: 

CUTTING THE CLIP TOO EARLY:

Option 1: - If we are getting the start/end image frames ourselves, then we can simply record the number of frames, and save that within the start_image title ('moviename_start_frame_132' = start frame then clip lasts 132 frames). 
    - Howver, this isn't dynamic, and doesn't allow a user to just input their 2 images for the same result. 

Option 2:
    - When we are looking for close matches, we record all of the close matches, and then sort them
    and choose the absolute closest match (instead of one that is "close enough" as it is
    currently doing). 
    - priority goes to the closest one, but if there are ties, then we pick the last one.  



GET RID OF THE PREVIEW AT THE END:
- Maybe the start of the preview has a specific image, always? 
    - maybe the preview is always the last thing, even if there is an extra's scene (are the extra's 
    always before the preview?)
    
- If start_frame also has some numbers afterwards, then this means it doesn't need an end frame, and we just to cut out those frames that it tells us to cut. 
- We can also label is as "final cut frame" to have the same effect.









- We should be able to specify if a particular cut can show up more than once. 
    (commercial transitions could happen multiple times, but an intro would only be once, so once that cut was found, we no longer have to look for it). 
- Specify roughly when the cut should show up.

- We copy/remember (and paste in a config file), the length of each video, the names of them, 
and the cuts that were found. 




- We have 2 distinct processes:
    1 - We mark & record (file) all of the positions of the cuts. This is regardless of movies.
        - the time to cut is Based on the opening frame of the entire episode. 
        Thus, whether the videos we obtain are off by differents amounts of seconds, it won't matter. 
    2 - We cut those out, and re-stitch the video together. 



Include Movies & OVA's???:
- If yes, then in Description for the video, we put where the movies/ova's start and end times so peeps can skip them if desired. 


One Cut vs. individual Episodes:
- One cut is cool, but is this viable as a video format?
- Might make more sense to do individual episodes on a playlist.
- Or each season as one video





Process for using clips instead of frames:
- We input the clips. 
    - App looks for a unique start frame: One that is easily identifiable as a unique frame.
    - Records amount of black screen time before unique start frame, if any (if processed from a clip video
    instead of images)
    - Checks to see if the final frame of the clip is a unique frame or black frame. 
    - If black, then backtracks to find the last unique frame and uses that final frame.
    - Records the black time after this final unique frame. 
    - We now have the 2 needed images (and black screen times) for the app to search, 
    for this particular cut. 



