#!/usr/bin/env python3

import argparse
import engine.keycodes
from engine.parser import buttery_parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description = "Parse Buttery Engine JSON definition to a QMK compatible keymap"
    )
    parser.add_argument(
        "input",
        metavar = "input",
        type = str,
        help = "Path to the input JSON"
    )
    args = parser.parse_args()

    with open('engine/template_h.txt', 'r') as file:
        template_h = file.read()

    with open('engine/template_c.txt', 'r') as file:
        template_c = file.read()

    result = buttery_parser(args.input)

    keymap_h = template_h.format(
        includes = result["includes"],
        keycodes = result["keycodes"],
        pseudolayers = result["pseudolayers"],
        keyboard_parameters = result["keyboard_parameters"],
        keymaps = result["keymaps"],
        buffers = result["buffers"]
    )

    keymap_c = template_c.format(          
        chords = result["chords"],
        leader_sequences = result["leader_sequences"]
    )
    
    with open('introspection.h', 'w') as file:
        file.write(keymap_h)
    
    with open('introspection.c', 'w') as file:        
        file.write(keymap_c)
   

    print("Finished!")
