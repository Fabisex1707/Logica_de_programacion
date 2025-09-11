#Operaciones con cadenas 
my_first_cadena=".-.-   - -"
print(my_first_cadena)
my_first_cadena=" "
list_morse=[]
list_morse.append(my_first_cadena.strip())
print(list_morse)
my_first_cadena="                   Hola papup."
print(my_first_cadena)
print(my_first_cadena.strip(" p,."))#letras a eliminar al final y al inicio de la cadena
print(my_first_cadena.lstrip(" p,."))#elimina los eapcios o letras del lado izq
print(my_first_cadena.rstrip(" p,."))#elimina los eapcios o letras del lado derecho
my_second_cadena=my_first_cadena #copia de cadenas
print(my_first_cadena)
print(my_second_cadena)
print(''.join((my_first_cadena.strip(" p,.")).upper())) # denrto del texto donde se gaurdara el texto, debes de poner el formato, por ejemplo, [,-./|" "]
lista_nombres=["Fabi          ","Olga","Viole","pedro"]
print(', '.join(((nombre.strip()).upper() for nombre in lista_nombres)))#aplicamos formato en cada uno de los nombres dentro de la lista con .strip() y .upper()
print(', '.join(((nombre.strip()).upper() if len(nombre.strip())>4  else "corto" for nombre in lista_nombres )))#ademas del formato etiquetamos los nombres que son menores 4 caracteres como cortos
# si quiero poner un if...esle debe ser antes del for
my_first_cadena=" "
print(''.join((letra for indice,letra in enumerate(my_first_cadena.strip()) if letra!=" " or my_first_cadena.strip()[indice+1]!=" ")))
list_morse=[]
list_morse.append(''.join((letra for indice,letra in enumerate(my_first_cadena.strip()) if letra!=" " or my_first_cadena.strip()[indice+1]!=" ")))
print(list_morse)

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        if -100<= num1 <=100 and -100<= num2 <=100:
            return num1 + num2

suma=Solution()
print(suma.sum(100,101))

def longestSubarray(nums: list) -> int:
    mayor=max(nums)
    max_len,counter=0,0
    for i in nums:
        if mayor==i:
            counter+=1
            max_len=max(max_len,counter)
        else:
            counter=0
    return max_len

print(longestSubarray([4,1,2,3,4,4]))



def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        new_array=[]
        new_array.extend(nums1)
        new_array.extend(nums2)
        len_array=len(new_array)
        new_array.sort()
        if len_array%2!=0:
            return new_array[(len_array//2)]
        else:
            return (new_array[(len_array//2)-1] + new_array[(len_array//2)])/2

print(findMedianSortedArrays([1,2,3],[4,2,5]))

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    left=0
    max_number_list=list()
    if k>1 or len(nums)>1:
        nk=k-1
    else:
        return nums[0]
    for right in range(len(nums)-nk):
        max_number_list.append(max(nums[left:right+k]))
        left+=1
    return max_number_list

print(maxSlidingWindow())


    

    

