def swap_ends(my_str):
  first = my_str[0]
  last = my_str[-1]
  middle = my_str[1:-1]
  new_str = last + middle + first
  return new_str

print(swap_ends('Hello-World'))


def swap_ends_efficient(my_str):
    return my_str[-1] + my_str[1:-1] + my_str[0]

print(swap_ends_efficient('Hello-World'))
