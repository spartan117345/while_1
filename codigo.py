# input
print("==============================================")
print("=========suma de los n primeros numeros=======")
print("==============================================")

n=int(input("dijite el valor de n: "))

# processing

s=0
i=1

while i <= n:
    s = s + i
    i = i + 1

print("==============================================")
print("la suma de los "+ str(n)+"primeros numeros naturales es: "+ str(s))
print("==============================================")
