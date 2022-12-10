
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
  end_of_row = number_of_columns - 1

  #Walk the rows
  for x in range(number_of_rows):
    largest_tree = grid[x][0]
    add_to_set(trees, x, 0) #Make the perimeter visible
    for y in range(number_of_columns):
      if grid[x][y] > largest_tree:
        largest_tree = grid[x][y]
        add_to_set(trees, x, y)

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

    largest_tree = grid[number_of_rows -1][y]
    add_to_set(trees, number_of_columns -1, y)
    for x in reversed(range(number_of_rows)):
      if grid[x][y] > largest_tree:
        largest_tree = grid[x][y]
        add_to_set(trees, x, y)

  return trees


def compute_site_lines(trees, grid):
  sight_lines=list()
  max_x = len(grid[0])-1
  max_y = len(grid)-1

  for tree in trees:
    tx,ty = tree.split(",")
    tree_x = int(tx)
    tree_y = int(ty)
    height = grid[tree_x][tree_y]
    right,left,up,down = 0,0,0,0

    if tree_x == 0 or tree_y == 0:
      sight_lines.append(0)
      continue

    grid_width = len(grid[0])
    grid_height = len(grid)

    for y in range(tree_y+1, grid_width):
      if grid[tree_x][y] < height:
        right+=1
      if grid[tree_x][y] >= height:
        right += 1
        break

    for y in reversed(range(0, tree_y)):
      if grid[tree_x][y] < height:
        left += 1
      if grid[tree_x][y] >= height:
        left += 1
        break

    for x in reversed(range(0, tree_x)):
      if grid[x][tree_y] < height:
        up += 1
      if grid[x][tree_y] >= height:
        up += 1
        break

    for x in range(tree_x+1, grid_height):
      if grid[x][tree_y] < height:
        down += 1
      if grid[x][tree_y] >= height:
        down += 1
        break

    sight_score = right * left * up * down
    sight_lines.append(sight_score)

  return sight_lines


def run():
  with open('input_day8.txt') as f:
    b = f.read().splitlines()
  f.close()

  grid = build_grid(b)
  trees = see_the_trees(grid)
  print("trees", len(trees))

  sight_lines = compute_site_lines(trees, grid)
  print("sight lines", max(sight_lines))

if __name__ == '__main__':
  run()