#forgot to commit seperately first time, 2nd time around did
class utils:

    def reversed(number):
        '''
        Inputs: 
        - number: assume integer
        Output:
        - reversed number, can take negative number
        '''
        #regular integer - assuming its an integer, it can be negative
        
        #Making assumption strings of integers can still work any other type fail 
        try:
            number = int(number)
        except:
            return False    
        
        if (number > 0):    
            editing_number = str(number)
            editing_number = editing_number[::-1]

        else:
            editing_number = str(number)[1:]
            editing_number = "-" + editing_number[::-1]
        
        return int(editing_number)

    def formatter(number):
            '''
            Inputs: 
            -number: assume integer
            Outputs:
            - binary and octal number 
            '''
            #regular integer - assuming its an integer, it can be negative
            #Making assumption strings of integers can still work any other type fail
            try:
                number = int(number)
            except:
                return False  
            return bin(number), oct(number)
            
