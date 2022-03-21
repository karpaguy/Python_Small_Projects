# Peguei esse código no stackoverflow, apenas para testar a forma que as funções pegam em python.

def fun1():
    fun1.var = "String."
    print(fun1.var)

def fun2():
    print(fun1.var)

fun1()
fun2()

print(fun1.var)