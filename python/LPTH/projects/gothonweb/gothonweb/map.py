class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
	
	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
The Gothons of PLanet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last urviving memeber and you last
mission is to get the neutron destuct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an
escape pod.

You're running down the central corridor to the Weapons Amrory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body. He's blocking the door to the
Armory and about to pull a weapon and blast you.
""")

laser_weapon_armory = Room("Laster Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laught and can't move.
While he's laughting you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.
""")

the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
bdirge where you must place it in the right spot.

You burst onto the Bridge with the neutron destruct bomb
under you arm and surprise 5 Gothons who are trying to
take control of the ship. Eash of the has an even uglier
clown costume than the last. They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
""")

escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.
You inch backward to the door, open it, and then carfully
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the clsoe button
and blast the lock so the Gothons can't get out.
Now that the vomv is placed you run to the escape pod to
get off this tin can.

You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes. It sems lik
hardly any Gothons are on the ship, so your run is clear of
interference. You get to the chamber with the escape pods,
and now need to pick ont to take. Some of them could be damaged
but you don't have time to look. There's 5 pods, which one
do you take?
""")

the_end_winner = Room("The End",
"""
You rump into pod 2 and hit the eject button.
The pod easily slides out into space heading to
the planet below. As if flies to the planet, you look
back and see your shop implode then explode like a
bright star, taking out the Gothon ship at the same
time. You won!
""")

the_end_loser = Room("The End",
"""
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
impoeds as the hull ruptures, crushing your body
into jam jelly.
"""
)

escape_pod.add_paths({
	'2': the_end_winner,
	'*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
	'throw the bomb':generic_death,
	'slowly place the bomb':escape_pod
})

laser_weapon_armory.add_paths({
	'0132': the_bridge,
	'*': generic_death
})

central_corridor.add_paths({
	'shoot!': generic_death,
	'dodge!': generic_death,
	'tell a joke': laser_weapon_armory
})

START = central_corridor
