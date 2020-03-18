def skip_elements(elements):
  # code goes here
  valid_elements=[]
  for element in range(0,len(elements),2):
    valid_elements.append(elements[element])
  return valid_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []