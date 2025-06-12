# Multiline Input from user


para=[]
# Getting input from user ^
print("Enter a para:")
#While loop Start
while True:
 line=input()
 if line:
  para.append(line)
 else:
  break
print(para)
output=("\n".join(para))
print(output)

