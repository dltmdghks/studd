import os

class WaterPuriFler(object):
    def __init__(self, name):
        self.name = name

        if not os.path.isdir("log"):
            os.mkdir("log")
        if not os.path.exists("log/path_log.txt"):
            f = open("log/count_log.txt", 'w', encoding="utf8")
            f.write("Recording was start\n")
            f.close()

    def ice(self, a):
        print(self.name, "Ice is taking")
        with open("log/path_log.txt", 'a', encoding="utf8") as f:
            import datetime

            stamp = str(datetime.datetime.now())
            value = 'Ice is '
            log_line = stamp + "\t" + str(value) + "taking" + "\n"
            f.write(log_line)
    def hot(self, a):
        print(self.name,"Hot water is taking")
        with open("log/path_log.txt", 'a') as f:
            import datetime

            stamp = str(datetime.datetime.now())
            value = 'Hot water is'
            log_line = stamp + "\t" + str(value) + "taking" + "\n"
            f.write(log_line)
    def cold(self, a):
        print(self.name,"Cold water is taking")
        with open("log/path_log.txt", 'a') as f:
            import datetime

            stamp = str(datetime.datetime.now())
            value = 'Cold water is '
            log_line = stamp + "\t" + str(value) + "taking" + "\n"
            f.write(log_line)

THCH = WaterPuriFler('water purifier')

while True:
    print('hot: hot water, ice: ice, cold:cold water')
    a = input('Please enter the water you want to draw ==>')

    if(a == 'quit'):
        break
    elif(a == 'hot'):
        THCH.hot(a)
    elif(a == 'ice'):
        THCH.ice(a)
    elif(a == 'cold'):
        THCH.cold(a)
    else:
        print('Please re-enter.')