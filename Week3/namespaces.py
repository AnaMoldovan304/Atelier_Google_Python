# def my_function():
#     global msg
#     msg = 'Hello'
#     #print(msg)
#     return None
#
# #print(dir(my_function()))
# my_function()
# print(msg)
#
# #print(msg)

# def my_function():
#     def my_sec_function():
#         global msg
#         msg = 'Buna'
#         return None
#     my_sec_function()
#     print(locals(), 'locale la nivel de my function')
#     msg = 'Buna1'
#     print(f'functia principala {msg}')
#     return None

def functie2():
    #print(msg, '>>>>')
    total = 1
    return total

#my_function()
functie2()
#print(msg)
print(globals())
print(locals(), 'locale la nivel de function2 ')