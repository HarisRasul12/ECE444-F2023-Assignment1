class utils:

    def reversed(number: int):
        '''
        Inputs: 
        - number: assume integer
        Output:
        - reversed number, can take negative number
        '''
        #regular integer - assuming its an integer, it can be negative
        if (number > 0):
            
            editing_number = str(number)
            editing_number = editing_number[::-1]

        else:
            editing_number = str(number)[1:]
            editing_number = "-" + editing_number[::-1]
        
        return int(editing_number)

    def formatter(number: int):
            '''
            Inputs: 
            -number: assume integer
            Outputs:
            - binary and octal number 
            '''
            #regular integer - assuming its an integer, it can be negative
            return bin(number), oct(number)
            
