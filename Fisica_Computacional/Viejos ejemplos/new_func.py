def Multi( arg1=0, arg2=0 , *vartuple ):
    "Multiplica todos los argumentos"
    produc=arg1*arg2
 
    for var in vartuple:
       produc=produc*var
 
    return produc
 
 
def fib(n):
    "Recibe un entero n, y entrega una lista con los números de fibonacci menores que n"
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
 
 
def SumLis(list):
    sum=0
    for i in list:
        sum=sum + i
 
    return sum
 
 
if __name__ == "__main__":
    a=fib(200)
    print('Serie de Fibonacci hasta el termino exactamente menor que 200: ',a)
    b=SumLis(a)
