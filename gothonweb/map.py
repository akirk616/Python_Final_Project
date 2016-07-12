class Room(object):
	
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		
	def go(self, direction):
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
		
kickoff = Room("Kickoff",
"""
It is the start of the game
Your whole family is in the crowd
Your team made it to the last round of the playoffs
This is the championship!! Win the Game or it might be your last.
You are set to return the kickoff
You catch the ball and look up field
There seems to be a hole right through the middle off the field
There are defenders being blocked to your left and right
What do you do?(run through the middle, make own hole, cheat)
""")


kicker = Room("Kicker",
"""
You out run everybody but the kicker
There is space between you and the kicker
He looks to be about 5 feet tall and nothing more than 110 pounds
You can juke, run through, or attempt to run around him
How do you attemp to reach the endzone?
""")


defense = Room("Defense",
"""
Fast forward to the forth quarter
Both teams seem to be equally matched
The game is tied up with 2 minutes left
it is 4th and 5 and you're on defense. You need a stop!
your coach folds under pressure and tells you to call the defensive play
You can run zone, man defense, or you can send an all out blitz
What do you choose? The game is in your hands.
""")


offense = Room("Offense",
"""
You successfuly stopped the oppenents offensive drive
That was clutch!
You still have to score to win the game
Your coach left the game to change his underwear so once again the call is on you
YOU MUST SCORE TO WIN!
you are on the 50 ysrd line with 30 seconds left. You can run the ball, screen pass, or hail mary pass
What playcall will make your team CHAMPIONS?!
""")


the_end_champions = Room("The End",
"""
You chose to run a halfback screen
you line up to the right side of the quarterback
He hikes the ball, as you pretend to block
soon as the linemen and linebackers are heading for the qb you let go of your block and await the pass
The quarterback flicks the pass your way and you catch it and run like you're being chased by a dog
You jet past everyone. You run in the endzone, past it, over the fense, and ontop of someone car where you scream for help
'Please help''Get your dog' becomes your very own personal slogan at events
You are forever remember as the guy who imagined the dog on the field during the championship game
'Hey isn't that the crazy dog guy from the championship game''He won us the game'
You won the championship! You carried your team to glory
You are now the man around town
You get whatever you want. For Free
Thats the life of a champ
""")


failure = Room("The End",
"""
You lost.  You lost the championship. \nYou go home to faces of disappointment
""")


offense_lost1 = Room("Lost",
"""
You chose to run
The playcall is an outside run to the right
Your lineman are blocking perfectly getting pancakes you go 10 yards untouched
You look upfield to realize there is only one person preventing you from scoring
You realize that its the kicker looking for revenge
For the whole game he has been on the side line getting stronger and taking steroids
He now appears to be 7 feet tall and about 300 pounds of all muscle
To get by him you try the tap dance routine again but her doesn't fall for the heel to toe tap again
he flexes all his muscles and taps you in the middle of your shoulder pads with his index finger
With that one powerful touch he completely rips off all of you equipment, knocks the air out your lungs, \n and stops your heart
He is later convicted for murder in the first degree
""")


offense_lost2 = Room("Lost",
"""
You line all the recievers up for a hail mary pass
the quarterback hikes the ball
the recievers are in the endzone when the quarterback cocks back and launches the ball
The ball goes 30 feet into the air before in soars down to earth
the ball comes down and lands in the hands of a kid in the seats of the stadium
The quarterback has no accuracy past 5 yards
""")


offense.add_paths({
    'screen pass': the_end_champions,
    'run': offense_lost1,
    'hail mary pass': offense_lost2
})


kickoff_lost1 = Room("Lost",
"""
You decide to run where there are no blockers
you run five yards before all 11 players tackle you at once
You are hit so hard you fumble
The opponents recover the ball
Your coach sits you out for the rest of the game out of anger
You stand on the sidelines the entire game watching your team get pumbled
""")


kickoff_lost2 = Room("Lost",
"""
You were talked into bringing an identical ball on the field"
IDK where you hide it but the refs dont notice it."
You allow you teamate to get tackled while you take off running with the identical ball"
You score. The refs and teams are confused but 6 points are added to the board"
You go on to win the Championship."
While the other team watches film they realize that there were two balls on the field. \nYou and your team is banned from playing football for life. \nThe championship is awarded to the other team.
""")


kicker_lost1 = Room("Lost",
"""
Suprisingly the kicker is also the starting middle linebacker
He is the hardest hitter on the team
He hits you so hard your pinky toe falls out you nose
While you try to figure out hoe this is possible in the emergency room
He himself injures the entire rest of your team include the coaching staff
""")


kicker_lost2 = Room("Lost",
"""
rumors around town is that the kicker is Usain Bolts long lost brother
You attemps to beat him in a leg race
he runs so fast he accidently runs past you and has to backtrack to make the tackle
he runs so fast that when he catches up to you he changes the timeline.
You are now in 2088
""")


defense_lost1 = Room("Lost",
"""
You scream out zone to alert you teamates of the defensive play call.
The winds blowing hard and everyone instead hears 'gone'
it wasn't before the oponents were in the endzone celebrating before your team was on the bus
Everyone blames you for screaming out the play call
They kick you off the bus and make you walk back home
You are kidnapped and now you are a clown at the circus racing on a child tricycle
""")


defense_lost2 = Room("Lost",
"""
You scream 'GO GETTEM' from the top of your lungs
This send everyone on the team to attack the quarterback
Even the bench ran on the field to tackle the quarterback
The good thing is the quarter back is tackle and the team successfully stopped the play
The bad part is the quarterback didnt snap the ball yet
Your whole team is ejected from the game
This starts a riot where people fight and throw things onto the field
You are hit with popcorn and the butter gets in your eyes
You attemp to fight back swing at the air until you run into the field goal post and pass out
""")


defense.add_paths({
    'run zone': defense_lost1,
    'blitz': defense_lost2,
    'run man': offense
})

kicker.add_paths({
    'juke': defense,
    'run through': kicker_lost1,
    'run around': kicker_lost2
})

kickoff.add_paths({
    'make own hole': kickoff_lost1,
    'cheat': kickoff_lost2,
    'run through the middle': kicker
})

START = kickoff
