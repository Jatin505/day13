Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:/python/Python37-32/day13/createtable1.py ============
>>> 
============= RESTART: C:/python/Python37-32/day13/fetchall1.py =============
[(1, 'audi', 52642), (2, 'mercedes', 57127), (3, 'skoda', 9000), (4, 'volvo', 29000), (5, 'beatley', 350000), (6, 'hummer', 41400), (7, 'volkswagen', 21600)]
------------------------------
(1, 'audi', 52642)
(2, 'mercedes', 57127)
(3, 'skoda', 9000)
(4, 'volvo', 29000)
(5, 'beatley', 350000)
(6, 'hummer', 41400)
(7, 'volkswagen', 21600)
>>> 
=============== RESTART: C:/python/Python37-32/day13/error.py ===============
>>> 
============= RESTART: C:/python/Python37-32/day13/fetchall1.py =============
[(6, 'citron', 210000), (7, 'hummer', 41400), (8, 'volkswagen', 21600)]
------------------------------
(6, 'citron', 210000)
(7, 'hummer', 41400)
(8, 'volkswagen', 21600)
>>> 
============ RESTART: C:/python/Python37-32/day13/createtable2.py ============
table created
enter id:505
enter name:jatin
Traceback (most recent call last):
  File "C:/python/Python37-32/day13/createtable2.py", line 15, in <module>
    cur.execute(input_fun())
  File "C:/python/Python37-32/day13/createtable2.py", line 5, in input_fun
    b=int(input("enter name:"))
ValueError: invalid literal for int() with base 10: 'jatin'
>>> 
============ RESTART: C:/python/Python37-32/day13/createtable2.py ============
table created
enter id:505
enter name:mercedes
enter price:52400
values in the table car inserted.
>>> 
============= RESTART: C:/python/Python37-32/day13/iris_print.py =============
5.1,3.5,1.4,0.2,Iris-setosa
 <class 'str'>
4.9,3.0,1.4,0.2,Iris-setosa
 <class 'str'>
4.7,3.2,1.3,0.2,Iris-setosa
 <class 'str'>
4.6,3.1,1.5,0.2,Iris-setosa
 <class 'str'>
5.0,3.6,1.4,0.2,Iris-setosa
 <class 'str'>
5.4,3.9,1.7,0.4,Iris-setosa
 <class 'str'>
4.6,3.4,1.4,0.3,Iris-setosa
 <class 'str'>
5.0,3.4,1.5,0.2,Iris-setosa
 <class 'str'>
4.4,2.9,1.4,0.2,Iris-setosa
 <class 'str'>
4.9,3.1,1.5,0.1,Iris-setosa
 <class 'str'>
5.4,3.7,1.5,0.2,Iris-setosa
 <class 'str'>
4.8,3.4,1.6,0.2,Iris-setosa
 <class 'str'>
4.8,3.0,1.4,0.1,Iris-setosa
 <class 'str'>
4.3,3.0,1.1,0.1,Iris-setosa
 <class 'str'>
5.8,4.0,1.2,0.2,Iris-setosa
 <class 'str'>
5.7,4.4,1.5,0.4,Iris-setosa
 <class 'str'>
5.4,3.9,1.3,0.4,Iris-setosa
 <class 'str'>
5.1,3.5,1.4,0.3,Iris-setosa
 <class 'str'>
5.7,3.8,1.7,0.3,Iris-setosa
 <class 'str'>
5.1,3.8,1.5,0.3,Iris-setosa
 <class 'str'>
5.4,3.4,1.7,0.2,Iris-setosa
 <class 'str'>
5.1,3.7,1.5,0.4,Iris-setosa
 <class 'str'>
4.6,3.6,1.0,0.2,Iris-setosa
 <class 'str'>
5.1,3.3,1.7,0.5,Iris-setosa
 <class 'str'>
4.8,3.4,1.9,0.2,Iris-setosa
 <class 'str'>
5.0,3.0,1.6,0.2,Iris-setosa
 <class 'str'>
5.0,3.4,1.6,0.4,Iris-setosa
 <class 'str'>
5.2,3.5,1.5,0.2,Iris-setosa
 <class 'str'>
5.2,3.4,1.4,0.2,Iris-setosa
 <class 'str'>
4.7,3.2,1.6,0.2,Iris-setosa
 <class 'str'>
4.8,3.1,1.6,0.2,Iris-setosa
 <class 'str'>
5.4,3.4,1.5,0.4,Iris-setosa
 <class 'str'>
5.2,4.1,1.5,0.1,Iris-setosa
 <class 'str'>
5.5,4.2,1.4,0.2,Iris-setosa
 <class 'str'>
4.9,3.1,1.5,0.1,Iris-setosa
 <class 'str'>
5.0,3.2,1.2,0.2,Iris-setosa
 <class 'str'>
5.5,3.5,1.3,0.2,Iris-setosa
 <class 'str'>
4.9,3.1,1.5,0.1,Iris-setosa
 <class 'str'>
4.4,3.0,1.3,0.2,Iris-setosa
 <class 'str'>
5.1,3.4,1.5,0.2,Iris-setosa
 <class 'str'>
5.0,3.5,1.3,0.3,Iris-setosa
 <class 'str'>
4.5,2.3,1.3,0.3,Iris-setosa
 <class 'str'>
4.4,3.2,1.3,0.2,Iris-setosa
 <class 'str'>
5.0,3.5,1.6,0.6,Iris-setosa
 <class 'str'>
5.1,3.8,1.9,0.4,Iris-setosa
 <class 'str'>
4.8,3.0,1.4,0.3,Iris-setosa
 <class 'str'>
5.1,3.8,1.6,0.2,Iris-setosa
 <class 'str'>
4.6,3.2,1.4,0.2,Iris-setosa
 <class 'str'>
5.3,3.7,1.5,0.2,Iris-setosa
 <class 'str'>
5.0,3.3,1.4,0.2,Iris-setosa
 <class 'str'>
7.0,3.2,4.7,1.4,Iris-versicolor
 <class 'str'>
6.4,3.2,4.5,1.5,Iris-versicolor
 <class 'str'>
6.9,3.1,4.9,1.5,Iris-versicolor
 <class 'str'>
5.5,2.3,4.0,1.3,Iris-versicolor
 <class 'str'>
6.5,2.8,4.6,1.5,Iris-versicolor
 <class 'str'>
5.7,2.8,4.5,1.3,Iris-versicolor
 <class 'str'>
6.3,3.3,4.7,1.6,Iris-versicolor
 <class 'str'>
4.9,2.4,3.3,1.0,Iris-versicolor
 <class 'str'>
6.6,2.9,4.6,1.3,Iris-versicolor
 <class 'str'>
5.2,2.7,3.9,1.4,Iris-versicolor
 <class 'str'>
5.0,2.0,3.5,1.0,Iris-versicolor
 <class 'str'>
5.9,3.0,4.2,1.5,Iris-versicolor
 <class 'str'>
6.0,2.2,4.0,1.0,Iris-versicolor
 <class 'str'>
6.1,2.9,4.7,1.4,Iris-versicolor
 <class 'str'>
5.6,2.9,3.6,1.3,Iris-versicolor
 <class 'str'>
6.7,3.1,4.4,1.4,Iris-versicolor
 <class 'str'>
5.6,3.0,4.5,1.5,Iris-versicolor
 <class 'str'>
5.8,2.7,4.1,1.0,Iris-versicolor
 <class 'str'>
6.2,2.2,4.5,1.5,Iris-versicolor
 <class 'str'>
5.6,2.5,3.9,1.1,Iris-versicolor
 <class 'str'>
5.9,3.2,4.8,1.8,Iris-versicolor
 <class 'str'>
6.1,2.8,4.0,1.3,Iris-versicolor
 <class 'str'>
6.3,2.5,4.9,1.5,Iris-versicolor
 <class 'str'>
6.1,2.8,4.7,1.2,Iris-versicolor
 <class 'str'>
6.4,2.9,4.3,1.3,Iris-versicolor
 <class 'str'>
6.6,3.0,4.4,1.4,Iris-versicolor
 <class 'str'>
6.8,2.8,4.8,1.4,Iris-versicolor
 <class 'str'>
6.7,3.0,5.0,1.7,Iris-versicolor
 <class 'str'>
6.0,2.9,4.5,1.5,Iris-versicolor
 <class 'str'>
5.7,2.6,3.5,1.0,Iris-versicolor
 <class 'str'>
5.5,2.4,3.8,1.1,Iris-versicolor
 <class 'str'>
5.5,2.4,3.7,1.0,Iris-versicolor
 <class 'str'>
5.8,2.7,3.9,1.2,Iris-versicolor
 <class 'str'>
6.0,2.7,5.1,1.6,Iris-versicolor
 <class 'str'>
5.4,3.0,4.5,1.5,Iris-versicolor
 <class 'str'>
6.0,3.4,4.5,1.6,Iris-versicolor
 <class 'str'>
6.7,3.1,4.7,1.5,Iris-versicolor
 <class 'str'>
6.3,2.3,4.4,1.3,Iris-versicolor
 <class 'str'>
5.6,3.0,4.1,1.3,Iris-versicolor
 <class 'str'>
5.5,2.5,4.0,1.3,Iris-versicolor
 <class 'str'>
5.5,2.6,4.4,1.2,Iris-versicolor
 <class 'str'>
6.1,3.0,4.6,1.4,Iris-versicolor
 <class 'str'>
5.8,2.6,4.0,1.2,Iris-versicolor
 <class 'str'>
5.0,2.3,3.3,1.0,Iris-versicolor
 <class 'str'>
5.6,2.7,4.2,1.3,Iris-versicolor
 <class 'str'>
5.7,3.0,4.2,1.2,Iris-versicolor
 <class 'str'>
5.7,2.9,4.2,1.3,Iris-versicolor
 <class 'str'>
6.2,2.9,4.3,1.3,Iris-versicolor
 <class 'str'>
5.1,2.5,3.0,1.1,Iris-versicolor
 <class 'str'>
5.7,2.8,4.1,1.3,Iris-versicolor
 <class 'str'>
6.3,3.3,6.0,2.5,Iris-virginica
 <class 'str'>
5.8,2.7,5.1,1.9,Iris-virginica
 <class 'str'>
7.1,3.0,5.9,2.1,Iris-virginica
 <class 'str'>
6.3,2.9,5.6,1.8,Iris-virginica
 <class 'str'>
6.5,3.0,5.8,2.2,Iris-virginica
 <class 'str'>
7.6,3.0,6.6,2.1,Iris-virginica
 <class 'str'>
4.9,2.5,4.5,1.7,Iris-virginica
 <class 'str'>
7.3,2.9,6.3,1.8,Iris-virginica
 <class 'str'>
6.7,2.5,5.8,1.8,Iris-virginica
 <class 'str'>
7.2,3.6,6.1,2.5,Iris-virginica
 <class 'str'>
6.5,3.2,5.1,2.0,Iris-virginica
 <class 'str'>
6.4,2.7,5.3,1.9,Iris-virginica
 <class 'str'>
6.8,3.0,5.5,2.1,Iris-virginica
 <class 'str'>
5.7,2.5,5.0,2.0,Iris-virginica
 <class 'str'>
5.8,2.8,5.1,2.4,Iris-virginica
 <class 'str'>
6.4,3.2,5.3,2.3,Iris-virginica
 <class 'str'>
6.5,3.0,5.5,1.8,Iris-virginica
 <class 'str'>
7.7,3.8,6.7,2.2,Iris-virginica
 <class 'str'>
7.7,2.6,6.9,2.3,Iris-virginica
 <class 'str'>
6.0,2.2,5.0,1.5,Iris-virginica
 <class 'str'>
6.9,3.2,5.7,2.3,Iris-virginica
 <class 'str'>
5.6,2.8,4.9,2.0,Iris-virginica
 <class 'str'>
7.7,2.8,6.7,2.0,Iris-virginica
 <class 'str'>
6.3,2.7,4.9,1.8,Iris-virginica
 <class 'str'>
6.7,3.3,5.7,2.1,Iris-virginica
 <class 'str'>
7.2,3.2,6.0,1.8,Iris-virginica
 <class 'str'>
6.2,2.8,4.8,1.8,Iris-virginica
 <class 'str'>
6.1,3.0,4.9,1.8,Iris-virginica
 <class 'str'>
6.4,2.8,5.6,2.1,Iris-virginica
 <class 'str'>
7.2,3.0,5.8,1.6,Iris-virginica
 <class 'str'>
7.4,2.8,6.1,1.9,Iris-virginica
 <class 'str'>
7.9,3.8,6.4,2.0,Iris-virginica
 <class 'str'>
6.4,2.8,5.6,2.2,Iris-virginica
 <class 'str'>
6.3,2.8,5.1,1.5,Iris-virginica
 <class 'str'>
6.1,2.6,5.6,1.4,Iris-virginica
 <class 'str'>
7.7,3.0,6.1,2.3,Iris-virginica
 <class 'str'>
6.3,3.4,5.6,2.4,Iris-virginica
 <class 'str'>
6.4,3.1,5.5,1.8,Iris-virginica
 <class 'str'>
6.0,3.0,4.8,1.8,Iris-virginica
 <class 'str'>
6.9,3.1,5.4,2.1,Iris-virginica
 <class 'str'>
6.7,3.1,5.6,2.4,Iris-virginica
 <class 'str'>
6.9,3.1,5.1,2.3,Iris-virginica
 <class 'str'>
5.8,2.7,5.1,1.9,Iris-virginica
 <class 'str'>
6.8,3.2,5.9,2.3,Iris-virginica
 <class 'str'>
6.7,3.3,5.7,2.5,Iris-virginica
 <class 'str'>
6.7,3.0,5.2,2.3,Iris-virginica
 <class 'str'>
6.3,2.5,5.0,1.9,Iris-virginica
 <class 'str'>
6.5,3.0,5.2,2.0,Iris-virginica
 <class 'str'>
6.2,3.4,5.4,2.3,Iris-virginica
 <class 'str'>
5.9,3.0,5.1,1.8,Iris-virginica <class 'str'>
>>> 
============= RESTART: C:/python/Python37-32/day13/iris_print.py =============
Traceback (most recent call last):
  File "C:/python/Python37-32/day13/iris_print.py", line 4, in <module>
    temp=line[0:-1].split(' , ')
NameError: name 'line' is not defined
>>> 
============= RESTART: C:/python/Python37-32/day13/iris_print.py =============
['5.1,3.5,1.4,0.2,Iris-setosa']
['4.9,3.0,1.4,0.2,Iris-setosa']
['4.7,3.2,1.3,0.2,Iris-setosa']
['4.6,3.1,1.5,0.2,Iris-setosa']
['5.0,3.6,1.4,0.2,Iris-setosa']
['5.4,3.9,1.7,0.4,Iris-setosa']
['4.6,3.4,1.4,0.3,Iris-setosa']
['5.0,3.4,1.5,0.2,Iris-setosa']
['4.4,2.9,1.4,0.2,Iris-setosa']
['4.9,3.1,1.5,0.1,Iris-setosa']
['5.4,3.7,1.5,0.2,Iris-setosa']
['4.8,3.4,1.6,0.2,Iris-setosa']
['4.8,3.0,1.4,0.1,Iris-setosa']
['4.3,3.0,1.1,0.1,Iris-setosa']
['5.8,4.0,1.2,0.2,Iris-setosa']
['5.7,4.4,1.5,0.4,Iris-setosa']
['5.4,3.9,1.3,0.4,Iris-setosa']
['5.1,3.5,1.4,0.3,Iris-setosa']
['5.7,3.8,1.7,0.3,Iris-setosa']
['5.1,3.8,1.5,0.3,Iris-setosa']
['5.4,3.4,1.7,0.2,Iris-setosa']
['5.1,3.7,1.5,0.4,Iris-setosa']
['4.6,3.6,1.0,0.2,Iris-setosa']
['5.1,3.3,1.7,0.5,Iris-setosa']
['4.8,3.4,1.9,0.2,Iris-setosa']
['5.0,3.0,1.6,0.2,Iris-setosa']
['5.0,3.4,1.6,0.4,Iris-setosa']
['5.2,3.5,1.5,0.2,Iris-setosa']
['5.2,3.4,1.4,0.2,Iris-setosa']
['4.7,3.2,1.6,0.2,Iris-setosa']
['4.8,3.1,1.6,0.2,Iris-setosa']
['5.4,3.4,1.5,0.4,Iris-setosa']
['5.2,4.1,1.5,0.1,Iris-setosa']
['5.5,4.2,1.4,0.2,Iris-setosa']
['4.9,3.1,1.5,0.1,Iris-setosa']
['5.0,3.2,1.2,0.2,Iris-setosa']
['5.5,3.5,1.3,0.2,Iris-setosa']
['4.9,3.1,1.5,0.1,Iris-setosa']
['4.4,3.0,1.3,0.2,Iris-setosa']
['5.1,3.4,1.5,0.2,Iris-setosa']
['5.0,3.5,1.3,0.3,Iris-setosa']
['4.5,2.3,1.3,0.3,Iris-setosa']
['4.4,3.2,1.3,0.2,Iris-setosa']
['5.0,3.5,1.6,0.6,Iris-setosa']
['5.1,3.8,1.9,0.4,Iris-setosa']
['4.8,3.0,1.4,0.3,Iris-setosa']
['5.1,3.8,1.6,0.2,Iris-setosa']
['4.6,3.2,1.4,0.2,Iris-setosa']
['5.3,3.7,1.5,0.2,Iris-setosa']
['5.0,3.3,1.4,0.2,Iris-setosa']
['7.0,3.2,4.7,1.4,Iris-versicolor']
['6.4,3.2,4.5,1.5,Iris-versicolor']
['6.9,3.1,4.9,1.5,Iris-versicolor']
['5.5,2.3,4.0,1.3,Iris-versicolor']
['6.5,2.8,4.6,1.5,Iris-versicolor']
['5.7,2.8,4.5,1.3,Iris-versicolor']
['6.3,3.3,4.7,1.6,Iris-versicolor']
['4.9,2.4,3.3,1.0,Iris-versicolor']
['6.6,2.9,4.6,1.3,Iris-versicolor']
['5.2,2.7,3.9,1.4,Iris-versicolor']
['5.0,2.0,3.5,1.0,Iris-versicolor']
['5.9,3.0,4.2,1.5,Iris-versicolor']
['6.0,2.2,4.0,1.0,Iris-versicolor']
['6.1,2.9,4.7,1.4,Iris-versicolor']
['5.6,2.9,3.6,1.3,Iris-versicolor']
['6.7,3.1,4.4,1.4,Iris-versicolor']
['5.6,3.0,4.5,1.5,Iris-versicolor']
['5.8,2.7,4.1,1.0,Iris-versicolor']
['6.2,2.2,4.5,1.5,Iris-versicolor']
['5.6,2.5,3.9,1.1,Iris-versicolor']
['5.9,3.2,4.8,1.8,Iris-versicolor']
['6.1,2.8,4.0,1.3,Iris-versicolor']
['6.3,2.5,4.9,1.5,Iris-versicolor']
['6.1,2.8,4.7,1.2,Iris-versicolor']
['6.4,2.9,4.3,1.3,Iris-versicolor']
['6.6,3.0,4.4,1.4,Iris-versicolor']
['6.8,2.8,4.8,1.4,Iris-versicolor']
['6.7,3.0,5.0,1.7,Iris-versicolor']
['6.0,2.9,4.5,1.5,Iris-versicolor']
['5.7,2.6,3.5,1.0,Iris-versicolor']
['5.5,2.4,3.8,1.1,Iris-versicolor']
['5.5,2.4,3.7,1.0,Iris-versicolor']
['5.8,2.7,3.9,1.2,Iris-versicolor']
['6.0,2.7,5.1,1.6,Iris-versicolor']
['5.4,3.0,4.5,1.5,Iris-versicolor']
['6.0,3.4,4.5,1.6,Iris-versicolor']
['6.7,3.1,4.7,1.5,Iris-versicolor']
['6.3,2.3,4.4,1.3,Iris-versicolor']
['5.6,3.0,4.1,1.3,Iris-versicolor']
['5.5,2.5,4.0,1.3,Iris-versicolor']
['5.5,2.6,4.4,1.2,Iris-versicolor']
['6.1,3.0,4.6,1.4,Iris-versicolor']
['5.8,2.6,4.0,1.2,Iris-versicolor']
['5.0,2.3,3.3,1.0,Iris-versicolor']
['5.6,2.7,4.2,1.3,Iris-versicolor']
['5.7,3.0,4.2,1.2,Iris-versicolor']
['5.7,2.9,4.2,1.3,Iris-versicolor']
['6.2,2.9,4.3,1.3,Iris-versicolor']
['5.1,2.5,3.0,1.1,Iris-versicolor']
['5.7,2.8,4.1,1.3,Iris-versicolor']
['6.3,3.3,6.0,2.5,Iris-virginica']
['5.8,2.7,5.1,1.9,Iris-virginica']
['7.1,3.0,5.9,2.1,Iris-virginica']
['6.3,2.9,5.6,1.8,Iris-virginica']
['6.5,3.0,5.8,2.2,Iris-virginica']
['7.6,3.0,6.6,2.1,Iris-virginica']
['4.9,2.5,4.5,1.7,Iris-virginica']
['7.3,2.9,6.3,1.8,Iris-virginica']
['6.7,2.5,5.8,1.8,Iris-virginica']
['7.2,3.6,6.1,2.5,Iris-virginica']
['6.5,3.2,5.1,2.0,Iris-virginica']
['6.4,2.7,5.3,1.9,Iris-virginica']
['6.8,3.0,5.5,2.1,Iris-virginica']
['5.7,2.5,5.0,2.0,Iris-virginica']
['5.8,2.8,5.1,2.4,Iris-virginica']
['6.4,3.2,5.3,2.3,Iris-virginica']
['6.5,3.0,5.5,1.8,Iris-virginica']
['7.7,3.8,6.7,2.2,Iris-virginica']
['7.7,2.6,6.9,2.3,Iris-virginica']
['6.0,2.2,5.0,1.5,Iris-virginica']
['6.9,3.2,5.7,2.3,Iris-virginica']
['5.6,2.8,4.9,2.0,Iris-virginica']
['7.7,2.8,6.7,2.0,Iris-virginica']
['6.3,2.7,4.9,1.8,Iris-virginica']
['6.7,3.3,5.7,2.1,Iris-virginica']
['7.2,3.2,6.0,1.8,Iris-virginica']
['6.2,2.8,4.8,1.8,Iris-virginica']
['6.1,3.0,4.9,1.8,Iris-virginica']
['6.4,2.8,5.6,2.1,Iris-virginica']
['7.2,3.0,5.8,1.6,Iris-virginica']
['7.4,2.8,6.1,1.9,Iris-virginica']
['7.9,3.8,6.4,2.0,Iris-virginica']
['6.4,2.8,5.6,2.2,Iris-virginica']
['6.3,2.8,5.1,1.5,Iris-virginica']
['6.1,2.6,5.6,1.4,Iris-virginica']
['7.7,3.0,6.1,2.3,Iris-virginica']
['6.3,3.4,5.6,2.4,Iris-virginica']
['6.4,3.1,5.5,1.8,Iris-virginica']
['6.0,3.0,4.8,1.8,Iris-virginica']
['6.9,3.1,5.4,2.1,Iris-virginica']
['6.7,3.1,5.6,2.4,Iris-virginica']
['6.9,3.1,5.1,2.3,Iris-virginica']
['5.8,2.7,5.1,1.9,Iris-virginica']
['6.8,3.2,5.9,2.3,Iris-virginica']
['6.7,3.3,5.7,2.5,Iris-virginica']
['6.7,3.0,5.2,2.3,Iris-virginica']
['6.3,2.5,5.0,1.9,Iris-virginica']
['6.5,3.0,5.2,2.0,Iris-virginica']
['6.2,3.4,5.4,2.3,Iris-virginica']
['5.9,3.0,5.1,1.8,Iris-virginic']
>>> 
============= RESTART: C:/python/Python37-32/day13/iris_print.py =============
[['5.1,3.5,1.4,0.2,Iris-setosa'], ['4.9,3.0,1.4,0.2,Iris-setosa'], ['4.7,3.2,1.3,0.2,Iris-setosa'], ['4.6,3.1,1.5,0.2,Iris-setosa'], ['5.0,3.6,1.4,0.2,Iris-setosa'], ['5.4,3.9,1.7,0.4,Iris-setosa'], ['4.6,3.4,1.4,0.3,Iris-setosa'], ['5.0,3.4,1.5,0.2,Iris-setosa'], ['4.4,2.9,1.4,0.2,Iris-setosa'], ['4.9,3.1,1.5,0.1,Iris-setosa'], ['5.4,3.7,1.5,0.2,Iris-setosa'], ['4.8,3.4,1.6,0.2,Iris-setosa'], ['4.8,3.0,1.4,0.1,Iris-setosa'], ['4.3,3.0,1.1,0.1,Iris-setosa'], ['5.8,4.0,1.2,0.2,Iris-setosa'], ['5.7,4.4,1.5,0.4,Iris-setosa'], ['5.4,3.9,1.3,0.4,Iris-setosa'], ['5.1,3.5,1.4,0.3,Iris-setosa'], ['5.7,3.8,1.7,0.3,Iris-setosa'], ['5.1,3.8,1.5,0.3,Iris-setosa'], ['5.4,3.4,1.7,0.2,Iris-setosa'], ['5.1,3.7,1.5,0.4,Iris-setosa'], ['4.6,3.6,1.0,0.2,Iris-setosa'], ['5.1,3.3,1.7,0.5,Iris-setosa'], ['4.8,3.4,1.9,0.2,Iris-setosa'], ['5.0,3.0,1.6,0.2,Iris-setosa'], ['5.0,3.4,1.6,0.4,Iris-setosa'], ['5.2,3.5,1.5,0.2,Iris-setosa'], ['5.2,3.4,1.4,0.2,Iris-setosa'], ['4.7,3.2,1.6,0.2,Iris-setosa'], ['4.8,3.1,1.6,0.2,Iris-setosa'], ['5.4,3.4,1.5,0.4,Iris-setosa'], ['5.2,4.1,1.5,0.1,Iris-setosa'], ['5.5,4.2,1.4,0.2,Iris-setosa'], ['4.9,3.1,1.5,0.1,Iris-setosa'], ['5.0,3.2,1.2,0.2,Iris-setosa'], ['5.5,3.5,1.3,0.2,Iris-setosa'], ['4.9,3.1,1.5,0.1,Iris-setosa'], ['4.4,3.0,1.3,0.2,Iris-setosa'], ['5.1,3.4,1.5,0.2,Iris-setosa'], ['5.0,3.5,1.3,0.3,Iris-setosa'], ['4.5,2.3,1.3,0.3,Iris-setosa'], ['4.4,3.2,1.3,0.2,Iris-setosa'], ['5.0,3.5,1.6,0.6,Iris-setosa'], ['5.1,3.8,1.9,0.4,Iris-setosa'], ['4.8,3.0,1.4,0.3,Iris-setosa'], ['5.1,3.8,1.6,0.2,Iris-setosa'], ['4.6,3.2,1.4,0.2,Iris-setosa'], ['5.3,3.7,1.5,0.2,Iris-setosa'], ['5.0,3.3,1.4,0.2,Iris-setosa'], ['7.0,3.2,4.7,1.4,Iris-versicolor'], ['6.4,3.2,4.5,1.5,Iris-versicolor'], ['6.9,3.1,4.9,1.5,Iris-versicolor'], ['5.5,2.3,4.0,1.3,Iris-versicolor'], ['6.5,2.8,4.6,1.5,Iris-versicolor'], ['5.7,2.8,4.5,1.3,Iris-versicolor'], ['6.3,3.3,4.7,1.6,Iris-versicolor'], ['4.9,2.4,3.3,1.0,Iris-versicolor'], ['6.6,2.9,4.6,1.3,Iris-versicolor'], ['5.2,2.7,3.9,1.4,Iris-versicolor'], ['5.0,2.0,3.5,1.0,Iris-versicolor'], ['5.9,3.0,4.2,1.5,Iris-versicolor'], ['6.0,2.2,4.0,1.0,Iris-versicolor'], ['6.1,2.9,4.7,1.4,Iris-versicolor'], ['5.6,2.9,3.6,1.3,Iris-versicolor'], ['6.7,3.1,4.4,1.4,Iris-versicolor'], ['5.6,3.0,4.5,1.5,Iris-versicolor'], ['5.8,2.7,4.1,1.0,Iris-versicolor'], ['6.2,2.2,4.5,1.5,Iris-versicolor'], ['5.6,2.5,3.9,1.1,Iris-versicolor'], ['5.9,3.2,4.8,1.8,Iris-versicolor'], ['6.1,2.8,4.0,1.3,Iris-versicolor'], ['6.3,2.5,4.9,1.5,Iris-versicolor'], ['6.1,2.8,4.7,1.2,Iris-versicolor'], ['6.4,2.9,4.3,1.3,Iris-versicolor'], ['6.6,3.0,4.4,1.4,Iris-versicolor'], ['6.8,2.8,4.8,1.4,Iris-versicolor'], ['6.7,3.0,5.0,1.7,Iris-versicolor'], ['6.0,2.9,4.5,1.5,Iris-versicolor'], ['5.7,2.6,3.5,1.0,Iris-versicolor'], ['5.5,2.4,3.8,1.1,Iris-versicolor'], ['5.5,2.4,3.7,1.0,Iris-versicolor'], ['5.8,2.7,3.9,1.2,Iris-versicolor'], ['6.0,2.7,5.1,1.6,Iris-versicolor'], ['5.4,3.0,4.5,1.5,Iris-versicolor'], ['6.0,3.4,4.5,1.6,Iris-versicolor'], ['6.7,3.1,4.7,1.5,Iris-versicolor'], ['6.3,2.3,4.4,1.3,Iris-versicolor'], ['5.6,3.0,4.1,1.3,Iris-versicolor'], ['5.5,2.5,4.0,1.3,Iris-versicolor'], ['5.5,2.6,4.4,1.2,Iris-versicolor'], ['6.1,3.0,4.6,1.4,Iris-versicolor'], ['5.8,2.6,4.0,1.2,Iris-versicolor'], ['5.0,2.3,3.3,1.0,Iris-versicolor'], ['5.6,2.7,4.2,1.3,Iris-versicolor'], ['5.7,3.0,4.2,1.2,Iris-versicolor'], ['5.7,2.9,4.2,1.3,Iris-versicolor'], ['6.2,2.9,4.3,1.3,Iris-versicolor'], ['5.1,2.5,3.0,1.1,Iris-versicolor'], ['5.7,2.8,4.1,1.3,Iris-versicolor'], ['6.3,3.3,6.0,2.5,Iris-virginica'], ['5.8,2.7,5.1,1.9,Iris-virginica'], ['7.1,3.0,5.9,2.1,Iris-virginica'], ['6.3,2.9,5.6,1.8,Iris-virginica'], ['6.5,3.0,5.8,2.2,Iris-virginica'], ['7.6,3.0,6.6,2.1,Iris-virginica'], ['4.9,2.5,4.5,1.7,Iris-virginica'], ['7.3,2.9,6.3,1.8,Iris-virginica'], ['6.7,2.5,5.8,1.8,Iris-virginica'], ['7.2,3.6,6.1,2.5,Iris-virginica'], ['6.5,3.2,5.1,2.0,Iris-virginica'], ['6.4,2.7,5.3,1.9,Iris-virginica'], ['6.8,3.0,5.5,2.1,Iris-virginica'], ['5.7,2.5,5.0,2.0,Iris-virginica'], ['5.8,2.8,5.1,2.4,Iris-virginica'], ['6.4,3.2,5.3,2.3,Iris-virginica'], ['6.5,3.0,5.5,1.8,Iris-virginica'], ['7.7,3.8,6.7,2.2,Iris-virginica'], ['7.7,2.6,6.9,2.3,Iris-virginica'], ['6.0,2.2,5.0,1.5,Iris-virginica'], ['6.9,3.2,5.7,2.3,Iris-virginica'], ['5.6,2.8,4.9,2.0,Iris-virginica'], ['7.7,2.8,6.7,2.0,Iris-virginica'], ['6.3,2.7,4.9,1.8,Iris-virginica'], ['6.7,3.3,5.7,2.1,Iris-virginica'], ['7.2,3.2,6.0,1.8,Iris-virginica'], ['6.2,2.8,4.8,1.8,Iris-virginica'], ['6.1,3.0,4.9,1.8,Iris-virginica'], ['6.4,2.8,5.6,2.1,Iris-virginica'], ['7.2,3.0,5.8,1.6,Iris-virginica'], ['7.4,2.8,6.1,1.9,Iris-virginica'], ['7.9,3.8,6.4,2.0,Iris-virginica'], ['6.4,2.8,5.6,2.2,Iris-virginica'], ['6.3,2.8,5.1,1.5,Iris-virginica'], ['6.1,2.6,5.6,1.4,Iris-virginica'], ['7.7,3.0,6.1,2.3,Iris-virginica'], ['6.3,3.4,5.6,2.4,Iris-virginica'], ['6.4,3.1,5.5,1.8,Iris-virginica'], ['6.0,3.0,4.8,1.8,Iris-virginica'], ['6.9,3.1,5.4,2.1,Iris-virginica'], ['6.7,3.1,5.6,2.4,Iris-virginica'], ['6.9,3.1,5.1,2.3,Iris-virginica'], ['5.8,2.7,5.1,1.9,Iris-virginica'], ['6.8,3.2,5.9,2.3,Iris-virginica'], ['6.7,3.3,5.7,2.5,Iris-virginica'], ['6.7,3.0,5.2,2.3,Iris-virginica'], ['6.3,2.5,5.0,1.9,Iris-virginica'], ['6.5,3.0,5.2,2.0,Iris-virginica'], ['6.2,3.4,5.4,2.3,Iris-virginica'], ['5.9,3.0,5.1,1.8,Iris-virginic']]
>>> 
============= RESTART: C:/python/Python37-32/day13/iris_print.py =============
data1: 121
data2: 29
>>> 
============= RESTART: C:/python/Python37-32/day13/iris_print.py =============
data1: 123
data2: 27
>>> training_data[0]
['4.9,3.0,1.4,0.2,Iris-setosa']
>>> 
