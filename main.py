import youtube_dl
import cv2
import os


def get_id_from_url(link):
    return link[32:]


if not os.path.exists("frames"):
    os.mkdir("frames")

link_list = ["https://www.youtube.com/watch?v=y8Kyi0WNg40",
"https://www.youtube.com/watch?v=XgvR3y5JCXg",
"https://www.youtube.com/watch?v=KmtzQCSh6xk",
"https://www.youtube.com/watch?v=PfYnvDL0Qcw",
"https://www.youtube.com/watch?v=HsvA7p0LYUk",
"https://www.youtube.com/watch?v=HPPj6viIBmU",
"https://www.youtube.com/watch?v=J---aiyznGQ",
"https://www.youtube.com/watch?v=lrzKT-dFUjE",
"https://www.youtube.com/watch?v=QH2-TGUlwu4",
"https://www.youtube.com/watch?v=YBkmefllgiE",
"https://www.youtube.com/watch?v=gNgXP4HII_4",
"https://www.youtube.com/watch?v=EIyixC9NsLI",
"https://www.youtube.com/watch?v=P5ex69c_dAs"]

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

for current_link in link_list:
    link_id = get_id_from_url(current_link)
    video_folder = os.path.join("frames", link_id)
    if not os.path.exists(video_folder):
        os.mkdir(video_folder)

    video_info = ydl.extract_info(current_link, download=True)
    current_filename = video_info['id'] + "." + video_info['ext']
    capture = cv2.VideoCapture(current_filename)

    for i in range(video_info['duration']):
        for j in range(video_info['fps']):
            success, image = capture.read()

        if success:
            cv2.imwrite(os.path.join("frames", link_id) + "\\" + str(link_id) + "_" + str(i) + ".png", image)

    capture.release()
    os.remove(current_filename)
