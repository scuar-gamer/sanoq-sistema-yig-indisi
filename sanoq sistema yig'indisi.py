a,b=map(int,input().split())
s=0
while a>=b:
  s+=a%b
  a=a//b
s+=a
print(s)
