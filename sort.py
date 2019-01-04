from random import randint

class Sort(object):

    def sort_by_entry(self, car_list):

        for car in car_list:
            print(f'Ranking: {car.rank}  '
                  f'Make: {car.make}  '
                  f'Model: {car.model}  '
                  f'color: {car.color}  '
                  f'Year:  {car.year}')

    def sort_by_ranking(self, car_list):

        sorted_list = sorted(car_list, key=lambda Car: Car.rank, reverse=False)

        for car in sorted_list:
            print(f'Ranking: {car.rank}  '
                  f'Make: {car.make}  '
                  f'Model: {car.model}  '
                  f'color: {car.color}  '
                  f'Year:  {car.year}')

    def sort_by_year(self, car_list):

        sorted_list = sorted(car_list, key=lambda Car: Car.year, reverse=True)

        for car in sorted_list:
            print(f'Ranking: {car.rank}  '
                  f'Make: {car.make}  '
                  f'Model: {car.model}  '
                  f'color: {car.color}  '
                  f'Year:  {car.year}')

    def sort_by_make(self, car_list):

        sorted_list = sorted(car_list, key=lambda Car: Car.make, reverse=False)

        for car in sorted_list:
            print(f'Ranking: {car.rank}  '
                  f'Make: {car.make}  '
                  f'Model: {car.model}  '
                  f'color: {car.color}  '
                  f'Year:  {car.year}')

    def random_sort(self, car_list):  # why is it deleting all the cars in my original car_list?

        car_list_copy = car_list
        sorted_list = []
        while car_list_copy != []:
            try:
                sorted_list.append(car_list_copy.pop(randint(0, 5)))
            except IndexError:
                pass

        for car in sorted_list:
            print(f'Ranking: {car.rank}  '
                  f'Make: {car.make}  '
                  f'Model: {car.model}  '
                  f'color: {car.color}  '
                  f'Year:  {car.year}')




