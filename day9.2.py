# COllECTION OF PACKAGES ARE CALLED LIBRARIES
# COLLECTION OF LIBRARIES ARE CALLED PACKAGES
import webbrowser
import time
song = input('Enter your songs name')
while True:
        webbrowser.open(f'https://www.youtube.com/results?search_query={song}')
        time.sleep(5)