
def build_grid(buffer):
  grid = list()
  if buffer is None:
    grid.append(list("30373"))
    grid.append(list("25512"))
    grid.append(list("65332"))
    grid.append(list("33549"))
    grid.append(list("35390"))
    return grid

  [grid.append(list(row)) for row in buffer]
  return grid

def add_to_set(trees, x,y):
  trees.add(str(x)+ "," + str(y))


def see_the_trees(grid):
  trees = set()
  number_of_rows = len(grid)
  number_of_columns = len(grid[0])

  #Walk the rows
  for x in range(number_of_rows):
    largest_tree = grid[x][0]
    add_to_set(trees, x, 0) #Make the perimeter visible
    for y in range(number_of_columns):
      if grid[x][y] > largest_tree:
        largest_tree = grid[x][y]
        add_to_set(trees, x, y)

    end_of_row = number_of_columns -1
    largest_tree = grid[x][end_of_row]
    add_to_set(trees, x, end_of_row)
    for y in reversed(range(number_of_columns)):
      if grid[x][y] > largest_tree:
        largest_tree = grid[x][y]
        add_to_set(trees, x, y)

  #Walk the columns
  for y in range(number_of_columns):
    largest_tree = grid[0][y]
    add_to_set(trees, 0, y)
    for x in range(number_of_rows):
      if grid[x][y] > largest_tree:
        largest_tree = grid[x][y]
        add_to_set(trees, x, y)

    largest_tree = grid[number_of_rows -1 ][y]
    add_to_set(trees, number_of_columns -1, y)
    for x in reversed(range(number_of_rows)):
      if grid[x][y] > largest_tree:
        largest_tree = grid[x][y]
        add_to_set(trees, x, y)

  return trees


def run():
  with open('input_day8.txt') as f:
    b = f.read().splitlines()
  f.close()

  #grid = build_grid(b)
  grid = build_grid(None)

  # for row in grid:
  #   print(row)

  trees = see_the_trees(grid)
  print(sorted(trees))
  print(len(trees))


if __name__ == '__main__':
  run()