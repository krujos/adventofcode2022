
def build_grid(buffer):
  grid = list()
  if buffer == None:
    grid.append(list("30373"))
    grid.append(list("25512"))
    grid.append(list("65332"))
    grid.append(list("33549"))
    grid.append(list("35390"))
    return grid
  
  [grid.append(list(row)) for row in buffer]
  return grid

def run():
  with open('input_day8.txt') as f:
    b = f.read().splitlines()
  f.close()

  #grid = build_grid(b)
  grid = build_grid(None)

  for row in grid:
    print(row)

if __name__ == '__main__':
  run()