class Solution:
    def reverse(self, x: int) -> int:
        y=str(x)
        if(x<0):
            y=y[1:]
        
        mapped_digits=map(int, y)
        z=list(mapped_digits)
        temp=z.reverse()
        #print(temp)
        s=[str(integer) for integer in z]
        a_string = "". join(s)
        result=int(a_string)
        
        if(result< -2**31 or result>= 2**31):
            return 0
        elif (x>= 0):
            return result
        else:
            return -result
