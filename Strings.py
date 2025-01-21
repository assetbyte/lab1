a = "Hello world"
print(a[2:5]) #from first L to O (5 is not included)

b = "Hello world"
print(b[:5]) #from start till the 5(not included)

c = "Hello world"
print(b[2:]) #from the 2 position 

d = "Hello, World!"
print(d[-5:-2])

e = "Hello, world"
print(a.upper()) #might be lower

f = " Hello, world "
print(f.strip())

g = "Jello, World"
print(g.replace("J","H"))

h = "Hello, world"
print(h.split('w'))

i = "Hello"
j = "World"
print(i+j)
k = i+" "+j
print(k)

#f strings
age = 36
txt = f"My name is John, I'm {age} years old"
print(txt)

price = 59
text = f"The price is {price:.3f}"
print(text)

sentence = "We are the so-called \"Vilings\""
print(sentence)


