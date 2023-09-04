"""
def elevator_algorithm(floors, requests):

  This function implements an elevator algorithm.

  Args:
    floors: A list of floors.
    requests: A list of requests, where each request is a tuple of (start floor, end floor).

  Returns:
    A list of floors that the elevator should visit, in order.
 

  # Initialize the elevator at the first floor.
  current_floor = 0

  # Create a list to store the floors that the elevator should visit.
  floors_to_visit = []

  # Iterate over the requests.
  for start_floor, end_floor in requests:
    # If the elevator is already on the start floor, skip this request.
    if current_floor == start_floor:
      continue

    # If the start floor is lower than the current floor, go down.
    if start_floor < current_floor:
      for i in range(current_floor - start_floor):
        floors_to_visit.append(current_floor - 1)
        current_floor -= 1

    # If the start floor is higher than the current floor, go up.
    else:
      for i in range(start_floor - current_floor):
        floors_to_visit.append(current_floor + 1)
        current_floor += 1

    # Add the end floor to the list of floors to visit.
    floors_to_visit.append(end_floor)

  # Return the list of floors to visit.
  return floors_to_visit

  """
def elevator(floors, requests):

    current_floor = 0
    floors_to_visit = []
    
    