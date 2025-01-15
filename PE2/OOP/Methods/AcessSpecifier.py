class Krishom:
    def visible(self):
        print("Visible")

    def __hidden(self):
        print("Hidden")

kr = Krishom()
kr.visible()

try:
    kr.__hidden()

except:
    print("Failed")

kr._Krishom__hidden() #this is why we say that python's private property are partially hidden