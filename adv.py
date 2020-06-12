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
traversal_path = []


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
opposite = {
    s: 'n',
    n: 's',
    e: 'w',
    w: 'e'
}


def go_backwards(backwards_list):


if __name__ == '__main__':
    print('hi')
    print(player.current_room.get_exits())
    # traversal_path

    stack = []
    go_back = []
    go_back_inner = []
    # cache holds the value of untested directions
    cache = {}

    cache[player.current_room.id] = player.current_room.get_exits()
    stack.append(cache[player.current_room.id])
    # player.current_room.id
    # player.current_room.get_exits()
    while len(stack) > 0:
        # players current room id
        room_id = player.current_room.id
        # check that cache[room_id] has locations to go.
        if len(cache[room_id]) > 0:
            directions = stack.pop()
            # this should be unneccasary code with the if check above.
            # while len(directions) == 0:
            #     directions = stack.pop()
            #     go_backwards(go_back.pop())
            direction = directions.pop(0)
            if len(directions) > 0:
                stack.append(directions)
            room_id = player.current_room.id
            if room_id in cache:
                # this way will be searched later dont go this way
                # remove direction from future room
                cache[room_id].remove(opposite_direction)
                # if go_back_inner len is greater then 1 then we need to call the function to go backwards.
                if len(go_back_inner) > 0:
                    go_backwards(go_back_inner)
                    # go_back_inner set back to empty as we have went backwards
                    go_back_inner = []
            else:
                traversal_path.append(direction)
                opposite_direction = opposite[direction]
                go_back_inner.append(opposite_direction)
                player.travel(direction)
                rooms = player.current_room.get_exits()
                rooms.remove(opposite_direction)
                if len(rooms) > 0:
                    cache[room_id] = rooms
                    stack.append(cache[room_id])
                else:

                    # go back **TODO**
        else:
            # go back

            # First we append the first rooms get exits
            # then we do a loop for as long as as len(stack) > 0
            # we append the first direction priortizing n
            # we also hold a cache of all visited locations
            # first n, s, w, and lastly e.
            # we also hold another array which is a stack
            # as well that holds the directions we take and pops off
            # when needing to go backwards.
