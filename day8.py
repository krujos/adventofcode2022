
def build_grid(buffer):
  if buffer = None



  grid = list()
  [grid.append(list(row)) for row in buffer]
  return grid

def run():
  with open('input_day8.txt') as f:
    b = f.read().splitlines()
  f.close()

  grid = build_grid(b)

  for row in grid:
    print(row)

if __name__ == '__main__':
  run()