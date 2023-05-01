import re

#alfabet = 'MHmh'

test =  str(input("Descreva a sequência de caracteres"))
#while alfabet not in test:
#    test =  str(input("Descreva sequência de caracteres contendo M, H, m e h"))
 



testmatcha = re.match('(MH|HM)((m|h)*m+(m|h)*m+(m|h)*)$|((m|h)*h+(m|h)*)$|((m|h)*h+(m|h)*h+(m|h)*)$', test, flags=0)
testmatchb = re.match('^(MH|HM)(mm|h)*m+(mm|h)*$',test, flags = 0)
testmatchc = re.match('^(MH|HM)(m)(h|m)*(h)$', test, flags=0)
testmatchd = re.match('^(MM|HH)(mm|hh|mh|hm)(mm|hh|mh|hm)(h|m)*(mm|hh|mh|hm)$', test, flags=0)
testmatche = re.match('^(MM|HH)((m?)(hm)*(h?))$|((h?)(mh)*(m?))$', test, flags=0)
testmatchf = re.match('^(MM|HH)(h(m|mh)*m{0,1})$|(m(m|hm)*h{0,1})$', test, flags=0)


#if testmatchb:
#    print(True)
#if testmatchc:
#    print(True)
#if testmatchd:
#    print(True)
#if testmatche:
#    print(True)    
if testmatchf:
    print(True)