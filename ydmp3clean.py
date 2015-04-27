import os
import sys

fileurl = str(sys.argv[1])
os.system("youtube-dl --extract-audio --audio-format mp3 %s" % fileurl)
videoid = fileurl[32:43]
print "The video id is : " + videoid
for filename in os.listdir("."):
    if filename.endswith("%s.mp3" % videoid):
        m = list(filename)
        print m
        count = 5
        while (count < 17):
            length = len(filename)
            m.pop(length-count)
            count = count + 1
        print m
        finalname = ''.join(m)
        print finalname
        os.rename(filename, finalname)