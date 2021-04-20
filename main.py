# def print_formatted(number):
#     # your code goes here
#     for number1 in range(1, number + 1):
#       decimal = number1
#       hexical = hex(number1)
#       binary = bin(number1)
#       octal = oct(number1)  
#       print(decimal, (octal[2:]).just(), hexical[2:].upper(), binary[2:])

# # def print_formatted(number):
#   list1 = []
#   result1 = []
#   for i in range(1, number + 1):
#     list1.append(i)
  
#   for i in list1:
#     hexical = hex(i)
#     binary = bin(i)
#     octal = oct(i)  
#     t = (f"{i},{octal[2:]},{(hexical[2:]).capitalize()},{binary[2:]}")
#     result1.append((t))



#   for l in result1:
#     print(("".join(l)).replace(",", " "))
    
# def print_formatted(number):
#   list1 = []
#   for i in range(1, number + 1):
#     list1.append(i)
  
#   for i in list1:
#     hexical = hex(i)
#     binary = bin(i)
#     octal = oct(i)  
#     p = (f"{i},{octal[2:]},{(hexical[2:]).capitalize()},{binary[2:]}")
#     print (p.replace(",", "  "))


def print_formatted(number):
    w = len(str(bin(number)).replace('0b',''))
    for i in range(1,number+1):   
        d = str(i).rjust(w,' ')
        b = bin(i)[2:].rjust(w,' ')   ## rjust is used for line alignment
        o = oct(i)[2:].rjust(w, ' ')
        h = hex(i)[2:].rjust(w, ' ').upper()
        print(d, o, h, b)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# print(print_formatted(15))



