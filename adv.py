from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = []

# First we append the first rooms get exits
# then we do a loop for as long as as len(stack) > 0
# we append the first direction priortizing n
# we also hold a cache of all visited locations
# first n, s, w, and lastly e.
# we also hold another array which is a stack
# as well that holds the directions we take and pops off
# when needing to go backwards.

opposite = {
    's': 'n',
    'n': 's',
    'e': 'w',
    'w': 'e'
}


def go_backwards(backwards_list):
    backwards_list.reverse()
    for direction in backwards_list:
        player.travel(direction)
        traversal_path.append(direction)


def test_loop(backwards_list):
    possible_directions = {}
    for x in backwards_list:
        if x in possible_directions:
            possible_directions[x] += 1
        else:
            possible_directions[x] = 1
    if 'n' in possible_directions and 's' in possible_directions and 'e' in possible_directions and 'w' in possible_directions:
        if possible_directions['n'] == possible_directions['s'] and possible_directions['e'] == possible_directions['w']:
            return True
    return False


stack = []
go_back = []
go_back_inner = []
# cache holds the value of untested directions
cache = {}

cache[player.current_room.id] = player.current_room.get_exits()
stack.append(cache[player.current_room.id])
while len(stack) > 0:
    # players current room id
    room_id = player.current_room.id
    # check that cache[room_id] has locations to go.
    if room_id in cache:
        if len(cache[room_id]) > 0:
            directions = stack.pop()
            # if len(directions) > 1:
            #     direction = directions.pop(1)
            # else:
            direction = directions.pop(0)
            if len(directions) > 0:
                stack.append(directions)
            # move our player
            player.travel(direction)
            # get the opposite direction
            opposite_direction = opposite[direction]
            # get the room player is in
            room_id = player.current_room.id
            if room_id in cache:
                # this way will be searched later dont go this way
                # remove direction from future room
                cache[room_id].remove(opposite_direction)
                #
                go_back_inner.append(opposite_direction)
                test = test_loop(go_back_inner)
                if test:
                    traversal_path.append(direction)
                    go_back_inner = []
                else:
                    go_back_inner.pop()
                    # go back to original position
                    player.travel(opposite_direction)
                    # if go_back_inner len is greater then 1 then we need to call the function to go backwards.
                    if len(go_back_inner) > 0:
                        go_backwards(go_back_inner)
                        # go_back_inner set back to empty as we have went backwards
                        go_back_inner = []
            else:
                # append the direction
                traversal_path.append(direction)
                # append opposite direction to inner backwards array
                go_back_inner.append(opposite_direction)
                # get new rooms
                rooms = player.current_room.get_exits()
                # remove the direction we just came from.
                rooms.remove(opposite_direction)
                # if length is 1 then we dont need to come back to this node
                # so we can actually keep adding to the inner go back list
                if len(rooms) == 1:
                    # add room_id to cache with the list of rooms
                    cache[room_id] = rooms
                    # append to the stack.
                    stack.append(cache[room_id])
                elif len(rooms) > 1:
                    # add room_id to cache with the list of rooms
                    cache[room_id] = rooms
                    # append to the stack.
                    stack.append(cache[room_id])
                    # this is a location we will need to come back to append the inner array and set it to an empty array.
                    go_back.append(go_back_inner)
                    go_back_inner = []
                else:
                    # no rooms to go to time to go backwards and set back inner to an empty list
                    if len(stack) > 0:
                        go_backwards(go_back_inner)
                        go_back_inner = []
        else:
            go_backwards(go_back.pop())
    else:
        stack.pop()
    # clean stack
    for i in reversed(range(len(stack))):
        # reverse loop to avoid index out of range
        if len(stack[i]) == 0:
            stack.pop(i)

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
