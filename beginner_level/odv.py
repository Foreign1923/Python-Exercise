import traceback
import sys
from math import log

__TEST__ = 0

class Digit_list(object):
    Testing_Q1 = 239945
    Testing_Q2_1:list = [2,3,9,9,4,5]
    Testing_Q1_2:list = [2,3,4] 
    def Question_A( parameter_unkown:int) -> list:
        def func_in(x:int, li1:list) -> None: 
            if(x > 10):
                func_in(x // 10, li1)
            li1.append(x % 10); 
            return None

        _l:list = list()
        func_in(parameter_unkown, _l)
        return _l
 
    def Question_B(parameter_list :list, function_place:int) -> list:
        def Replace_(li2:list, x:int, f:int) -> None:
           
            print(f"L {li2}")
            print(f"X {x}")
            print(f"F {f}")
            print(f"Index of X {li2.index(x)}")

            li2[li2.index(x)] = f
            return None; 

        def func_inn1(l:list):
            def func_inn2(l:list, c:int, i:int):
                nonlocal MAX_indx
                print(f"L{l}")
                print(f"C{c}")
                print(f"i{i}")
                if(i >= len(l)):
                    return 0
                count_indx:int = l[i:].count(l[i])

                if(count_indx > len(l) //2):
                    MAX_indx = l[i] 
                    return MAX_indx

                if(count_indx > c):
                    MAX_indx = l[i] 
                
                func_inn2(l, count_indx, i + count_indx)
                return 0


            l = l.copy()
            l.sort()
            
            print(f"L {l}")
            MAX_indx :int = None
            
            func_inn2(l, 0,0)
            return MAX_indx


        def func_inn3(r:int, l:list, m:int) -> int:
            try:
                print("error you should trace the inner function given:",m, func_inn2 )
                if(m not in l):
                    print("You should trace the inner 1")
                    return 0
                Replace_(l,func_inn2,r)
                func_inn3(r,l, m)
                return 0

            except Exception as e:

                print(traceback.format_exc())

            return -1
        
        def func_inn4(r:int, l:list) -> int:
            nonlocal Key_to
            if(Key_to):
                Key_to -= 1
                l.insert(0,r)
                func_inn4(r,l)
            return 0
        Key_to = len(parameter_list)    
        if(Key_to % 2 == 0): 
            func_inn2 = func_inn1(parameter_list)
            print(f"There is the main inner function: {func_inn2}")
            if(func_inn2 != function_place):
                print("There is the first one")
                func_inn3(function_place, parameter_list, func_inn2)
            else:
                print("Try again...")
            
        else :
            print("There is the second one")
            func_inn4(function_place, parameter_list)
        
        return parameter_list
    def Question_C():
        x =  y = 10
        x = int(input("X: "))
        while(not (0 < y < 10) ):
            y = int(input("Y:"))
    

        _list   = Digit_list.Question_A(x)
        N_List  = Digit_list.Question_B(_list.copy(), y)
        print("A\n",_list)
        print("B\n",N_List)


def main() -> int:
    if(__TEST__):
        A = Digit_list.Question_A(Digit_list.Testing_Q1)
        B = Digit_list.Question_B(Digit_list.Testing_Q2_1, 1)
        C = Digit_list.Question_B(Digit_list.Testing_Q1_2, 1)
    
        print(f"A:{A}")
        print(f"B:{B}")
        print(f"C:{C}")

        return 0

    Digit_list.Question_C()
    
    return 0

if(__name__ == '__main__'):
    main()



