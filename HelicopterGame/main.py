# CELL_TYPES = "🟩🌳🌊🏥🏬⛈️"

from map import Map
import time
import os
from helicopter import Helicopter as Helico
from pynput import keyboard
from clouds import Clouds

TICK_SLEEP = 0.1
TREE_UPDATE = 100
FIRE_UPDATE = 50
CLOUDS_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)


MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1),}

def process_key(key, injected):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx = MOVES[c][0]
        dy = MOVES[c][1]
        helico.move(dx, dy)


listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

tick = 1

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print("TICK", tick)
    tick +=1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()
    