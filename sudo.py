# Output on monitor as matrix.

def pr_vid_sudo (sud3_list):
    for i in range(9):
       print(format(sud3_list[i * 9:i * 9 + 9]))

# Output on monitor intermediate solution.
       
def pr_vid_dic (elem_dic_1,sud3_list ):
    print("HELLO!")
    for k in range (9):
        pr_str = ""
        for i in range(9):
             
             if  sud3_list[k * 9 + i] == 0:
                 pr_str = pr_str + (str(elem_dic_1[k * 9 + i]).replace(',','')).ljust(11)
                 
             else:
                 pr_str = pr_str + (str(sud3_list[k * 9 + i])).ljust(11)

        print(pr_str)
        
        
"""Процедура инспектирует квадраты на наличие скрытых наборов из двух элементов и если находит их корректирует набор в 
#квадрате и/либо в строке/солбце в зависимостиот расположения этого скрытого набора"""

""" Function inspect squares on hidden sets from 2 elements and if find it,make correcting set in
    square and/ or row/column depend on posion of this hidden sets  """          
        
        
        
def alg_hid_set_in_squ (elem_dic_1,sud3_list) :
    
# Проверяет элемент на количество вхождений в строку  и если равно 2 то возвращает TRUE.

# Inspect digit on numbers input in row. If numbers  equals  2, then return TRUE. 
    
    def ins_l_in_row(nom_el,dig_l):
        dat = False
        num_dat = 0
        for i in range(9):
            if sud3_list[ int(nom_el / 9) * 9 + i] == 0:
                if elem_dic_1[int(nom_el / 9) * 9 + i].issuperset(dig_l):
                    num_dat += 1
        if num_dat == 2:
            dat=True
        return dat       
    
# Проверяет элемент на количество вхождений в колонку  и если равно 2 то возвращает TRUE.

# Inspect digit on numbers input in column. If numbers  equals  2, then return TRUE. 
    def ins_l_in_col(nom_el,dig_l):
        dat = False
        num_dat = 0
        n_col= int(nom_el % 9)
        for i in range(0,81,9):
            if sud3_list[ n_col + i] == 0:
                if elem_dic_1[n_col + i].issuperset(dig_l):
                    num_dat += 1
                   
        if num_dat == 2:
            dat = True
           
        return dat                        

    sq_set={0,3,6,27,30,33,54,57,60}
    for key_sq in sq_set:
        
        num_dict = dict()
        
        for l in range(9):
            l += 1
            l_set = {l}
            num_set = set()
            for i in range(0,27,9):
                for j in range(3):
                    if sud3_list[key_sq + i + j] == 0:
                        if elem_dic_1[key_sq + i + j].issuperset(l_set):
                            num_set.add(key_sq + i + j)

            num_dict[l] = num_set
        for key_l in num_dict.keys():
            elem_list=list(num_dict[key_l])
            elem_list.sort()
            num_set_1 = set()
            num_set_2 = set()
            
            if len(elem_list) == 2:
                num_set_1 = elem_dic_1[int(elem_list[0])]
                num_set_2 = elem_dic_1[int(elem_list[1])]
                 
# Проверяем какой из наборов имеет длину в два элемента                   

# Inspect set on length 2 
                
                if  len(num_set_1) == 2: 
                    if num_set_2.issuperset(num_set_1):
                        if   (int(elem_list[1] / 9) == int(elem_list[0] / 9)) and ins_l_in_row(elem_list[1],{key_l}) :
                            n_row =int(elem_list[0] / 9)
                            for k in range(9):
                                if sud3_list[n_row * 9 + k] == 0 and not(n_row * 9 + k in elem_list) and sud3_list[n_row * 9:n_row * 9 + 9].count(0) > 2:
                                    elem_dic_1[n_row * 9 + k]=elem_dic_1[n_row * 9 + k] - num_set_1
                                   
                        if   elem_list[1] == elem_list[0]+9 and ins_l_in_col(elem_list[1],{key_l}) :
                            n_col = int(elem_list[1] % 9)
                            for k in range(0,81,9):
                                if sud3_list[n_col + k] == 0 and   not(n_col + k in elem_list) and sud3_list[n_col:n_col + 81:9].count(0) > 2:
                                    elem_dic_1[n_col + k] = elem_dic_1[n_col + k] - num_set_1  
                elif  len(num_set_2) == 2: 
                    if num_set_1.issuperset(num_set_2):
                        elem_dic_1[elem_list[0]] = num_set_2
                        elem_dic_1[elem_list[1]] = num_set_2
                        if   (int(elem_list[1] / 9) == int(elem_list[0] / 9)) and ins_l_in_row(elem_list[1],{key_l}):
                            n_row =int(elem_list[0] / 9)
                            for k in range(9):
                                if sud3_list[n_row * 9 + k] == 0 and   not(n_row * 9 + k in elem_list)  and sud3_list[n_row * 9:n_row * 9 + 9].count(0) > 2: 
                                
                                    
                                    elem_dic_1[n_row * 9 + k]=elem_dic_1[n_row * 9 + k] - num_set_2
                                    
                        if   elem_list[1] == elem_list[0] + 9  and ins_l_in_col(elem_list[1],{key_l}):
                            n_col = int(elem_list[1] % 9)
                            for k in range(0,81,9):
                                if sud3_list[n_col + k] == 0 and not(n_col + k in elem_list)  and sud3_list[n_col:n_col + 81:9].count(0) > 2:
                                    elem_dic_1[n_col + k] = elem_dic_1[n_col + k] - num_set_2             
       
    return  elem_dic_1                               



"""Данная процедура определяет те цифры которые встречаются в квадрате только два разаи если их положение в
   одинаковое ,то этим двум положениям присаивает набор из двух элементов."""        
""" This function determinate 2 digit that in square only two times.
    And if this two digit in the same rows/columns,them determinate assign meaning."""         

def ins_two_eguel_set_in_squ (elem_dic_1,sud3_list) :


    sq_set={0,3,6,27,30,33,54,57,60}
    for key_sq in sq_set:
        
        num_dict = dict()
        
        for l in range(9):
            l += 1
            l_set = {l}
            num_set = set()
            for i in range(0,27,9):
                for j in range(3):
                    if sud3_list[key_sq + i + j] == 0:
                        if elem_dic_1[key_sq + i + j].issuperset(l_set):
                            num_set.add(key_sq + i + j)
            if len(num_set) == 2:
                num_dict[l] = num_set
        num_set_1 = set()
        num_set_2 = set() 
        elem_set = set()
               
        if len(num_dict) == 2:
            for key in num_dict:
                num_set_2 = num_set_1
                elem_set.add(key)
                num_set_1 = num_dict[key]
            if num_set_1 == num_set_2:
                elem_dic_1[num_set_2.pop()] = elem_set
                elem_dic_1[num_set_2.pop()] = elem_set
                            
    return  elem_dic_1                               

# Функция проверяет вхождение в каждой цифры в строку и если оно одно то заполняет этот элемент и 
# корректирует словарь
""" functin inspect entry each digit in row and if it is one set this digit"""


def ins_one_elem__in_row (elem_dic_1,sud3_list) :
    global  COUNTER
    COUNTER = 0
    pr_vid_dic (elem_dic_1,sud3_list )
    for key_row in range(9):
        for i in range(9):
            ind_set = set()
            i += 1
            dig_set = {i}
            for key_col in range(9):
                n_elem =  key_row * 9 + key_col
                if  n_elem in list(elem_dic_1.keys()):
                    if elem_dic_1[n_elem].issuperset(dig_set):
                        ind_set.add(n_elem)
            if len(ind_set) == 1 and not(i in sud3_list[key_row * 9:key_row * 9 + 9]):
                 sud3_list[(list(ind_set)[0])] = i
                 del elem_dic_1[(list(ind_set)[0])]
                 COUNTER += 1

    return  elem_dic_1,sud3_list            

       
       
# Функция проверяет вхождение в каждой цифры в в колонке и если оно одно то заполняет этот элемент и 
# корректирует словарь
""" functin inspect entry each digit in column and if it is one set this digit"""

def ins_one_elem__in_col (elem_dic_1,sud3_list) :
    global  COUNTER
    COUNTER = 0
    pr_vid_dic (elem_dic_1,sud3_list)
    for key_row in range(9):
        for i in range(9):
            ind_set = set()
            i += 1
            dig_set = {i}
            
            for key_col in range(9):
                n_elem=  key_row + key_col * 9
                if  n_elem in list(elem_dic_1.keys()):
                    if elem_dic_1[n_elem].issuperset(dig_set):
                        ind_set.add(n_elem)
                        
            if len(ind_set)==1 and not(i in sud3_list[key_row:key_row + 81:9]) :
                sud3_list[list(ind_set)[0]] = i              
                del elem_dic_1[list(ind_set)[0]]
                COUNTER += 1
               
    return  elem_dic_1,sud3_list             
             


# Проверяет  колонку что цифра может быть только в этой колонку и корректирует словарь 
""" functin inspect of sets elements on entry each digit in column   and if it is one set this digit"""

def ins_one_col (elem_dic_1):
 
    sq_set = {0,3,6,27,30,33,54,57,60}
    for key in sq_set:
        
        for i in range (9):
            i += 1
            b_col_1 = False
            b_col_2 = False
            b_col_3 = False
            dig_set = {i}
            for j in range(0,27,9):
                if key+j in list(elem_dic_1.keys()):
                  b_col_1 = b_col_1 or dig_set.issubset(elem_dic_1[key + j])
                if key+j+1  in list(elem_dic_1.keys()):
                  b_col_2 = b_col_2 or dig_set.issubset(elem_dic_1[key + j + 1])
                if key+j+2  in list(elem_dic_1.keys()):
                  b_col_3 = b_col_3 or dig_set.issubset(elem_dic_1[key + j + 2])
                  
            if b_col_1 == True and b_col_2 == False and b_col_3 == False:
                if key == 0 or key == 3 or key == 6:
                    for z in range(27,81,9):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z]=elem_dic_1[key + z] - dig_set
                elif key == 27 or key == 30 or key == 33:
                    for z in range( 0,27,9):
                        if key - 27 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 27 + z]=elem_dic_1[key - 27 + z] - dig_set
                    for z in range(54,81,9):
                        if key - 27 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 27 + z] = elem_dic_1[key - 27 + z] - dig_set
                elif key == 54 or key == 57 or key == 60:
                    for z in range(0,54,9):
                        if key -54 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 54 + z]=elem_dic_1[key - 54 + z] - dig_set
                                
            if b_col_1 ==  False and b_col_2 == True and b_col_3 == False:
                if key == 0 or key == 3 or key == 6:
                    for z in range(28,82,9):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z] = elem_dic_1[key + z] - dig_set
                elif key == 27 or key == 30 or key == 33:
                    for z in range(1,28,9):
                        if key - 27 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 27 + z] = elem_dic_1[key - 27 + z] - dig_set
                    for z in range(55,82,9):
                        if key- 27 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 27 + z] = elem_dic_1[key - 27 + z] - dig_set
                elif key == 54 or key == 57 or key == 60:
                    for z in range(1,55,9):
                        if key  -54 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 54 + z] = elem_dic_1[key - 54 + z] - dig_set

            if b_col_1 == False and b_col_2 == False and b_col_3 == True:
                if key == 0 or key == 3 or key == 6:
                    for z in range(29,83,9):
                        if key + z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z] = elem_dic_1[key + z] - dig_set
                elif key == 27 or key == 30 or key == 33:
                    for z in range(2,29,9):
                        if key - 27 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 27 + z] = elem_dic_1[key - 27 + z] - dig_set
                    for z in range(56,83,9):
                        if key - 27 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key-27+z] = elem_dic_1[key-27+z] - dig_set
                elif key == 54 or key == 57 or key == 60:
                    for z in range(2,56,9):
                        if key - 54 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 54 + z] = elem_dic_1[key - 54 + z] - dig_set

    return elem_dic_1



# Проверяет  строку что цифра может быть только в этой строке и корректирует словарь 
""" functin inspect of sets elements on entry each digit in row   and if it is one set this digit"""

def ins_one_row (elem_dic_1):
    sq_set={0,3,6,27,30,33,54,57,60}
    for key in sq_set:
        for i in range (9):
            i += 1
            b_row_1 = False
            b_row_2 = False
            b_row_3 = False
            dig_set = {i}
            for j in range(3):
                if key+j in list(elem_dic_1.keys()):
                  b_row_1 = b_row_1 or dig_set.issubset(elem_dic_1[key + j])
                if key+j + 9  in list(elem_dic_1.keys()):
                  b_row_2 = b_row_2 or dig_set.issubset(elem_dic_1[key + j + 9])
                if key+j + 18  in list(elem_dic_1.keys()):
                  b_row_3 = b_row_3 or dig_set.issubset(elem_dic_1[key + j + 18])

            if b_row_1 == True and b_row_2 == False and b_row_3 == False:
                if key == 0 or key == 27 or key == 54 :
                    for z in range(3,9):
                        if key + z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z]=elem_dic_1[key + z] - dig_set
                elif key == 3 or key == 30 or key == 57:
                    for z in range(-3,0):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z] = elem_dic_1[key + z] - dig_set
                    for z in range(3,6):
                        if key - 27 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 27 + z] = elem_dic_1[key - 27 + z] - dig_set
                elif key == 6 or key == 33 or key == 60:
                    for z in range(-6,0):
                        if key + z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z] = elem_dic_1[key + z] - dig_set

            if b_row_1 ==  False and b_row_2 == True and b_row_3 == False:
                if key == 0 or key == 27 or key == 54:
                    for z in range(12,18):
                        if key + z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z] = elem_dic_1[key + z] - dig_set
                elif key == 3 or key == 30 or key == 57:
                    for z in range(6,9):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z] = elem_dic_1[key + z] - dig_set
                    for z in range(12,15):
                        if key + z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z] = elem_dic_1[key + z] - dig_set
                elif key == 6 or key == 33 or key == 60:
                    for z in range(3,9):
                        if key + z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z] = elem_dic_1[key + z] - dig_set

            if b_row_1 == False and b_row_2 == False and b_row_3 == True:
                if key == 0 or key == 27 or key == 54:
                    for z in range(21,27):
                        if key + z in list(elem_dic_1.keys()):
                            elem_dic_1[key + z] = elem_dic_1[key + z] - dig_set
                elif key == 3 or key == 30 or key == 57:
                    for z in range(15,18):
                        if key - 27 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 27 + z] = elem_dic_1[key - 27 + z] - dig_set
                    for z in range(21,24):
                        if key - 27 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 27 + z] = elem_dic_1[key - 27 + z] - dig_set
                elif key == 6 or key == 33 or key == 60:
                    for z in range(12,18):
                        if key - 54 + z in list(elem_dic_1.keys()):
                            elem_dic_1[key - 54 + z] = elem_dic_1[key - 54 + z] - dig_set

    return elem_dic_1


# Проверяет наличие одного элемента в сете по всем эдементам и заменяет его в листе   
""" If in set only 1 element, in this position write digit.
    The search go for all set of elements"""

def ins_one_elem (elem_dic_1,sud3_list) :
    global  COUNTER 
    COUNTER = 0
    for key in range(81):
        if sud3_list[key] == 0 and len(elem_dic_1[key]) == 1:
            sud3_list[key]= (elem_dic_1[key]).pop()
            del elem_dic_1[key]
            COUNTER += 1
            
    return  elem_dic_1, sud3_list             

# В данном модуле идет формирование набора возможных элементов для пустых значений. 
""" In this part makes set of digits for all empty elements""" 


def  make_dict(elem_dic_1,sud3_list) :
    test_set=set(i for i in range (10))
    for i in range(81):
        if  sud3_list[i]==0:
            n_row = int(i / 27)
            n_col = int((i % 9) / 3)
            sud_set_sq_1 = set(sud3_list[(n_row * 27) + (n_col * 3):(n_row * 27) + (n_col * 3) + 3]) 
            sud_set_sq_2 = set(sud3_list[(n_row * 27) + (n_col * 3) + 9:(n_row * 27) + (n_col * 3) + 9 + 3])
            sud_set_sq_3 = set(sud3_list[(n_row * 27) + (n_col * 3)+18:(n_row * 27) + (n_col * 3) + 18 + 3])
            sud_set_sq = sud_set_sq_1 | sud_set_sq_2 | sud_set_sq_3
            set_row = set(sud3_list[int(i / 9) * 9:int(i / 9) * 9 + 9])
            set_col = set( sud3_list[(int(i % 9))::9])
            set_elem = test_set - sud_set_sq - set_row -set_col
            elem_dic_1[i] = set_elem

    return elem_dic_1




# Этот блок проверяет квадраты наналичие не повторяюшихся цифр во множестве слоаря
# и переписывает соответствующий элемент в список.
""" It go inspect of squares of elements (9 pieces) on non-repeated.
    And if  find it, replace digit as the value."""  
      
def insp_squ(elem_dic_1,sud3_list):
    global  COUNTER
    COUNTER = 0
    for i in range(81):
        n_row = int(i / 27)
        n_col = int((i % 9) / 3)
        squ = set()
        if  sud3_list[i] == 0:
            squ1 = set()
            for c_row in range(3):
                for c_col in range(3):
                    n_elem = int((n_row * 27 + c_row * 9) + (n_col * 3 + c_col))
                    if n_elem in elem_dic_1.keys() and n_elem != i:
                        squ1= squ1|elem_dic_1[n_elem]
            squ = elem_dic_1[i] - squ1
            if len (squ) == 1:
                sud3_list[i] = squ.pop()
                del elem_dic_1[i]
                COUNTER += 1
  
    return  elem_dic_1,sud3_list              
 


        
# Read from file sudoku in list integer.

def read_from_file():

    with open('exsud.txt', 'r') as f:
        sud_list = f.read().split(' ')

    sud1_list = sud_list[0].replace('\n','') # Made list , delete non writeable symbol and list wiht intenger elements.     
    sud0_list = list(map(int, sud1_list[:]))
    sud02_list = list(map(int, sud1_list[:]))
    
    return  sud02_list

def main():
    sud2_list = read_from_file()
    sud0_list = sud2_list
    print ("\n\n\n FIRST")
    pr_vid_sudo (sud2_list)
    elem_dic = {} # Create dictionary where key - namber element, value set of posible digit.
    global  COUNTER
    make_dict(elem_dic,sud2_list)
    pr_vid_dic (elem_dic,sud2_list )
    print(len(elem_dic),sud2_list.count(0))


    g_counter = 0


    while sud2_list.count(0) != 0 and g_counter < 5:
        g_counter += 1
        print("g_counter==",g_counter)
        COUNTER = 1
        while COUNTER != 0  : 
            
            while COUNTER != 0:
                ins_one_elem (elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
                
            insp_squ(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
            while COUNTER != 0:
                ins_one_elem (elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
            
            ins_one_elem__in_col (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
            while COUNTER != 0:
                ins_one_elem (elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
            
            ins_one_elem__in_row (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            
            while COUNTER != 0:
                ins_one_elem (elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
    
        COUNTER = 1    
        while COUNTER != 0:
    
            for _  in  range(3):
                ins_one_col (elem_dic)
                ins_one_elem__in_row (elem_dic,sud2_list)

            COUNTER = 1 
            while COUNTER != 0:
                ins_one_elem (elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
    
        
        
        COUNTER = 1 
        while COUNTER != 0: 

            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
   
            insp_squ(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
        
            ins_one_elem__in_col(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
        
            ins_one_elem__in_row(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)

        COUNTER = 1    
        while COUNTER != 0:
            for _  in  range(3):
                ins_one_row (elem_dic)
                ins_one_elem__in_col(elem_dic,sud2_list)
    
        COUNTER = 1 
        while COUNTER != 0:
            ins_one_elem(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
    
        
        COUNTER=1
        while COUNTER != 0: 
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
   
            insp_squ(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
        
            ins_one_elem__in_col(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
        
            ins_one_elem__in_row(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
      
        COUNTER = 1    
        while COUNTER != 0:
            COUNTER = 1    
            for _  in  range(3):
                ins_one_col(elem_dic)
                ins_one_row(elem_dic)
                ins_two_eguel_set_in_squ(elem_dic,sud2_list)
       
            pr_vid_dic(elem_dic,sud2_list )
            ins_one_elem__in_row(elem_dic,sud2_list)
            ins_one_elem__in_col(elem_dic,sud2_list)
    
            COUNTER = 1 
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
        
        COUNTER = 1
        while COUNTER != 0  : 
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
       
            insp_squ(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
            
            ins_one_elem__in_col(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
             
            ins_one_elem__in_row(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
    
        alg_hid_set_in_squ(elem_dic,sud2_list)
        print("COUNTER_161", COUNTER)
        pr_vid_dic(elem_dic,sud2_list )
        COUNTER = 1
        while COUNTER != 0:
            ins_one_elem(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
       
        insp_squ(elem_dic,sud2_list)
        ins_one_elem__in_row(elem_dic,sud2_list)
        ins_one_elem__in_col(elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        
        COUNTER = 1
        while COUNTER != 0:
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
       
            insp_squ(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
            
            
            ins_one_elem__in_col(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
             
            ins_one_elem__in_row(elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
            while COUNTER != 0:
                ins_one_elem(elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
                
    if g_counter >= 5:
        print('Something went wrong')
        pr_vid_dic (elem_dic,sud2_list)
        print('Inpect, is input correct?')
        pr_vid_sudo (sud0_list)
        print(len(elem_dic),sud2_list.count(0))
            
    else:     
        pr_vid_sudo (sud2_list)
        print(len(elem_dic),sud2_list.count(0))


    return 


if __name__ == "__main__":
    main()

                     
