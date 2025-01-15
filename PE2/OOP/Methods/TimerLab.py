def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer:
    def __init__(self,hour=0,minutes=0,seconds=0):
        self.__hour = hour
        self.__minutes = minutes
        self.__seconds = seconds

        #
        # Write code here
        #

    def __str__(self):
        return two_digits(self.__hour) + ":" + two_digits(self.__minutes)+":"+two_digits(self.__seconds)
        #
        # Write code here
        #

    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__minutes += 1
            self.__seconds = 0
            if self.__minutes> 59:
                self.__hour += 1
                self.__minutes = 0
                if self.__hour > 23:
                    self.__hour =0


        # Write code here
        #

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds <0:
            self.__seconds = 59
            self.__minutes -=1
            if self.__minutes < 0:
                self.__minutes =59
                self.__hour -= 1
                if self.__hour  < 0:
                    self.__hour = 23
        #
        # Write code here
        #


timer = Timer(2, 9, 9)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)