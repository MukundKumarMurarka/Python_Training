"""
Singly inheritance program by using if and else statement
"""
class NumberList:
    number_list = [1, 5, 6, 9, 4, 2, 11, 13, 64, 51]
    def even_number(self):
        number_list2= self.number_list
        even_num =[]
        odd_num = []
        for i in range(len(number_list2)):
            if number_list2[i]  % 2 == 0:
                even_num.append(number_list2[i])
            else:
                odd_num.append(number_list2[i])
        print("even number list is : ", even_num)
        print("odd number list is ",odd_num)
class Even_odd_list(NumberList):
    def new_List(self):
        super().even_number()

num = Even_odd_list()
num.new_List()


