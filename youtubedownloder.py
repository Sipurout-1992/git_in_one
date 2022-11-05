from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ",yt.views)

argv[1] = "https://www.youtube.com/watch?v=KFsnY-4YPcw"