import re

x = int(input("Insira o mínimo de adultos possíveis: "))
y = int(input("Insira o máximo de adultos possíveis: "))

test =  str(input("Descreva a sequência de caracteres: "))

while (x >= y or y <= x):
    x = int(input("Insira novamente o mínimo de adultos possíveis: "))
    y = int(input("Insira novamente o máximo de adultos possíveis: "))
    
if bool(re.match(r'[mhMH]', test, flags=0)) == False:
    while bool(re.match(r'[mhMH]', test, flags=0)) == False :
        test =  str(input("Descreva sequência de caracteres contendo M, H, m e h: "))

testmatcha = re.match(r'(MH|HM)(((m|h)*m+(m|h)*m+(m|h)*)|((m|h)*h+(m|h)*)|((m|h)*h+(m|h)*h+(m|h)*))', test, flags=0)
testmatchb = re.match(r'(MH|HM)((m|h))*', test, flags=0)
testmatchc = re.match(r'(MH|HM)m(h|m)*(h)$', test, flags=0)
testmatchd = re.match(r'(MM|HH)(mm|hh|mh|hm)(mm|hh|mh|hm)(h|m)*(mm|hh|mh|hm)$', test, flags=0)
testmatche = re.match(r'(MM|HH)((m?)(hm)*(h?))$|((h?)(mh)*(m?))$', test, flags=0)
testmatchf = re.match(r'(MM|HH)((h(m|mh)*m?)$|(m(m|hm)*h?)$)', test, flags=0)
testmatchg = re.match(r'(M|H){%d,%d}(m|h)*mmm'%(x,y), test, flags=0)


if bool(testmatcha) == True:
   print("caso a)")

if bool(testmatchb) == True:
    mCounter = 0
    for letter in test:
        if letter == 'm':
            mCounter += 1
    
    if mCounter%3 == 0:
        print("caso b)")
        
if bool(testmatchc) == True:
    print("caso c)")
    
if bool(testmatchd) == True:
    print("caso d)")
    
if bool(testmatche) == True:
    print("caso e)")
        
if bool(testmatchf) == True:
    print("caso f)")

if bool(testmatchg) == True:
    print("caso g)")