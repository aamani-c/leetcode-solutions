class Solution:
    def reverse(self, x: int) -> int:
        min_int, max_int=-2**31,2**31-1
        sign=-1 if x<0 else 1
        x=abs(x)
        def reverse_rec(n,rev=0):
            if n==0:
                return rev
            digit=n%10
            rev=rev*10+digit
            return reverse_rec(n//10,rev)
        reversed_x=sign*reverse_rec(x)
        if reversed_x <min_int or reversed_x>max_int:
            return 0
        return reversed_x