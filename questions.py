
class Questions(object):

    def make(self):
        print("What is the make of your dream car?")
        make = input()
        return make

    def model(self):
        print("What is the model of your dream car?")
        model = input()
        return model

    def year(self):
        print("What is the year of your dream car?")
        year = input()
        return year

    def color(self):
        print("What is the color of this dream car?")
        color = input()
        return color

    def rank(self):
        print("rank this car 1-5, 1 being your favorite and 5 being least favorite")
        rank = input()
        return rank
