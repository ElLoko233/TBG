# main.py
from TBG.CMD import Cmd
from TBG.level import Level
from TBG.room import Room
from TBG.player import Player, NPC, Enemy
from TBG.item import Food, Scroll, Enhancement, Armor
from TBG.fight_move import Fight
from TBG.default_help import def_ex_help, def_bat_help

# ─────────────────────────────────────────
#  FIGHT MOVES
# ─────────────────────────────────────────

punch = Fight("Punch", style="Normal", damage=20)
punch.desc = "A solid right hook"
punch.atck_desc = [
    "You land a heavy punch on the enemy!",
    "Your fist connects with a satisfying crack!",
]

slash = Fight("Slash", style="Shadow", damage=35)
slash.desc = "A dark energy blade slash"
slash.atck_desc = [
    "You slice through the air with shadow energy!",
    "A crescent of dark force tears through the enemy!",
]

ghost_wail = Fight("Ghost_Wail", style="Spirit", damage=25)
ghost_wail.desc = "A chilling spectral scream"
ghost_wail.atck_desc = [
    "The ghost lets out a soul-piercing wail!",
    "A horrifying screech rattles your bones!",
]

ghost_grab = Fight("Ghost_Grab", style="Spirit", damage=15)
ghost_grab.desc = "Icy spectral hands reach for you"
ghost_grab.atck_desc = [
    "Cold ghostly hands lunge at you!",
    "You feel icy fingers grasp your soul!",
]

# ─────────────────────────────────────────
#  ITEMS
# ─────────────────────────────────────────

health_potion = Food("Health_Potion", regeneration=40)
health_potion.desc = "A glowing red vial. Restores 40 HP."

shadow_scroll = Scroll("Shadow_Scroll")
shadow_scroll.desc = "Ancient scroll crackling with dark energy. Teaches shadow moves."
shadow_scroll.fight_moves = {slash.name: slash}

dumbbell = Enhancement("Iron_Dumbbell", style="Normal", damage_increase=10)
dumbbell.desc = "Old rusty dumbbells. Boosts Normal-style moves by +10 damage."

chest_armor = Armor("Knight_Chest", defence=10)
chest_armor.desc = "A dusty old chest plate. Provides solid defence."

candle = Food("Candle", regeneration=5)  # flavour item with tiny regen
candle.desc = "A half-melted candle. Not very nutritious but desperate times..."

# ─────────────────────────────────────────
#  ROOMS
# ─────────────────────────────────────────

entrance = Room("Entrance_Hall")
entrance.desc = (
    "You stand in the crumbling entrance hall of the Blackwood Mansion.\n"
    "Cobwebs hang from the chandelier. The air smells of dust and dread.\n"
    "Doors lead north to the Library and east to the Armory."
)

library = Room("Library")
library.desc = (
    "Rows of rotting bookshelves surround you.\n"
    "Moonlight filters through a broken window.\n"
    "Something ancient sits on the reading table..."
)

armory = Room("Armory")
armory.desc = (
    "Rusted weapons line the walls. A suit of armor stands in the corner.\n"
    "There's also a dusty old chest on the floor."
)

basement = Room("Basement")
basement.desc = (
    "The air is ice cold. Strange symbols are scratched into the stone floor.\n"
    "This must be where the ghost is anchored...\n"
    "There is no escape until you face what lurks here."
)

# Connect rooms
entrance.near_rooms = {library.name: library, armory.name: armory}
library.near_rooms = {entrance.name: entrance, basement.name: basement}
armory.near_rooms = {entrance.name: entrance}
basement.near_rooms = {}  # No escape from the boss room

# Place items in rooms
library.items = {shadow_scroll.name: shadow_scroll, candle.name: candle}
armory.items = {chest_armor.name: chest_armor, dumbbell.name: dumbbell}
entrance.items = {health_potion.name: health_potion}

# ─────────────────────────────────────────
#  NPCs
# ─────────────────────────────────────────

old_ghost = NPC("Old_Ghost")
old_ghost.text_opt = [
    "...*whispers* Turn back while you still can...",
    "The master of this house does not welcome the living...",
    "Find the Shadow Scroll if you wish to survive the basement...",
]

entrance.people = {old_ghost.name: old_ghost}

# ─────────────────────────────────────────
#  PLAYER
# ─────────────────────────────────────────

player = Player("Hunter", max_hp=100, defence=0)
player.backstory = (
    "You are a paranormal investigator hired to cleanse the Blackwood Mansion.\n"
    "Armed with only your wits and fists, you descend into the darkness.\n"
    "Rumour has it a powerful ghost guards the mansion's basement...\n"
    "Survive, and the reward will be yours."
)
player.fight_moves = {punch.name: punch}

# ─────────────────────────────────────────
#  ENEMY
# ─────────────────────────────────────────

phantom = Enemy("The_Phantom", hp=120, defence=5)
phantom.fight_moves = {ghost_wail.name: ghost_wail, ghost_grab.name: ghost_grab}

# ─────────────────────────────────────────
#  CMD OBJECTS  (exploration)
# ─────────────────────────────────────────

cmd_help      = Cmd("ex_help")
cmd_help.command_list = [r"(help)(\s*)", r"(how[\s]*to[\s]*play)(\s*)"]

cmd_goto      = Cmd("goto")
cmd_goto.command_list = [
    r"(goto|go to|enter|move to)(\s*)(?P<arg1>[\w\']*)",
]

cmd_look      = Cmd("look_around")
cmd_look.command_list = [
    r"(look around|examine room|look)(\s*)",
]

cmd_take      = Cmd("take_item")
cmd_take.command_list = [
    r"(take|pick up|grab)(\s*)(?P<arg1>[\w\']*)",
]

cmd_throw     = Cmd("throw")
cmd_throw.command_list = [
    r"(throw|discard|drop|throw away)(\s*)(?P<arg1>[\w\']*)",
]

cmd_examine   = Cmd("examine_item")
cmd_examine.command_list = [
    r"(examine|inspect|look at)(\s*)(?P<arg1>[\w\']*)",
]

cmd_inv       = Cmd("search_inv")
cmd_inv.command_list = [
    r"(search inventory|inventory|bag|search inv|inv)(\s*)",
]

cmd_stats     = Cmd("stats")
cmd_stats.command_list = [
    r"(stats|abilities|status)(\s*)",
]

cmd_story     = Cmd("my_story")
cmd_story.command_list = [
    r"(my story|backstory|back story|story)(\s*)",
]

cmd_learn     = Cmd("learn")
cmd_learn.command_list = [
    r"(learn|study|read)(\s*)(?P<arg1>[\w\']*)",
]

cmd_enhance   = Cmd("enhance")
cmd_enhance.command_list = [
    r"(enhance|train|use)(\s*)(?P<arg1>[\w\']*)",
]

cmd_show_move = Cmd("show_move")
cmd_show_move.command_list = [
    r"(show move|skill|show_move)(\s*)(?P<arg1>[\w\']*)",
]

cmd_equip     = Cmd("equip")
cmd_equip.command_list = [
    r"(equip|wear|put on)(\s*)(?P<arg1>[\w\']*)",
]

cmd_talk      = Cmd("talk")
cmd_talk.command_list = [
    r"(talk|speak|approach|talk to)(\s*)(?P<arg1>[\w\']*)",
]

cmd_eat       = Cmd("eat")
cmd_eat.command_list = [
    r"(eat|consume|drink|chow)(\s*)(?P<arg1>[\w\']*)",
]

cmd_proceed   = Cmd("proceed")
cmd_proceed.command_list = [
    r"(proceed|descend|go to basement|enter basement)(\s*)",
]

# ─────────────────────────────────────────
#  CMD OBJECTS  (battle)
# ─────────────────────────────────────────

cmd_attack    = Cmd("attack")
cmd_attack.command_list = [
    r"(attack with|attack|use|strike with)(\s*)(?P<arg1>[\w\']*)",
]

cmd_bat_help  = Cmd("battle_help")
cmd_bat_help.command_list = [r"(help)(\s*)"]

cmd_bat_stats = Cmd("stats")
cmd_bat_stats.command_list = [r"(stats|abilities|status)(\s*)"]

cmd_bat_move  = Cmd("show_move")
cmd_bat_move.command_list = [r"(show move|skill|show_move)(\s*)(?P<arg1>[\w\']*)"]

cmd_bat_eat   = Cmd("eat")
cmd_bat_eat.command_list = [r"(eat|consume|drink|chow)(\s*)(?P<arg1>[\w\']*)"]

# ─────────────────────────────────────────
#  LEVEL SETUP
# ─────────────────────────────────────────

level1 = Level()
level1.level_rooms = entrance
level1.explore_help = def_ex_help
level1.battle_help = def_bat_help

level1.command_variant = [
    cmd_help, cmd_goto, cmd_look, cmd_take, cmd_throw,
    cmd_examine, cmd_inv, cmd_stats, cmd_story, cmd_learn,
    cmd_enhance, cmd_show_move, cmd_equip, cmd_talk,
    cmd_eat, cmd_proceed,
]

# ─────────────────────────────────────────
#  GAME START
# ─────────────────────────────────────────

print("=" * 40)
print("   BLACKWOOD MANSION  — A TBG Adventure")
print("=" * 40)
print("\nType 'help' at any time to see available commands.")
print("Type 'look' to examine your surroundings.")
print("Type 'proceed' when you're ready to face the Basement...\n")

# Exploration phase
level1.explore_loop(player)

# ─────────────────────────────────────────
#  BOSS BATTLE
# ─────────────────────────────────────────

print("\n" + "==" * 20)
print("You descend the creaking stairs into the Basement...")
print("A bone-chilling figure materialises before you!")
print(f"\n  *** THE PHANTOM AWAKENS ***\n")
print("==" * 20 + "\n")

# Swap to battle commands
level1.command_variant = [
    cmd_attack, cmd_bat_help, cmd_bat_stats, cmd_bat_move, cmd_bat_eat,
]

result = level1.battle_loop(player, phantom)

# ─────────────────────────────────────────
#  ENDING
# ─────────────────────────────────────────

print("\n" + "==" * 20)
if result == 1:
    print("The Phantom dissolves into shadow with a final shriek.")
    print("The mansion shudders... then goes silent.")
    print("You walk out into the moonlight, victorious.")
    print("\n  *** YOU ESCAPED BLACKWOOD MANSION ***")
else:
    print("Darkness closes in around you...")
    print("The Phantom's laughter echoes through the halls forever.")
    print("\n  *** GAME OVER ***")
print("==" * 20)