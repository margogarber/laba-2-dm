import random
import numpy as np
from array import array

def task1():
    A = array('i', range(1000))
    print (A)


def task2(*args): 
    try:
        args = [random.randint(-100, 100) for _ in range(10)]
        if all(isinstance(i, int) for i in args):
            return array("i", args)
    except ValueError:
        print ('Error')
        return task2()


def task3():
    args = [random.randint(-100, 100) for _ in range(10)]
    def s1():
        a = sorted(args)
        return array("i", a)
    print (s1())
    def s2():
        b = sorted(args, reverse=True)
        return array("i", b)
    print (s2())


def task4():
    args1 = [random.randint(-100, 100) for _ in range(10)]
    a = sorted(args1)
    print(args1)
    args2 = [random.randint(-100, 100) for _ in range(10)]
    b = sorted(args2)
    print(args2)
    def script1():
        args3 = a + b
        args3 = sorted(args3)
        return array('i', args3)
    print(script1())
    def script2():
        for element in b:
           for i in range(len(a)):
               if element < a[i]:
                   a.insert(i, element)
                   break
           else:
               a.append(element)
        return array('i', a)
    print (script2())


def task5():
    N = 100
    if isinstance(N, int) and N>0:
        arr = array('i')
        while len(arr) < N:
            a = random.randint(1, N)
            arr.append(a)
        return sorted(arr)
    else:
        raise ValueError ('Error')
    

def task6():
    a = np.linspace(1.0, 100.0, 100)
    print (a)
    b = a.reshape(10,10)
    print (b)


def task7():
    a = np.linspace(1.0, 100.0, 100)
    b = a.reshape(10,10)
    c = np.array2string(b)
    print (c, '\n\n')


def task8():
    a = np.linspace(1.0, 100.0, 100)
    b = a.reshape(1,100)
    c = b.reshape(100,1)
    print (c)


def task9():
    a = [1, 2, 3]
    b = np.resize(a, (1, 30))
    print (b)


def task10():
    a = np.zeros((10,10), int)
    print (a)


def task11():
    a = np.linspace(1.0, 100.0, 100)
    b = a.reshape(10,10)
    max_cols = np.max(b, axis=0)
    min_cols = np.min(b, axis=0)
    max_rows = np.max(b, axis=1)
    min_rows = np.min(b, axis=1)
    print("Найбільші елементи кожного стовпця:", max_cols)
    print("Найменші елементи кожного стовпця:", min_cols)
    print("Найбільші елементи кожного рядка:", max_rows)
    print("Найменші елементи кожного рядка:", min_rows)

    
def task12():
    arr = [random.randint(-100, 100) for _ in range(10)]
    print (arr)
    b = np.max(arr)
    print (b)
    c = arr.index(b)
    print (c)


def task13():
    list1 = ('січень', 'квітень', 'травень', 'золото', 'мідь', 'олово')
    list2 = ('січень', 'квітень', 'травень', 'алюміній', 'рудій', 'свинець')
    list3 = np.setxor1d(list1, list2)
    print (list3)


def task14():
    months = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
    winter = (months[11], months[0], months[1])
    spring = (months[2], months[3], months[4])
    summer = (months[5], months[6], months[7])
    autumn = (months[8], months[9], months[10])
    seasons = (winter, spring, summer, autumn)
    print (seasons)


def task15():
    students = (["Іваненко Іван Іванович", "12.05.1998"], ["Петренко Петро Петрович", "03.08.2000"], ["Сидоренко Сидір Сидорович", "15.09.1997"])
    sorted_student = sorted(students, key=lambda x: x[1][6:] + x[1][3:5] + x[1][:2])
    return tuple(sorted_student)


def task16():
    list_price = [("хліб", 10, 50), ("молоко", 20, 30), ("яблуко", 5, 100)]
    order = [("хліб", 5), ("молоко", -10)]
    total_cost = 0
    for i in list_price:
        if isinstance(i[0],str) == False:
            raise ValueError("Аргумент продукту має бути рядком")
        if isinstance(i[1],int) == False:
            raise ValueError("Аргумент кількості має бути числом")
        if isinstance(i[2],int) == False:
            raise ValueError("Аргумент кількості має бути числом")
    for i in order:
        if i[1] <= 0:
            raise ValueError('К-сть повинна бути додатня')
        if isinstance(i[0],str) == False:
            raise ValueError("Аргумент продукту має бути рядком")
        if isinstance(i[1],int) == False:
            raise ValueError("Аргумент кількості має бути числом")

    pricelist_dictionary = {item[0].strip().lower(): [item[1], item[2]] for item in list_price}

    for product, order_q in order:
        changed_product_case = product.strip().lower()

        if changed_product_case not in pricelist_dictionary:
            return -2
        
        price, available_qty = pricelist_dictionary[changed_product_case]
        
        if order_q > available_qty:
            return -1
        
        total_cost += price * order_q
        pricelist_dictionary[changed_product_case][1] -= order_q
    
    updated_pricelist = [(product, pricelist_dictionary[product][0], 
                    pricelist_dictionary[product][1])
                         for product in pricelist_dictionary]
    
    return total_cost, updated_pricelist

def task17():
    class Student:
        def __init__(self, name ='', courses =[], phone_number = "", email="", degree=""):
            self.name = name
            self.courses = courses
            self.phone_number = phone_number
            self.email = email
            self.degree = degree

        def printDetails(self):
            print ("Ім'я: ", self.name)
            print ("Курси: ", self.courses)
            print ("Номер телефону: ", self.phone_number)
            print ("Емейл: ", self.email)
            print ("Ступінь: ", self.degree)
        def add_name(self, name):
            self.name = name

        def enroll(self, course):
            self.courses.append(course)

        def add_phone_number(self, phone_number):
            self.phone_number = phone_number

        def add_email(self, email_):
            self.email = email_
        
        def add_degree(self, degree):
            self.degree = degree

    student1 = Student('', [], '', '', '')

    name = input("Уведіть ім'я: " )
    student1.add_name(name)

    course = input("Уведіть курси, які вивчає: " + student1.name + " ")
    student1.enroll(course)

    while course != "stop":
        student1.enroll(course)
        print("Уведіть курси, які вивчає", student1.name)
        course = input ("Уведіть номер курсу або 'stop' ")

    phone_number = input("Уведіть номер телефону " + student1.name + " ")
    student1.add_phone_number(phone_number)

    email_ = input("Уведіть поштову скриньку " + student1.name + " ")
    student1.add_email(email_)

    degree = input("Уведіть ступінь " + student1.name + " ")
    student1.add_degree(degree)

    student1.printDetails()

def task18():
    class Employee:
        def __init__(self, name, age, position, pay):
            self.name = name
            self.age = age
            self.position = position
            self.pay = pay
            print("Створено об’єкт для "+ name)      
        def printDetails(self):
            print("Ім’я: ", self.name)
            print("Вік: ", self.age)
            print("Посада: ", self.position)
            print("Заробітня плата: ",self.pay)       
        def is_retired(self):
            if self.age >= 70:
                print("Пора на пенсію")
            else:
                print("На пенсію не треба")       
        def change_position(self, new_position):
            self.position = new_position   
        def change_pay(self, cash):
            self.pay += cash
    Employee1 = Employee("Микола", 72, "Касир", 10000)
    Employee1.change_pay(-2000)
    Employee1.is_retired()
    Employee1.change_position("Охоронник")
    Employee1.printDetails()


m = int(input('Choose task: '))
arr = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, task14, task15, task16, task17, task18]
try:
    print (arr[m-1]())
except IndexError:
    print('Всього 18 завдань')