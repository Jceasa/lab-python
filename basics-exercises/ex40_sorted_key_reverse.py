# Ordene uma lista de palavras por tamanho (usando key=len).

words = ['Wuxia',"Xinxia","Fantasy","Urban","Terror"]

sorted_list_with_reverse_true = sorted(words , reverse=True)
sorted_list_with_reverse_false = sorted(words , reverse=False)
sorted_list_with_key = sorted(words , key=len)

print(*sorted_list_with_reverse_true) # reserve=true
print(*sorted_list_with_reverse_false) # reserve=false
print(*sorted_list_with_key) # key=len
