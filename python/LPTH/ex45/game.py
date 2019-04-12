#!/usr/bin/python
from room import room
from player import player

print "Welcome! Please enter your name below"
my_name = raw_input("Name: ")
my_player = player(my_name)

shore_scene= """
shore
"""

forest_scene="""
forest
"""

clif_scene="""
clif
"""

room1 = room("Shoreline", shore_scene)
room2 = room("Forest", forest_scene)
room3 = room("Clif", clif_scene)

print "%s, you were just on an amazing cruise, but the ship was poorly managed. " % my_player.whoami()
print "As a result the crew was not taken care of and in turn did not take work hard"
print "or take care of the ship, the culmination of these efforts, or lack thereof"
print "lead to the ship running into troublesome waters and no one took any of the"
print "appropriate measures, therefore it was destoryed and lost at sea."
print "You somehow managed to get to an deserted island and pass out from exhaustion."
print "There endless %s to your right, a dense %s up ahead, and steep rock %s to your left." % ( room1.getName(), room2.getName(), room3.getName() )

while True:
	print "Which way do you go?"
	next_room = raw_input("> ")
