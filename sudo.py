#вывод на печать в в виде матрицы
def pr_vid_sudo (sud3_list):
    for i in range(9):
       print("\033[31m {}".format( sud3_list[i*9:i*9+9]))


       
def pr_vid_dic (elem_dic_1,sud3_list ):
    print("HELLO!")
    for k in range (9):
        pr_str=""
        for i in range(9):
             
             if  sud3_list[k*9+i] == 0:
                 pr_str =pr_str + (str(elem_dic_1[k*9+i]).replace(',','')).ljust(11)
                 
             else:
                 pr_str =pr_str + (str(sud3_list[k*9+i])).ljust(11)

        print(pr_str)
        
        
#процедура инспектирует квадраты на наличие скрытых наборов из двух элементов и если находит их корректирует набор в 
#квадрате и/либо в строке/солбце в зависимостиот расположения этого скрытого набора          
        
        
        
def alg_hid_set_in_squ (elem_dic_1,sud3_list) :
    
#проверяет элемент на количество вхождений в строку  и если равно 2 то возвращает TRUE    
    def ins_l_in_row(nom_el,dig_l):
        dat= False
        num_dat=0
        for i in range(9):
            if sud3_list[ int(nom_el/9)*9 +i] ==0:
                if elem_dic_1[int(nom_el/9)*9 +i].issuperset(dig_l):
                    num_dat+=1
        if num_dat==2:
            dat=True
        return dat       
    
#проверяет элемент на количество вхождений в колонку  и если равно 2 то возвращает TRUE             
    def ins_l_in_col(nom_el,dig_l):
        dat= False
        num_dat=0
        n_col= int(nom_el % 9)
        for i in range(0,81,9):
            if sud3_list[ n_col +i] ==0:
                if elem_dic_1[n_col +i].issuperset(dig_l):
                   
                    
                    num_dat+=1
                   
        if num_dat==2:
            dat=True
           
        return dat                        
                


    sq_set={0,3,6,27,30,33,54,57,60}
    for key_sq in sq_set:
        
        num_dict=dict()
        
        for l in range(9):
            l+=1
            l_set={l}
            num_set=set()
            for i in range(0,27,9):
                for j in range(3):
                    print("COUNTER_201",l,key_sq,i,j,key_sq+i+j,num_set )
                    print("COUNTER_2011", sud3_list[key_sq+i+j])
                    if sud3_list[key_sq+i+j]==0:
#                        print("COUNTER_101",l,key_sq,key_sq+i+j,elem_dic_1[key_sq+i+j],num_set )
#                        print("COUNTER_1011",l,key_sq,key_sq+i+j,elem_dic_1[key_sq+i+j],num_set,l_set,elem_dic_1[key_sq+i+j].issuperset(l_set) )
                        if elem_dic_1[key_sq+i+j].issuperset(l_set):
                            num_set.add(key_sq+i+j)
                            print("COUNTER_202",l,key_sq,key_sq+i+j,elem_dic_1[key_sq+i+j],num_set )
#            print("COUNTER_103",l,key_sq,key_sq+i+j,num_set )   

            num_dict[l]=num_set
        for key_l in num_dict.keys():
            elem_list=list(num_dict[key_l])
            elem_list.sort()
            num_set_1=set()
            num_set_2=set()
            
            if len(elem_list)==2:
                num_set_1 = elem_dic_1[int(elem_list[0])]
                num_set_2 = elem_dic_1[int(elem_list[1])] 
#проверяем какой из наборов имеет длину в два элемента                   
                
                if  len(num_set_1)==2: 
                    if num_set_2.issuperset(num_set_1):
#                        elem_dic_1[elem_list[0]]=num_set_1
#                        elem_dic_1[elem_list[1]]=num_set_1
                        print("COUNTER_203",num_set_1,num_set_2,elem_list,elem_dic_1[elem_list[0]],elem_dic_1[elem_list[1]] )
#меняем элементы в квадрате                        
#                        for i in range(0,27,9):
#                            for j in range(3):
#                                if sud3_list[key_sq+i+j]==0 and not num_dict[key_l].issuperset({key_sq+i+j}):
#                                    
#                                    print("COUNTER_204",key_sq+i+j,num_set_1,num_set_2,elem_list,elem_dic_1[key_sq+i+j] )
#                                    elem_dic_1[key_sq+i+j]=elem_dic_1[key_sq+i+j]-num_set_1
#                                    print("COUNTER_205",key_sq+i+j,num_set_1,num_set_2,elem_list,elem_dic_1[key_sq+i+j] )
#проверем в одной ли строке набор и если да то меняем набор в строке
                        print("COUNTER_2031",key_l,key_sq, elem_list,int(elem_list[1]/9) , int(elem_list[0]/9),(int(elem_list[1]/9) == int(elem_list[0]/9)),ins_l_in_row(elem_list[1],l_set ))
                        print("COUNTER_2032",key_l,key_sq, elem_list,(elem_list[1] == elem_list[0]+9) , ins_l_in_col(elem_list[1],l_set))                            
                        if   (int(elem_list[1]/9) == int(elem_list[0]/9)) and ins_l_in_row(elem_list[1],{key_l}) :
                            n_row =int(elem_list[0]/9)
                            for k in range(9):
                                if sud3_list[n_row*9+k]==0 and   not(n_row*9+k in elem_list)  and sud3_list[n_row*9:n_row*9+9].count(0)>2:
                                    print("COUNTER_2061",n_row,k,n_row*9+k,num_set_1,num_set_2,elem_list ) 
                                    print("COUNTER_206",n_row,num_set_1,num_set_2,elem_list,elem_dic_1[n_row*9+k] ) 
                                    elem_dic_1[n_row*9+k]=elem_dic_1[n_row*9+k]-num_set_1
                                    print("COUNTER_207",n_row,num_set_1,num_set_2,elem_list,elem_dic_1[n_row*9+k] ) 
                                    
#проверем в одном ли столбце набор и если да то меняем набор в столбце
                        print("COUNTER_2071",key_sq ,  elem_list[1], elem_list[0],elem_list[1] == elem_list[0]+9 ) 
                        if   elem_list[1] == elem_list[0]+9 and ins_l_in_col(elem_list[1],{key_l}) :
                                                        
                            
                            n_col =int(elem_list[1]%9)
                                                       
                            for k in range(0,81,9):
                                if sud3_list[n_col+k]==0 and   not(n_col+k in elem_list)  and sud3_list[n_col:n_col+81:9].count(0)>2: 
                                    print("COUNTER_208", n_col ,k,n_col+k,num_set_1,num_set_2,elem_dic_1[n_col+k] )
                                    elem_dic_1[n_col+k]=elem_dic_1[n_col+k]-num_set_1 
                                    print("COUNTER_209", n_col ,k,n_col+k, num_set_1,num_set_2,elem_dic_1[n_col+k] ) 
                                    
                                    
#проверяем какой из наборов имеет длину в два элемента                   
                
                elif  len(num_set_2)==2: 
                    if num_set_1.issuperset(num_set_2):
                        elem_dic_1[elem_list[0]]=num_set_2
                        elem_dic_1[elem_list[1]]=num_set_2
                        print("COUNTER_210",num_set_1,num_set_2,elem_list,elem_dic_1[elem_list[0]],elem_dic_1[elem_list[1]] )
                        print("COUNTER_2033",key_l,key_sq, elem_list,int(elem_list[1]/9) , int(elem_list[0]/9),(int(elem_list[1]/9) == int(elem_list[0]/9)),ins_l_in_row(elem_list[1],l_set ))
                        print("COUNTER_2034",key_l,key_sq, elem_list,(elem_list[1] == elem_list[0]+9) , ins_l_in_col(elem_list[1],l_set))                            
#меняем элементы в квадрате                        
#                        for i in range(0,27,9):
#                            for j in range(3):
#                                if sud3_list[key_sq+i+j]==0 and not num_dict[key_l].issuperset({key_sq+i+j}):
#                                    print("COUNTER_211",key_sq+i+j,num_set_1,num_set_2,elem_list,elem_dic_1[key_sq+i+j] )
#                                    elem_dic_1[key_sq+i+j]=elem_dic_1[key_sq+i+j]-num_set_2
#                                    print("COUNTER_212",key_sq+i+j,num_set_1,num_set_2,elem_list,elem_dic_1[key_sq+i+j] )
#проверем в одной ли строке набор и если да то меняем набор в строке
                        if   (int(elem_list[1]/9) == int(elem_list[0]/9)) and ins_l_in_row(elem_list[1],{key_l}):
                            n_row =int(elem_list[0]/9)
                            for k in range(9):
                                if sud3_list[n_row*9+k]==0 and   not(n_row*9+k in elem_list)  and sud3_list[n_row*9:n_row*9+9].count(0)>2: 
                                
                                    print("COUNTER_213",n_row,num_set_1,num_set_2,elem_list,elem_dic_1[n_row*9+k] ) 
                                    elem_dic_1[n_row*9+k]=elem_dic_1[n_row*9+k]-num_set_2
                                    print("COUNTER_214",n_row,num_set_1,num_set_2,elem_list,elem_dic_1[n_row*9+k] ) 
                                    
#проверем в одном ли столбце набор и если да то меняем набор в столбце

                        if   elem_list[1] == elem_list[0]+9  and ins_l_in_col(elem_list[1],{key_l}):
                            n_col =int(elem_list[1]%9)
                            
                            
                            for k in range(0,81,9):
                                if sud3_list[n_col+k]==0 and   not(n_col+k in elem_list)  and sud3_list[n_col:n_col+81:9].count(0)>2:
                               
                                    print("COUNTER_215", n_col ,num_set_1,num_set_2,elem_dic_1[n_col+k] ) 
                                    elem_dic_1[n_col+k]=elem_dic_1[n_col+k]-num_set_2             
                                    print("COUNTER_216", n_col ,num_set_1,num_set_2,elem_dic_1[n_col+k] )
                                    
                                    
       
    return  elem_dic_1                               



#данная процедураопределяет те цифры которые встречаются в квадрате только два разаи если их положение в
#одинаковое ,то этим двум положениям присаивает набор из двух элементов        
        

def ins_two_eguel_set_in_squ (elem_dic_1,sud3_list) :


    sq_set={0,3,6,27,30,33,54,57,60}
    for key_sq in sq_set:
        
        num_dict=dict()
        
        for l in range(9):
            l+=1
            l_set={l}
            num_set=set()
            for i in range(0,27,9):
                for j in range(3):
                    if sud3_list[key_sq+i+j]==0:
#                        print("COUNTER_101",l,key_sq,key_sq+i+j,elem_dic_1[key_sq+i+j],num_set )
#                        print("COUNTER_1011",l,key_sq,key_sq+i+j,elem_dic_1[key_sq+i+j],num_set,l_set,elem_dic_1[key_sq+i+j].issuperset(l_set) )
                        if elem_dic_1[key_sq+i+j].issuperset(l_set):
                            num_set.add(key_sq+i+j)
#                            print("COUNTER_102",l,key_sq,key_sq+i+j,elem_dic_1[key_sq+i+j],num_set )
#            print("COUNTER_103",l,key_sq,key_sq+i+j,num_set )                
            if len(num_set)==2:
                
                num_dict[l]=num_set
#        print("COUNTER_100",num_dict)
        num_set_1=set()
        num_set_2=set() 
        elem_set=set()
               
        if len( num_dict)==2:
            for key in num_dict:
                num_set_2=num_set_1
                elem_set.add(key)
                num_set_1= num_dict[key]
            if num_set_1==num_set_2:
 #               print("COUNTER_104",key_sq,num_set_2,elem_set ) 
                
                elem_dic_1[num_set_2.pop()]=elem_set
                elem_dic_1[num_set_2.pop()]=elem_set
                            
    return  elem_dic_1                               

        
       
       
#функция проверяет вхождение в каждой цифры в строку и если оно одно то заполняет этот элемент и 
# корректирует словарь
def ins_one_elem__in_row (elem_dic_1,sud3_list) :
    global  counter
    counter=0
#    print("COUNTER_6", counter)
    pr_vid_dic (elem_dic_1,sud3_list )
    for key_row in range(9):
        for i in range(9):
            
            ind_set=set()
            i+=1
            dig_set={i}
            for key_col in range(9):
                n_elem=  key_row*9 +key_col
#ecли в сформированном словаре множество имеет один элемент то списку присваивается значение этого элемента        
                if  n_elem in list(elem_dic_1.keys()):
                    if elem_dic_1[n_elem].issuperset(dig_set):
                        ind_set.add(n_elem)
#            print("COUNTER_62",i,ind_set)            
            if len(ind_set)==1 and  not(i in sud3_list[key_row*9:key_row*9+9]):
                 print("COUNTER_61", i,ind_set,(list(ind_set)[0]),n_elem,not(i in sud3_list[key_row*9:key_row*9+9])   )
                 print (i,sud3_list[key_row*9:key_row*9+9],i in sud3_list[key_row*9:key_row*9+9])
                    

                
#                n_elem = ind_set.pop()
                 sud3_list[(list(ind_set)[0])]=i
                                     
                 del elem_dic_1[(list(ind_set)[0])]
                 counter+=1
#    print("COUNTER_63", counter,sud3_list[10],elem_dic_1[10])           
                
    return  elem_dic_1,sud3_list            

       
       
#функция проверяет вхождение в каждой цифры в в колонке и если оно одно то заполняет этот элемент и 
# корректирует словарь
def ins_one_elem__in_col (elem_dic_1,sud3_list) :
    global  counter
    counter=0
    print("COUNTER_70", counter)
    pr_vid_dic (elem_dic_1,sud3_list )
    for key_row in range(9):
        for i in range(9):
            
            ind_set=set()
            
            
            i+=1
            dig_set={i}
            
            for key_col in range(9):
                n_elem=  key_row + key_col*9
#ecли в сформированном словаре множество имеет один элемент то списку присваивается значение этого элемента        
                if  n_elem in list(elem_dic_1.keys()):
                    if elem_dic_1[n_elem].issuperset(dig_set):
                        ind_set.add(n_elem)
                            
                        
            if len(ind_set)==1 and not(i in sud3_list[key_row:key_row+81:9]) :
                print("COUNTER_72", i,ind_set,(list(ind_set)[0]),n_elem,not(i in sud3_list[key_row:key_row+81:9]) )    
                print(i,sud3_list[key_row:key_row+81:9],(i in sud3_list[key_row:key_row+81:9]))

                
                sud3_list[list(ind_set)[0]]=i              

                    
                del elem_dic_1[list(ind_set)[0]]

                counter+=1
    print("COUNTER_73", counter)           
    return  elem_dic_1,sud3_list             
             
       
       
       
       


#данная процедура ищет одинаковое положение по строкам одинаковых цифр в квадрате и
#в этой строде в других  квадратах корректирует множество и если один элемент то ставит значение       
def ins_one_dig_sq_row( elem_dic_1, sud3_list):
    
    for m in (0,27,54):
        
        sq_set={0,3,6}
       
        for key in sq_set:
            for i in range (9):
                i+=1
                boll_1=True
                boll_2=True
                boll_3=True    
                dig_set={i}     

                for z in range(0,27,9):
                    for j in range (3):
                  
                        if sud3_list[key + m + z + j]==0:
                            if  z==0 and elem_dic_1[key + m + z + j].issuperset(dig_set):
                                
                                boll_1=False
#                                    if i==2 :                    
#                                        print(i,key,z,j,set_sq_1,elem_dic_1[key+z+j],sud2_list[16])
                            elif z==9 and elem_dic_1[key + m + z + j].issuperset(dig_set):
                                
                                boll_2=False
                                
                            elif z==18 and elem_dic_1[key + m + z + j].issuperset(dig_set):
                            
                                boll_3=False
                
  

                if  not boll_1 and boll_2 and boll_3:
                    
                    if  key==0 :
                        for l in range(3,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
                                    
            
                    if  key==3 :
                        for l in range(0,3):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
            
            
                        for l in range(6,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
                        
            
                    if  key==6 :
                        for l in range(0,6):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                if   boll_1 and not boll_2 and boll_3:
                    
                    if  key==0 :
                        for l in range(3,9):
                            if  sud3_list[ m + l+9]==0:
                                if len(elem_dic_1[m+l+9]-dig_set)==1 :
                                    sud3_list[ m + l+9]=(elem_dic_1[m+l+9]-dig_set).pop()
                                    del  elem_dic_1[m+l+9]
                                    
            
                    if  key==3 :
                        for l in range(0,3):
                            if  sud3_list[ m + l+9]==0:
                                if len(elem_dic_1[m+l+9]-dig_set)==1 :
                                    sud3_list[ m + l+9]=(elem_dic_1[m+l+9]-dig_set).pop()
                                    del  elem_dic_1[m+l+9]
            
            
                        for l in range(6,9):
                            if  sud3_list[ m + l+9]==0:
                                if len(elem_dic_1[m+l+9]-dig_set)==1 :
                                    sud3_list[ m + l+9]=(elem_dic_1[m+l+9]-dig_set).pop()
                                    del  elem_dic_1[m+l+9]
                        
            
                    if  key==6 :
                        for l in range(0,6):
                            if  sud3_list[ m + l+9]==0:
                                if len(elem_dic_1[m+l+9]-dig_set)==1 :
                                    sud3_list[ m + l+9]=(elem_dic_1[m+l+9]-dig_set).pop()
                                    del  elem_dic_1[m+l+9]
            
            
                

                if  boll_1 and  boll_2 and not boll_3:                    
                    if  key==0 :
                        for l in range(3,9):
                            if  sud3_list[ m +18 + l]==0:
                                if len(elem_dic_1[m+18+l]-dig_set)==1 :
                                    sud3_list[ m + 18 + l]=(elem_dic_1[m+18+l]-dig_set).pop()
                                    del  elem_dic_1[m+18+l]
                                    
            
                    if  key==3 :
                        for l in range(0,3):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+18+l]-dig_set)==1 :
                                    sud3_list[ m+18 + l]=(elem_dic_1[m+18+l]-dig_set).pop()
                                    del  elem_dic_1[m+18+l]
            
            
                        for l in range(6,9):
                            if  sud3_list[ m+18 + l]==0:
                                if len(elem_dic_1[m+18+l]-dig_set)==1 :
                                    sud3_list[ m+18 + l]=(elem_dic_1[m+18+l]-dig_set).pop()
                                    del  elem_dic_1[m+18+l]
                        
            
                    if  key==6 :
                        for l in range(0,6):
                            if  sud3_list[ m+18 + l]==0:
                                if len(elem_dic_1[m+18+l]-dig_set)==1 :
                                    sud3_list[ m+18 + l]=(elem_dic_1[m+18+l]-dig_set).pop()
                                    del  elem_dic_1[m+18+l]                    
                                
            
            
            
            
            
            
            
            
            
           
                           
                        
    return elem_dic_1,sud3_list







#данная процедура ищет одинаковое положение по столбцамодинаковых цифр в строке и
#столбце в разных квадратахи в третьем определяет позицию       
def ins_one_dig_sq_col( elem_dic_1, sud3_list):
    
    for m in (0,3,6):
        sq_set={0,27,54}   
            
        for key in sq_set:
            for i in range (9):
                
                i+=1
                
                dig_set={i}
                boll_1=True
                boll_2=True
                boll_3=True 
                     

                for z in range(3):
                    for j in range (3):
                  
                        if sud3_list[key + m + z + j*9]==0:
                            if  z==0 and elem_dic_1[key + m + z + j*9].issuperset(dig_set):
                                
                                boll_1=False
#                                    if i==2 :                    
#                                        print(i,key,z,j,set_sq_1,elem_dic_1[key+z+j*9],sud2_list[16])
                            elif z==1 and elem_dic_1[key + m + z + j*9].issuperset(dig_set):
                                
                                boll_2=False
                                
                            elif z==2 and elem_dic_1[key + m + z + j*9].issuperset(dig_set):
                            
                                boll_3=False
                if m==3:
                    print("Counter_70",i,boll_1,boll_2,boll_3)
  

                if  not boll_1 and boll_2 and boll_3:
                    
                    if  key==0 :
                        for l in range(27,81,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
                                    
            
                    if  key==27 :
                        for l in range(0,27,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
            
            
                        for l in range(54,81,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
                        
            
                    if  key==54 :
                        for l in range(0,54,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
            
                                          
                if   boll_1 and not boll_2 and boll_3:
                     
                    if  key==0 :
                        for l in range(28,82,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
                                    
            
                    if  key==27 :
                        for l in range(1,28,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
            
            
                        for l in range(55,82,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
                        
            
                    if  key==54 :
                        for l in range(1,55,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]                    
            
            
                

                if  boll_1 and  boll_2 and not boll_3:
                    
                    if  key==0 :
                        for l in range(29,83,9):
                            if  sud3_list[ m  + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m  + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
                                    
            
                    if  key==27 :
                        for l in range(2,29,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m + l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
            
            
                        for l in range(56,83,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m+ l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]
                        
            
                    if  key==54 :
                        for l in range(2,56,9):
                            if  sud3_list[ m + l]==0:
                                if len(elem_dic_1[m+l]-dig_set)==1 :
                                    sud3_list[ m+ l]=(elem_dic_1[m+l]-dig_set).pop()
                                    del  elem_dic_1[m+l]                    
                                
            
            
             
                        
    return elem_dic_1,sud3_list







#проверяет  колонку что цифра может быть только в этой колонку и корректирует словарь 

def ins_one_col (elem_dic_1):
    
    

    sq_set={0,3,6,27,30,33,54,57,60}
    for key in sq_set:
        
        for i in range (9):
            i+=1
            b_col_1=False
            b_col_2=False
            b_col_3=False
            dig_set={i}
            for j in range(0,27,9):
                if key+j in list(elem_dic_1.keys()):
                  b_col_1 = b_col_1 or dig_set.issubset(elem_dic_1[key+j])
                if key+j+1  in list(elem_dic_1.keys()):
                  b_col_2 = b_col_2 or dig_set.issubset(elem_dic_1[key+j+1])
                if key+j+2  in list(elem_dic_1.keys()):
                  b_col_3 = b_col_3 or dig_set.issubset(elem_dic_1[key+j+2])

#                print("COUNTER_80",key,i,j,key +j,b_col_1,b_col_2,b_col_3)
                  
            if b_col_1== True and b_col_2 == False and b_col_3 == False:
#               print("COUNTER_81",key,i,b_col_1,b_col_2,b_col_3)
                if key == 0 or key == 3 or key == 6:
                    for z in range(27,81,9):
                        if key+z in list(elem_dic_1.keys()):
#                            print("COUNTER_811",i,key,z,key+z,elem_dic_1[key+z])
                            
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
#                            print("COUNTER_812",i,key,z,key+z,elem_dic_1[key+z])
#                   elem_dic_1[key+27:key+81:9]=elem_dic_1[key+27:key+81:9]-dig_set
                elif key == 27 or key == 30 or key == 33:
                    for z in range( 0,27,9):
                        if key-27+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-27+z]=elem_dic_1[key-27+z]-dig_set
                            
#                   elem_dic_1[key-27:key:9]=elem_dic_1[key-27:key:9]-dig_set
                    for z in range(54,81,9):
                        if key-27+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-27+z]=elem_dic_1[key-27+z]-dig_set
                            
#                   elem_dic_1[key+27:key+54:9]=elem_dic_1[key+27:key+54:9]-dig_set
                elif key == 54 or key == 57 or key == 60:
                    for z in range(0,54,9):
                        if key-54+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-54+z]=elem_dic_1[key-54+z]-dig_set
                            
#                    elem_dic_1[key-54:key:9]=elem_dic_1[key-54:key:9]-dig_set     
            if b_col_1 ==  False and b_col_2 == True and b_col_3 == False:
#                print("COUNTER_82",key,i,b_col_1,b_col_2,b_col_3)
                if key == 0 or key == 3 or key == 6:
                    for z in range(28,82,9):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
#                    elem_dic_1[key+28:key+82:9]=elem_dic_1[key+28:key+82:9]-dig_set
                elif key == 27 or key == 30 or key == 33:
                    for z in range(1,28,9):
                        if key-27+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-27+z]=elem_dic_1[key-27+z]-dig_set
#                    elem_dic_1[key-26:key+1:9]=elem_dic_1[key-26:key+1:9]-dig_set
                    for z in range(55,82,9):
                        if key-27+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-27+z]=elem_dic_1[key-27+z]-dig_set
                            
#                    elem_dic_1[key+28:key+55:9]=elem_dic_1[key+28:key+55:9]-dig_set
                elif key == 54 or key == 57 or key == 60:
                    for z in range(1,55,9):
                        if key-54+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-54+z]=elem_dic_1[key-54+z]-dig_set
                            
#                    elem_dic_1[key-53:key+1:9]=elem_dic_1[key-53:key+1:9]-dig_set
            if b_col_1 == False and b_col_2 == False and b_col_3 == True:
#                print("COUNTER_83",key,i,b_col_1,b_col_2,b_col_3)
                if key == 0 or key == 3 or key == 6:
                    for z in range(29,83,9):
                        if key+ z in list(elem_dic_1.keys()):
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
                           
#                   elem_dic_1[key+29:key+83:9]=elem_dic_1[key+29:key+83:9]-dig_set
                elif key == 27 or key == 30 or key == 33:
                    for z in range(2,29,9):
                        if key-27+z in list(elem_dic_1.keys()):
#                            print("COUNTER_813",i,key,z,key+z,elem_dic_1[key+z])
#                            print(key,z,elem_dic_1[z],dig_set)
                            elem_dic_1[key-27+z]=elem_dic_1[key-27+z]-dig_set
                            
#                            print("COUNTER_814",i,key,z,key+z,elem_dic_1[key-27+z])
#                            print(key,z,elem_dic_1[z],dig_set)
#                    elem_dic_1[key-25:key+2:9]=elem_dic_1[key-25:key+2:9]-dig_set
                    for z in range(56,83,9):
                        if key-27+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-27+z]=elem_dic_1[key-27+z]-dig_set
                            
#                   elem_dic_1[key+29:key+56:9]=elem_dic_1[key+29:key+56:9]-dig_set
                elif key == 54 or key == 57 or key == 60:
                    for z in range(2,56,9):
                        if key-54+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-54+z]=elem_dic_1[key-54+z]-dig_set
                            
#                   elem_dic_1[key-52:key+2:9]=elem_dic_1[key-52:key+2:9]-dig_set

    return elem_dic_1



#проверяет  строку что цифра может быть только в этой строке и корректирует словарь 

def ins_one_row (elem_dic_1):
    
    

    sq_set={0,3,6,27,30,33,54,57,60}
    for key in sq_set:
        
        for i in range (9):
            i+=1
            b_row_1=False
            b_row_2=False
            b_row_3=False
            dig_set={i}
            for j in range(3):
                if key+j in list(elem_dic_1.keys()):
                  b_row_1 = b_row_1 or dig_set.issubset(elem_dic_1[key+j])
                if key+j+9  in list(elem_dic_1.keys()):
                  b_row_2 = b_row_2 or dig_set.issubset(elem_dic_1[key+j+9])
                if key+j+18  in list(elem_dic_1.keys()):
                  b_row_3 = b_row_3 or dig_set.issubset(elem_dic_1[key+j+18])

            print("COUNTER_90",key,i,b_row_1,b_row_2,b_row_3)
                  
            if b_row_1== True and b_row_2 == False and b_row_3 == False:
                print("COUNTER_91",key,i,b_row_1,b_row_2,b_row_3)
                if key == 0 or key == 27 or key == 54 :
                    for z in range(3,9):
                        if key+z in list(elem_dic_1.keys()):
                            print("COUNTER_911",i,key,z,key+z,elem_dic_1[key+z])
                            
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
                            print("COUNTER_912",i,key,z,key+z,elem_dic_1[key+z])
#                   elem_dic_1[key+27:key+81:9]=elem_dic_1[key+27:key+81:9]-dig_set
                elif key == 3 or key == 30 or key == 57:
                    for z in range( -3,0):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
#                   elem_dic_1[key-27:key:9]=elem_dic_1[key-27:key:9]-dig_set
                    for z in range(3,6):
                        if key-27+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-27+z]=elem_dic_1[key-27+z]-dig_set
                            
#                   elem_dic_1[key+27:key+54:9]=elem_dic_1[key+27:key+54:9]-dig_set
                elif key == 6 or key == 33 or key == 60:
                    for z in range(-6,0):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
#                    elem_dic_1[key-54:key:9]=elem_dic_1[key-54:key:9]-dig_set     
            if b_row_1 ==  False and b_row_2 == True and b_row_3 == False:
#                print("COUNTER_92",key,i,b_row_1,b_row_2,b_row_3)
                if key == 0 or key == 27 or key == 54:
                    for z in range(12,18):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
#                    elem_dic_1[key+28:key+82:9]=elem_dic_1[key+28:key+82:9]-dig_set
                elif key == 3 or key == 30 or key == 57:
                    for z in range(6,9):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
#                    elem_dic_1[key-26:key+1:9]=elem_dic_1[key-26:key+1:9]-dig_set
                    for z in range(12,15):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
#                    elem_dic_1[key+28:key+55:9]=elem_dic_1[key+28:key+55:9]-dig_set
                elif key == 6 or key == 33 or key == 60:
                    for z in range(3,9):
                        if key+z in list(elem_dic_1.keys()):
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
#                    elem_dic_1[key-53:key+1:9]=elem_dic_1[key-53:key+1:9]-dig_set
            if b_row_1 == False and b_row_2 == False and b_row_3 == True:
#                print("COUNTER_93",key,i,b_row_1,b_row_2,b_row_3)
                if key == 0 or key == 27 or key == 54:
                    for z in range(21,27):
                        if key+ z in list(elem_dic_1.keys()):
                            elem_dic_1[key+z]=elem_dic_1[key+z]-dig_set
                            
                           
#                   elem_dic_1[key+29:key+83:9]=elem_dic_1[key+29:key+83:9]-dig_set
                elif key == 3 or key == 30 or key == 57:
                    for z in range(15,18):
                        if key-27+z in list(elem_dic_1.keys()):
                            print("COUNTER_913",i,key,z,key+z,elem_dic_1[key+z])
                            print(key,z,elem_dic_1[z],dig_set)
                            elem_dic_1[key-27+z]=elem_dic_1[key-27+z]-dig_set
                            
#
                            print("COUNTER_914",i,key,z,key+z,elem_dic_1[key-27+z])
                            print(key,z,elem_dic_1[z],dig_set)
#                    elem_dic_1[key-25:key+2:9]=elem_dic_1[key-25:key+2:9]-dig_set
                    for z in range(21,24):
                        if key-27+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-27+z]=elem_dic_1[key-27+z]-dig_set
                            
#                   elem_dic_1[key+29:key+56:9]=elem_dic_1[key+29:key+56:9]-dig_set
                elif key ==6 or key == 33 or key == 60:
                    for z in range(12,18):
                        if key-54+z in list(elem_dic_1.keys()):
                            elem_dic_1[key-54+z]=elem_dic_1[key-54+z]-dig_set
                            
#                   elem_dic_1[key-52:key+2:9]=elem_dic_1[key-52:key+2:9]-dig_set

    return elem_dic_1






#процедура проверяет квадрат на наличие одинаковых наборов множеств и по остальным
#свбодным ячейкам в квадрате делает корректировку набора и и результирующего набора строки

def ins_two_equel_squ(elem_dic_1,sud3_list):
    
    
    sq_set={0,3,6,27,30,33,54,57,60}
    for key in sq_set:
        num_set=set()
        
        for i in range(0,27,9):
            for j in range(3):
                if sud3_list[key+i+j]==0:
                    num_set.add(key+i+j)
                    
        if len(num_set)==2:
#проверям находится ли одной строке, и если да то корректируем наборы и при одном наборе в строке
            loop_set=set()
            if int( (list(num_set)[0])/9)==int( list(num_set)[1]/9) and elem_dic_1[int( list(num_set)[0])]==elem_dic_1[int( list(num_set)[1])] :
                for z in range (9):
                    if sud3_list[int( (list(num_set)[0])/9)*9+z] ==0:
                        loop_set.add(int( (list(num_set)[0])/9)*9+z)
                loop_set=loop_set-num_set
                for k in loop_set:
                    if len(elem_dic_1[k]-elem_dic_1[num_set[0]])==1:
                           sud3_set[k]=(elem_dic_1[k]-elem_dic_1[num_set[0]]).pop()
                           del elem_dic_1[k]
#проверям находится ли одном столбце, и если да то корректируем наборы и при одном наборе в столбце
            if int( (list(num_set)[0])%9)==int( list(num_set)[1]%9) and elem_dic_1[int( list(num_set)[0])]==elem_dic_1[int( list(num_set)[1])] :
                for z in range (int( (list(num_set)[0])%9),81+int( (list(num_set)[0])%9),9):
                    if sud3_list[z] ==0:
                        loop_set.add(z)
                loop_set=loop_set-num_set
                for k in loop_set:
                    if len(elem_dic_1[k]-elem_dic_1[num_set[0]])==1:
                           sud3_set[k]=(elem_dic_1[k]-elem_dic_1[num_set[0]]).pop()
                           del elem_dic_1[k]

                           
        if len(num_set)==3:
#проверям находится ли одной строке, и если да то корректируем наборы и при одном наборе в строке
            loop_set=set()
            if int( (list(num_set)[0])/9)==int( list(num_set)[1]/9)==int( list(num_set)[2]/9) and elem_dic_1[int( list(num_set)[0])]==elem_dic_1[int( list(num_set)[1])] :
                for z in range (9):
                    if sud3_list[int( (list(num_set)[0])/9)*9+z] ==0:
                        loop_set.add(int( (list(num_set)[0])/9)*9+z)
                loop_set=loop_set-num_set
                for k in loop_set:
                    if len(elem_dic_1[k]-elem_dic_1[num_set[0]])==1:
                           sud3_set[k]=(elem_dic_1[k]-elem_dic_1[num_set[0]]).pop()
                           del elem_dic_1[k]
#проверям находится ли одном столбце, и если да то корректируем наборы и при одном наборе в столбце
            if int( (list(num_set)[0])%9)==int( list(num_set)[1]%9)==int( list(num_set)[2]%9)and elem_dic_1[int( list(num_set)[0])]==elem_dic_1[int( list(num_set)[1])] :
                for z in range (int( (list(num_set)[0])%9),81+int( (list(num_set)[0])%9),9):
                    if sud3_list[z] ==0:
                        loop_set.add(z)
                loop_set=loop_set-num_set
                for k in loop_set:
                    if len(elem_dic_1[k]-elem_dic_1[num_set[0]])==1:
                           sud3_set[k]=(elem_dic_1[k]-elem_dic_1[num_set[0]]).pop()

                           del elem_dic_1[k]

        indic= True
        num_set_1=num_set
        while indic :
            for m in num_set:
                num_set_1=num_set_1-{m}
                
                print("step 19",m,num_set,num_set_1)

#                print(elem_dic)
                for n in num_set_1:
                    print("step 20",m,n,num_set,num_set_1)
                    
                    if elem_dic_1[m]==elem_dic_1[n] and len(elem_dic_1[m])==2:
                        print("step 201",m,n,num_set,num_set_1)
                        print(elem_dic_1[m],elem_dic_1[n])
                        num_set_2=num_set-{m}-{n}
                        print("step 21",num_set,num_set_2,m,n)
                        print(elem_dic_1[m] ,elem_dic_1[n])
                
        
                        for l in num_set_2:

                            if len(elem_dic_1[l]-elem_dic_1[m])==1:
                                print("step 22",num_set,num_set_2,l,m,n,sud2_list[l])
                                print(elem_dic_1[l])
                
                                sud3_list[l]=(elem_dic_1[l]-elem_dic_1[m]).pop()
                                del elem_dic_1[l]
                    
                                print("step 23",num_set,num_set_2,l,m,n,sud2_list[l])
#                                print(elem_dic_1[l])
                                indic=False
                        break
                     
                break

            break

                        
#        break
                
                
                    
                       
    return sud3_list,elem_dic_1

#проверяет наличие одного элемента в сете по всем эдементам и заменяет его в листе   
    

def ins_one_elem (elem_dic_1,sud3_list) :
    global  counter 
    counter =0
    for key in range(81):#list(elem_dic.keys()):  # Use a list instead of a view

#ecли в сформированном словаре множество имеет один элемент то списку присваивается значение этого элемента        
        if sud3_list[key]==0 and len(elem_dic_1[key])==1:
           
            print("COUNTER_50",key,sud3_list[key],sud3_list[key]==0,len(elem_dic_1[key]),elem_dic_1[key] ) 
                
            sud3_list[key]= (elem_dic_1[key]).pop()

            del elem_dic_1[key]
            if key == 6:
                print("COUNTER_50",sud3_list[6]) 
   
            counter+=1
    return  elem_dic_1,sud3_list             




def  make_dict(elem_dic_1,sud3_list) :
    
    for i in range(81):
        
       
        if  sud3_list[i]==0:
           
                     
            n_row=int(i/27)
            n_col=int((i%9)/3)
            sud_set_sq_1=set(sud3_list[(n_row*27)+ (n_col*3):(n_row*27)+ (n_col*3)+3]) 
            sud_set_sq_2=set(sud3_list[(n_row*27)+ (n_col*3)+9:(n_row*27)+ (n_col*3)+9+3])
            sud_set_sq_3=set(sud3_list[(n_row*27)+ (n_col*3)+18:(n_row*27)+ (n_col*3)+18+3])
            sud_set_sq= sud_set_sq_1 |sud_set_sq_2 | sud_set_sq_3
            set_row=set(sud3_list[int(i/9)*9:int(i/9)*9+9])

            set_col=set( sud3_list[(int(i%9))::9])
            set_elem=test_set - sud_set_sq - set_row -set_col

            elem_dic_1[i]=set_elem
            
            



    return elem_dic_1




#этот блок проверяет квадраты наналичие не повторяюшихся цифр во множестве слоаря
#и переписывает соответствующий элемент в список    
def insp_squ(elem_dic_1,sud3_list):
    global  counter
    counter=0
    for i in range(81):
        n_row=int(i/27)
        n_col=int((i%9)/3)
        squ=set()
        if  sud3_list[i]==0:
 
            squ1=set()
            for c_row in range(3):
                for c_col in range(3):
                    n_elem= int((n_row*27 +c_row*9)+(n_col*3+c_col))
                    if n_elem in elem_dic_1.keys() and n_elem !=i:
#                        print ("COUNTER_31",i,squ,n_elem,squ1,elem_dic_1[n_elem])
                        squ1= squ1|elem_dic_1[n_elem]
#                        print ("COUNTER_32",i,squ,n_elem,squ1,elem_dic_1[n_elem])
#            print ("COUNTER_33",elem_dic_1[i],i,squ,n_elem,squ1)            
            squ = elem_dic_1[i] - squ1
            if len (squ)==1:
#                print ("COUNTER_30",i,squ )
                sud3_list[i]=squ.pop()
                del elem_dic_1[i]
                counter+=1
  
    return  elem_dic_1,sud3_list              
 


        
#read from file sudoku in list integer
#nomer 205
with open('exsud13.txt', 'r') as f:
    sud_list=f.read().split(' ')#.replace('\n','')
#made list , delete non writeable symbol and list wiht intenger elements     
sud1_list=sud_list[0].replace('\n','')
sud0_list = list(map(int, sud1_list[:]))
sud2_list = list(map(int, sud1_list[:]))

#made test set with elements from 1 to 9 for comparing 
test_set=set(i for i in range (10))

#create dictionary where key - namber element, value set of posible digit
elem_dic={}

make_dict(elem_dic,sud2_list)
print("COUNTER_0")
pr_vid_dic (elem_dic,sud2_list )
print(len(elem_dic),sud2_list.count(0))


g_counter=0


while sud2_list.count(0)!=0 :
    g_counter=+1

    counter=1
    
    
    while counter !=0  : 
    
    
    
    
   

        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
   
        insp_squ(elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_col (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_row (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
    

            print("COUNTER_10", counter)
    
            pr_vid_dic (elem_dic,sud2_list )
    
    
   
    counter = 1    
    while counter !=0:
        print("COUNTER_11", counter)
    
        for _  in  range(3):
            ins_one_col (elem_dic)
            print("COUNTER_18", counter)
            pr_vid_dic (elem_dic,sud2_list )
            ins_one_elem__in_row (elem_dic,sud2_list)
            pr_vid_dic (elem_dic,sud2_list )


        counter = 1 
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
    
        
        
    counter=1
    while counter !=0  : 
    
    
    
    
    

        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
   
        insp_squ(elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_col (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_row (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
   

    print("COUNTER_12", counter)
    
    pr_vid_dic (elem_dic,sud2_list )
    
    
    counter = 1    
    while counter !=0:
        print("COUNTER_13", counter)
    
        for _  in  range(3):
            ins_one_row (elem_dic)
            print("COUNTER_18", counter)
            pr_vid_dic (elem_dic,sud2_list )
            ins_one_elem__in_col(elem_dic,sud2_list)
            pr_vid_dic (elem_dic,sud2_list )
    
            counter = 1 
            while counter !=0:
                ins_one_elem (elem_dic,sud2_list)
                make_dict(elem_dic,sud2_list)
    
    
    
    
    
    
    
    
    
    counter=1
    while counter !=0  : 
    
    
    
    
    

        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
   
        insp_squ(elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_col (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_row (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
    
        

    print("COUNTER_14", counter)
    
    pr_vid_dic (elem_dic,sud2_list )
    
    
    
    counter = 1    
    while counter !=0:
        print("COUNTER_15", counter)
        counter = 1    
        for _  in  range(3):
            ins_one_col (elem_dic)
            ins_one_row (elem_dic)
            ins_two_eguel_set_in_squ (elem_dic,sud2_list)
        
       
        pr_vid_dic (elem_dic,sud2_list )
        
        ins_one_elem__in_row (elem_dic,sud2_list)

        ins_one_elem__in_col (elem_dic,sud2_list)

    
        counter = 1 
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
    
        
        
    counter=1
    while counter !=0  : 
    
    
    
    
   
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
   
        insp_squ(elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_col (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_row (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
    
    print("COUNTER_16", counter)
    
    
    
    
    alg_hid_set_in_squ (elem_dic,sud2_list)
    print("COUNTER_161", counter)
    pr_vid_dic (elem_dic,sud2_list )
    counter=1
    while counter !=0:
            print("COUNTER_1611", counter)
            pr_vid_dic (elem_dic,sud2_list ) 
            ins_one_elem (elem_dic,sud2_list)
            print("COUNTER_1612", counter)
            pr_vid_dic (elem_dic,sud2_list )
            make_dict(elem_dic,sud2_list)
            print("COUNTER_1613", counter)
            pr_vid_dic (elem_dic,sud2_list )
       
    print("COUNTER_162", counter)
    pr_vid_dic (elem_dic,sud2_list )       
    
    insp_squ(elem_dic,sud2_list)
    
    ins_one_elem__in_row (elem_dic,sud2_list)
    print("COUNTER_163", counter)
    pr_vid_dic (elem_dic,sud2_list )

    ins_one_elem__in_col (elem_dic,sud2_list)

    make_dict(elem_dic,sud2_list)
    print("COUNTER_164", counter)
    pr_vid_dic (elem_dic,sud2_list )
    
    counter=1
    while counter !=0  : 
    
    
    
    
   
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
   
        insp_squ(elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_col (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
        
        
        ins_one_elem__in_row (elem_dic,sud2_list)
        make_dict(elem_dic,sud2_list)
        while counter !=0:
            ins_one_elem (elem_dic,sud2_list)
            make_dict(elem_dic,sud2_list)
    
    
    
        

    print("COUNTER_17", counter)
    
    pr_vid_dic (elem_dic,sud2_list )
      
    print("COUNTER_171", g_counter,sud2_list.count(0),sud2_list.count(0)==0, g_counter<1000,sud2_list.count(0)==0 or g_counter<1000)   
    
    
    
print("COUNTER_52", counter)


pr_vid_dic (elem_dic,sud2_list)
    
 
    
pr_vid_sudo (sud2_list)


print(len(elem_dic),sud2_list.count(0))

print ("\n\n\n FIRST")

pr_vid_sudo (sud0_list)






                     
