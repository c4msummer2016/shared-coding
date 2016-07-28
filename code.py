
LL =['AYLMNKVVNVVEGKV', 'CDILCHWCKRNVGWK', 'CHWCKRNVGWKYLQS', 'CKRNVGWKYLQSSND','CRHCKTHLSSSFQII','DDQQYKEGKFILELK','DILCHWCKRNVGWKY','DQQYKEGKFILELKN','DYLVCDILCHWCKRN','DYRGRTGTAYLMNKV','EGKFILELKNICKCT','ENPLSSPSSSYKSIN','EQRRMLTGDYLVCDI','FHSQHRSQKNVSFIT','FITYGCRHCKTHLSS','GDYLVCDILCHWCKR','GKVEQRRMLTGDYLV','GLRYSIYIENPLSSP','GRTGTAYLMNKVVNV','GTAYLMNKVVNVVEG','HCKTHLSSSFQIISR','HLSSSFQIISRDYRG','IISRDYRGRTGTAYL','ISRDYRGRTGTAYLM','ITYGCRHCKTHLSSS','IYIENPLSSPSSSYK','KEGKFILELKNICKC','KRNVGWKYLQSSNDD','KSINDPLFHSQHRSQ','KVEQRRMLTGDYLVC','KVVNVVEGKVEQRRM','KYLQSSNDDQQYKEG','LFHSQHRSQKNVSFI','LMNKVVNVVEGKVEQ','LQSSNDDQQYKEGKF','LSSPSSSYKSINDPL','LSSSFQIISRDYRGR','LTGDYLVCDILCHWC','LVCDILCHWCKRNVG','MGLRYSIYIENPLSS','MNKVVNVVEGKVEQR','NDDQQYKEGKFILEL','NDPLFHSQHRSQKNV','NKVVNVVEGKVEQRR','NPLSSPSSSYKSIND','NVVEGKVEQRRMLTG','PLSSPSSSYKSINDP','PSSSYKSINDPLFHS','QHRSQKNVSFITYGC','QIISRDYRGRTGTAY','QKNVSFITYGCRHCK','QYKEGKFILELKNIC','RDYRGRTGTAYLMNK','RGRTGTAYLMNKVVN','RHCKTHLSSSFQIIS','RMLTGDYLVCDILCH','RRMLTGDYLVCDILC','RSQKNVSFITYGCRH','RTGTAYLMNKVVNVV','RYSIYIENPLSSPSS','SFITYGCRHCKTHLS','SINDPLFHSQHRSQK','SIYIENPLSSPSSSY','SPSSSYKSINDPLFH','SQHRSQKNVSFITYG','SQKNVSFITYGCRHC','SRDYRGRTGTAYLMN','SSFQIISRDYRGRTG','SSNDDQQYKEGKFIL','FQIISRDYRGRTGTA','SSPSSSYKSINDPLF','SSSFQIISRDYRGRT','SSSYKSINDPLFHSQ','SSYKSINDPLFHSQH','SYKSINDPLFHSQHR','TAYLMNKVVNVVEGK','TGTAYLMNKVVNVVE','THLSSSFQIISRDYR','TYGCRHCKTHLSSSF','VCDILCHWCKRNVGW','VGWKYLQSSNDDQQY','VNVVEGKVEQRRMLT','VSFITYGCRHCKTHL','VVEGKVEQRRMLTGD','VVNVVEGKVEQRRML','WKYLQSSNDDQQYKE','YGCRHCKTHLSSSFQ','YKEGKFILELKNICK','YKSINDPLFHSQHRS','YLMNKVVNVVEGKVE','YLQSSNDDQQYKEGK','YLVCDILCHWCKRNV','YRGRTGTAYLMNKVV','YSIYIENPLSSPSSS','MLTGDYLVCDILCHW']

next={}
#this is a setup function that fills in the 'next' dictionary based on the array LL 
for s in LL:
#iterates through all of the strings in the array LL.
  for i in range(0,len(s)-4):
    #iterates through all the characters in string s, not including the last 4. combined with the last one, this iterates through most of all characters in LL
    next[s[i:i+4]]=s[i+4]
    #sets the 'next' of s, the character after s, and the character after that character to the character 4 characters after s. this means that even though the iteration stops at 4 before the end, it catches every single possible 'next'

begin="MGLR"
#this manually sets the beggining to MGLR to give the code something to base itself off of
seq=begin
#this manually sets seq to begin, or MGLR, to give the code something to base itself off of

while True:
#this means that this while loop will never ever stop unless manually broken
      if begin in next:
      #checks if the code has not yet iterated beyond the point where the current 'begin' is in 'next'
         n=next[begin]
         #sets a new variable, 'n', to the element in the dictionary 'next' that has the index of the letters in 'begin'
         seq=seq+n
         #adds n to seq.
         begin=begin[1:4]+n
         #shifts begin over 1, dropping the first letter and adding n, or the letter after the old begin, to the end.
      else:
      #stops running if the current operation the if statement would have preformed would act upon a 'begin' that is beyond the far end of 'next'
       break

print seq
      
