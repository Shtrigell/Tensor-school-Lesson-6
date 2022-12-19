inp=open('C:\\Users\\Shtrige11\\Desktop\\Input.txt', 'r')
data=inp.read().splitlines()[1:]
C=[int(s) for s in data[0].split() if s.isdigit()]
H=[int(s) for s in data[1].split() if s.isdigit()]
O=[int(s) for s in data[2].split() if s.isdigit()]
try:
    alcohol=min([int(C[0])//2,int(H[0])//6,int(O[0])//1])
except IndexError:
    alcohol=0
inp.close()
out=open('C:\\Users\\Shtrige11\\Desktop\\Output.txt','w')
out.write("Количество молекул спирта равно: "+str(alcohol))
out.close()