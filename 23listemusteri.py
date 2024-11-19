musteriler=["a","b","c"]
musterilerYeni=musteriler[:]
print(musterilerYeni) # ['a', 'b', 'c']
print(id(musterilerYeni)) # 140412111111296
musteriler.pop() 
print(musteriler) # ['a', 'b']