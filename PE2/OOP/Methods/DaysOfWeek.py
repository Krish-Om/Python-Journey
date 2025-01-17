class WeekDayError(Exception):
    pass


class Weeker:
    __weekDays = ["Sun" ,"Mon", "Tue" ,"Wed", "Thu", "Fri", "Sat"]

    def __init__(self, day):
        try:
            self.__current = Weeker.__weekDays.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return f"{Weeker.__weekDays[self.__current]}"

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker("Mon")
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker("Monday")
except WeekDayError:
    print("Sorry, I can't serve your request.")
