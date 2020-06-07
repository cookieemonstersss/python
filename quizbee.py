print('Hello, buwan ng wika QUIZ BEE!!!')

ans = input ('handa kana ba sa ating palaro  (yes/no): ')
score = 0
total_q = 6
 
if ans.lower() == 'yes':
    print ('\n1. kailan nag simula ang buwan ng wika?')
    ans = input('\na. 1935.  \nb. 1948.  \nc. 1568.  \n\nSagot: ')

if ans.lower() == 'a':
        score += 1
        print ('\nCONGRATULATIONS!!!TAMA ANG IYONG SAGOT!!!')
else:
        print ('\nMALI ANG IYONG SAGOT!!! \nAng tamang sagot ay A.1935' )

print ('\n2. ano ang pambansang wika natin?')
ans = input('\na. cebuano.  \nb. tagalog.  \nc. filipino.  \n\nSagot: ')

if ans.lower() == 'c':
        score += 1
        print ('\nCONGRATULATIONS!!! TAMA ANG IYONG SAGOT!!!')
else:
        print ('\nMALI ANG IYONG SAGOT!!! \nAng tamang sagot ay C. filipino' )

print ('\n3. sino ang pangulong nagdeklara ng buwan ng agosto bilang "buwan ng wika"?')
ans = input('\na. diosdado macapagal.  \nb. ferdinand marcos.  \nc. fidel ramos.  \n\nSagot: ')

if ans.lower() == 'c':
        score += 1
        print ('\nCONGRATULATIONS!!! TAMA ANG IYONG SAGOT!!!')
else:
        print ('\nMALI ANG IYONG SAGOT!!! \nAng tamang sagot ay C. Fidel Ramos ' )



print ('\n4. who is the national hero of the philippines?')
ans = input('\na. Andres Bonifacio.  \nb. Dr. Jose Rizal.  \nc. Emilio Aguinaldo.  \n\nSagot: ')

if ans.lower() == 'b':
        score += 1
        print ('\nCONGRATULATIONS!!! TAMA ANG IYONG SAGOT!!!')
else:
        print ('\nMALI ANG IYONG SAGOT!!! \nAng tamang sagot ay B.Dr. Jose Rizal  ' )


print ('\n5. who is the brain of katipunan?')
ans = input('\na. Andres Bonifacio.  \nb. Apolinario Mabini.  \nc. Emilio Jacinto.  \n\nSagot: ')

if ans.lower() == 'c':
        score += 1
        print ('\nCONGRATULATIONS!!! TAMA ANG IYONG SAGOT!!!')
else:
        print ('\nMALI ANG IYONG SAGOT!!! \nAng tamang sagot ay C.Emilio Jacinto  ' )



print ('\n6. who is the founder of katipunan?')
ans = input('\na. Andres Bonifacio.  \nb. Apolinario Mabini.  \nc. Emilio Jacinto.  \n\nSagot: ')

if ans.lower() == 'a':
        score += 1
        print ('\nCONGRATULATIONS!!! TAMA ANG IYONG SAGOT!!!')
else:
        print ('\nMALI ANG IYONG SAGOT!!! \nAng tamang sagot ay A.Andres Bonifacio  ' )



print ('\nMaraming Salamat sa paglalaro, Ang Nakuha mo',score,"Sagot na tama" )
total= (score/total_q) *100

print('Average: ',total)
print('\nPaalam')
