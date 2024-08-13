#!/usr/bin/python
import traceback
import sys
__TEST__ = 0;

class HW1(object):
    _Q1TEST :int = 239945;
    _Q2TEST1:list = [2,3,9,9,4,5];
    _Q2TEST2:list = [2,3,4]; 

    @staticmethod
    def Q1A( param_x:int) -> list:
        def _inner(x:int, l:list) -> None: # python does not create a deep copy of an array when it passed via parameter
            if(x > 10):
                _inner(x // 10, l);
            l.append(x % 10); # could also use insert 0
            return None;

        _l = list();
        _inner(param_x, _l);
        return _l;

    @staticmethod
    def Q1B(param_l :list, rplace:int) -> list:
        def _replace(l:list, x:int, r:int) -> None:
            l[l.index(x)] = r;
            return None; # this is funny about python, there is no void type but none which is actually a type




        def _inner1(r:int, l:list, m:int) -> int:
            try:
                print("MOST in inner1m,most",m, _most );
                if(m not in l):
                    return 0;
                if(_most == m):#max(l)): #max will be defined before calling the func
                    print("replace in inner1");
                    _replace(l,_most,r); 
                    _inner1(r,l, m);
                    return 0;

            except Exception as e:#incase if max is not defined
                #print("%s" % (e));#I could do pass the _max with param as I did in Q1
                print(traceback.format_exc())
            return -1; 
        
        def _inner2(r:int, l:list) -> int:
            nonlocal _key;
            if(_key):
                _key -= 1;
                l.insert(0,r);
                _inner2(r,l);
            return 0;

        _key = len(param_l);        
        if(_key % 2 == 0): # even length of list
            _most = max(param_l)#most(param_l);
            _inner1(rplace, param_l, _most);
            #print("TEST_MAX: %d" % (_max), file = sys.stdout);
        else :
            _inner2(rplace, param_l);
        
        return param_l;


    @staticmethod
    def Q1C():
        x =  y = 10;
        x = int(input("X:"));
        while(not (0 < y < 10) ):
            y = int(input("Y (0..10)"))
        
        _list   = HW1.Q1A(x);
        _nList  = HW1.Q1B(_list.copy(), y);
        print("A\n",_list);
        print("B\n",_nList);


def main() -> int:
    if(__TEST__):
        a = HW1.Q1A(HW1._Q1TEST);
        b = HW1.Q1B(HW1._Q2TEST1, 1);
        c = HW1.Q1B(HW1._Q2TEST2, 1);
        return 0;
    HW1.Q1C();
    return 0;

if(__name__ == '__main__'):
    main();



