from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# traversal_path.append('n')

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

if __name__ == '__main__':
    print('hi')
    print(player.current_room.get_exits())
    # traversal_path

    stack = []
    cache = {}

    stack.append(cache[player.current_room.id])
    # player.current_room.id
    # player.current_room.get_exits()
    while len(stack) > 0:
        directions = stack.pop()
        direction = directions.pop(0)
        traversal_path.append(direction)
        stack.append(directions)
        # cache holds the value to get back to start.
        cache[player.current_room.id] = direction
    # player.travel(direction)

    # my strategy is to completely destroy this project!
    # under 1000 moves!
    # First we append the first rooms get exits
    # then we do a loop for as long as as len(stack) > 0
    # we append the first direction priortizing n
    # we also hold a cache of all visited locations
    # first n, s, w, and lastly e.
    # we also hold another array which is a stack
    # as well that holds the directions we take and pops off
    # when needing to go backwards.
