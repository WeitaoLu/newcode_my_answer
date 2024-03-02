
#https://ac.nowcoder.com/acm/contest/11187/A
import sys 
count = int(sys.stdin.readline())
number = sys.stdin.readline().split()
number = [ int(n) for n in number]

odd = []
even = []
even_pos = []
odd_pos = []
for i in range(0,count):
    if number[i]%2 ==0:
        even_pos.append(i)
        even.append(number[i])
    else:
        odd_pos.append(i)
        odd.append(number[i])
gt = number.copy()
gt.sort()
even.sort()
odd.sort()
i=j=0
m=n=0
for i in range(0,count):
    if i in even_pos:
        number[i] = even[m]
        m+=1
    else:
        number[i] = odd[n]
        n+=1

if(gt==number):
    print("Yes")
else:
    print("No")
        
