class WeekDaysError(Exception):
    pass


class Weeker:
    __weekDays = {
        "1": "Sun",
        "2": "Mon",
        "3": "Tue",
        "4": "Wed",
        "5": "Thu",
        "6": "Fri",
        "7": "Sat",
    }

    def __init__ (self,day):
        try:
            self.day = day
            self.n = int(Weeker.__weekDays[day])
        except WeekDaysError:
            print(f"No Week Day available for the entered day: {self.day}")

    def __str__(self):
        return Weeker.__weekDays

    def __add_days(self,n):
        self.n += n
        if self.n > 7:
            self.n = 1

    def _subtract_days(self,n):
        self.n -= n
        if self.n < 1:
            self.n = 7