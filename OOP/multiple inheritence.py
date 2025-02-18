class A:
    va1="It is A"
class B:
    va2="It is B"
class C(A,B):
    va3="It is C"
c=C()
print(c.va1,c.va2,c.va3)