mentions = [['Annabeth', 'Percy', 'Percy', 'Grover'],
            ['Percy', 'Annabeth', 'Percy', 'Chiron'],
            ['Percy', 'Clarisse', 'Grover'],
            ['Percy', 'Percy', 'Annabeth', 'Percy', 'Grover']]

def count_add_percy(pages):
   for page in range(len(pages)):
      count = 0
      for name in pages[page]:
         if name == "Percy":
            count += 1
         pages[page].append(count)
   return pages

count_per_line = count_add_percy(mentions)
for line in count_per_line:
    print(line)


    




