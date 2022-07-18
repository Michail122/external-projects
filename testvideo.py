from moviepy.editor import VideoFileClip, concatenate_videoclips
import easygui

def get_video_files():
    clips = []
    nach = []
    kon = []
    clips_discriptors = []
    yn = 1
    while True:
        if yn==0:
            answer = input ('another video?').upper()
            if answer == 'Y':
                yn= 1
            if answer == 'N':
                yn=0
                return clips_discriptors

        if yn==1:
            clips.append(easygui.fileopenbox(filetypes=["*.mp4"]))
            print('Начало отрезка видео, введите количество часов, минут, секунд через Enter:')
            n_hours = int(input('Часов:')) * 60 * 60
            n_min = int(input('Минут:')) * 60
            n_second = int(input('Секунд:'))
            nach.append(n_second + n_min + n_hours)
            print('Конец отрезка видео, введите количество часов, минут, секунд через Enter:')
            k_hours = int(input('Часов:') * 60 * 60)
            k_min = int(input('Минут:') * 60)
            k_second = int(input('Секунд:'))
            kon.append(k_second + k_min + k_hours)
            print(nach,kon)
            clips_discriptors.append(VideoFileClip(clips[-1]).subclip(nach[-1], kon[-1]))
            print(clips_discriptors[-1])
            yn=0

clips_discriptors = get_video_files()
print(clips_discriptors)
final_clip = concatenate_videoclips(clips_discriptors)
final_clip.write_videofile("new.mp4")