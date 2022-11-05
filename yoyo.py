def toggle_corner(corner : tuple , n: int , m: int) -> tuple:
  row = 0
  column = 0
  if corner[0] :
    row = 0
  else:
    row = n-1

  if corner[1]:
    column = 0
  else :
    column = m-1
  return (row , column)

def find_longest_path(position : tuple , n : int , m : int):
  is_left = True if position[1] < m/2 else False
  column = 0 if is_left else m
  row = 0 if position[0] > n-1 - position[0] else n
  print(is_left)
  corner = tuple((row, column))
  other_corner = toggle_corner(corner, n , m )
  print(corner)
  print(other_corner)
  # distance to closer corner (named corner) *2 + distance to further corner (other corner)
  length = 2 * (abs(position[0] - corner[0]) + abs(position[1] - corner[1])) + abs(position[0] - other_corner[0]) + abs(position[1] - other_corner[1])
  return length

print(find_longest_path((2,1),4,7))

