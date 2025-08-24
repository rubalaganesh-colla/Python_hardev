basic = int(input("enter the value of basic"))
da = basic * 30/100
hra = basic * 12.5/100
pf = basic * 10/100
gross = basic + da + hra
netpay = gross - pf 
print(gross,"\n",netpay)