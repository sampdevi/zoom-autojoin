from datetime import datetime
import time
import os

cmd = 'C:/Users/exl/AppData/Roaming/Zoom/bin/Zoom.exe';

classes = [
    {
        "tag": "LCFILIA",
        "done": 0,
        "hour": "11",
        "minute": "00",
        "end_hour": "12",
        "end_min": "30",
        "link": "https://zoom.us/j/4919481653?pwd=c2RObUNiR0hlcE95anVYbEtDOFdsQT09"
    },
    {
        "tag": "CCICOMP",
        "done": 0,
        "hour": "14",
        "minute": "30",
        "end_hour": "04",
        "end_min": "30",
        "link": "https://zoom.us/j/96761825930?pwd=Q2ZOazNGVHFPdVlpUWxJYjc1RUowZz09"
    }
]


def main():
    sleepers = 1
    while 1:
        current = datetime.now()
        for i in classes:
            if(i['done'] == 1):
                if(current.strftime('%H') == i['end_hour']):
                    if(int(current.strftime('%M')) >= int(i['end_min'])):
                        os.system('taskkill /f /im "Zoom.exe" /t');
                        i['done'] = 0;

            if(current.strftime('%H') == i['hour']):
                if(int(current.strftime('%M')) >= int(i['minute'])):
                    print("[{}] (ClassJoiner): Joined class for {}.".format(current.strftime('%H:%M'), i["tag"]))
                    os.system('{} --url="{}"'.format(cmd, i['link']))
                    i['done'] = 1;

        sleepers -= 1;
        if(sleepers == 0):
            sleepers = 60;
            print("(ClassJoiner): Running: (Time: {})".format(current.strftime('%H:%M')))
        time.sleep(1)

main()
