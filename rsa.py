from Crypto.Util.number import inverse, long_to_bytes
import binascii


p=71391722727717739701725166091355122687202806220568629026094214328299044250559
q=63705385054712742361366264023313834233300571732330798894025871462807058868837
c=1105226503465807521542759563216670205978729993278846163740949338419872446008653994624528555679226930396813159797836171650698733381154344190590806951929702
e=65537


n = p * q
phi = (p - 1) * (q - 1)
d = inverse(e, phi)


#encrypted
m = pow(c, d, n)
print(long_to_bytes(m), end="")



'''

#authenticated
#answer = hex(pow(c,e,n))
#print(answer[2:])
#print(str(bytes.fromhex(answer[2:]), 'utf-8'

def find_invpow(x, n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1
'''
