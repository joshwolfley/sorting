from cars import Car
from questions import Questions
from sort import Sort

class Application(object):

    def __init__(self):
        self.questions = Questions()
        self.car_list = []
        self.sort = Sort()

    def main_menu(self):
        print("What would you like to do?")
        print("1 - practice sorting")
        print("2 - quit")

    def sorting_menu(self):
        print("1 - Sort by time entered")
        print("2 - Sort by ranking")
        print("3 - Sort by year (newest to oldest)")
        print("4 - Sort alphabetically by make")
        print("5 - Random")
        print("6 - End")

    def run(self):

        while True:
            self.main_menu()
            user_input = input()
            if user_input == "1":
                i = 0
                print("Please answer the following questions for your top 5 dream cars")
                while len(self.car_list) < 5:
                    i += 1
                    print(f"Car #{i}")
                    make = self.questions.make()
                    model = self.questions.model()
                    year = self.questions.year()
                    color = self.questions.color()
                    rank = self.questions.rank()
                    self.car_list.append(
                       Car(make=make, model=model, year=year, color=color, rank=rank))
                user_input = None
                while user_input != "6":
                    self.sorting_menu()
                    user_input = input()
                    if user_input == "1":
                        self.sort.sort_by_entry(car_list=self.car_list)
                    elif user_input == "2":
                        self.sort.sort_by_ranking(car_list=self.car_list)
                    elif user_input == "3":
                        self.sort.sort_by_year(car_list=self.car_list)
                    elif user_input == "4":
                        self.sort.sort_by_make(car_list=self.car_list)
                    elif user_input == "5":
                        self.sort.random_sort(car_list=self.car_list)
                    elif user_input == "6":
                        break
                    else:
                        print('try again')
            elif user_input == "2":
                break
            else:
                print("Not an option, try again")
        print(self.car_list)


if __name__ == "__main__":
    app = Application()
    app.run()





