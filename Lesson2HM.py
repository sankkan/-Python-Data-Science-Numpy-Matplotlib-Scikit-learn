#!/usr/bin/env python
# coding: utf-8

# Задание 1
# 
# Импортируйте библиотеку Numpy и дайте ей псевдоним np.
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это признак, а строка - наблюдение. Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.
# 

# In[1]:


import numpy as np


# In[10]:


a = np.array([[1, 2, 3, 3, 1],
              [6, 8, 11, 10, 7]]).transpose()
a


# In[13]:


mean_a = np.mean(a, axis = 0)
mean_a


# Задание 2
# 
# Вычислите массив a_centered, отняв от значений массива а средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.
# 

# In[15]:


a_centered = a - mean_a
a_centered


# Задание 3
# 
# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.
# 

# In[18]:


a_centered_sp = a_centered.T[0] @ a_centered.T[1]


# In[21]:


a_centered_sp / (5-1)


# Задание 4**
# 
# Число, которое мы получили в конце задания 3 является ковариацией двух признаков, содержащихся в массиве а. В задании 4 мы делили сумму произведений центрированных признаков на N-1, а не на N, поэтому полученная нами величина является несмещенной оценкой ковариации. В этом задании проверьте получившееся число, вычислив ковариацию еще одним способом - с помощью функции np.cov. В качестве аргумента m функция np.cov должна принимать транспонированный массив a. В получившейся ковариационной матрице (массив Numpy размером 2x2) искомое значение ковариации будет равно элементу в строке с индексом 0 и столбце с индексом 1.

# In[23]:


np.cov(a.T)[0, 1]


# Pandas
# 
# Задание 1
# 
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].
# 

# In[24]:


import pandas as pd


# In[33]:


author = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']}
                      , columns = ['author_id','author_name'])
author


# In[32]:


book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price':[450, 300, 350, 500, 450, 370, 290]},
                    columns = ['author_id','book_title','price'])
book


# Задание 2
# 
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

# In[40]:


authors_price = pd.merge(author, book, on = 'author_id', how = 'outer')
authors_price


# Задание 3
# 
# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

# In[43]:


top5 = authors_price.nlargest(5, 'price')

top5


# Задание 4
# 
# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.
# 

# In[47]:


authors_stat = authors_price['author_name'].value_counts()
authors_stat


# In[61]:


authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
authors_stat


# In[ ]:




 
