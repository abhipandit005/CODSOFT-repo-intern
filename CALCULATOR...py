num1 = float(input("enter first no."));
num2 = float(input("enter second no."));
op = input("enter the operator like +,-,/,*");
if(op=='+'):
    res = num1+num2;
    print(res);
elif(op=='-'):
    res = num1-num2;
    print(res);
elif(op=='*'):
    res = num1*num2;
    print(res);
elif(op=='/'):
    res = num1/num2;
    print(res);    