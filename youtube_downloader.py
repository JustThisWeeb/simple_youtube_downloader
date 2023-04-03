from pytube import YouTube
from pytube import Playlist
import os
print("Youtube video downloader by jtw")
print("If you want to change directories type \"dir change\" in the choice input below.")
def directory_change(new_directory):
    with open('save_directory.txt', "w") as directory_file:
        directory_file.write(new_directory)
    directory_file.close()
    return f"directory changed to {new_directory}"

def read_directory(): #reading the contents of the save_directory file
    files = os.listdir()
    present = False
    for file in files: #Checking if the file exists in the same directory as the file.
        if file.startswith("save_directory"):
            present = True
    if present:
        with open("save_directory.txt", "r") as directory_file:
            directory = directory_file.readlines()
            directory_file.close()
            return directory
    else:
        directory_choice = input("the \"save_directory.txt\" file seems to be missing. Do you want for the script to create it or create it manually? (Y/N): ")
        if directory_choice == "Y":
            directory_change(input("put the path to the new directory here (make sure it's correct): "))


def single_video_download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        directory = read_directory()[0]
        youtube_object.download(directory)
    except:
        print("there was an error while downloading the video")
    print(f"{youtube_object.title} downloaded successfully\n")

def playlist_dowload(link):
    playlist = Playlist(link)
    for video in playlist.videos:
        print(f"Downloading {video.title}...")
        try:
            url = video.watch_url
            single_video_download(url)
        except:
            print(f"failed to download video {video.title}")
while True:
    choice = input("Choose if you want to download a single video or an entire playlist (1 and 2 respectively) or alternatively type \"exit\" to exit the script: ")
    if choice == "exit":
        exit()
    if choice == "1":
        link = input("Paste the url here: ")
        single_video_download(link)
    elif choice == "2":
        link = input("Paste the url here: ")
        playlist_dowload(link)
    elif choice == "dir change":
        print(directory_change(input("put the path to the new directory here (make sure it's correct): ")))
    else:
        print("bad input")
