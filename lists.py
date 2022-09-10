#this code calculates an average of input integers using list
numlist = list()

while True:
  inp = input('enter a number:')
  if inp == 'done': break
  num = float(inp)
  numlist.append(num)

average = sum(numlist)/len(numlist)
print(average)
