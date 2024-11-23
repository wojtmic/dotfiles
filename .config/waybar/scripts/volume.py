#!/bin/python3

import subprocess

def get_volume():
    # to check volume we use wpctl get-volume @DEFAULT_AUDIO_SINK@
    volume = subprocess.check_output(["wpctl", "get-volume", "@DEFAULT_AUDIO_SINK@"], text=True).split()[1]
    return float(volume)

def main():
    numberVolume = get_volume() * 100
    icons = ["", "", ""]
    icon = "?"
    if numberVolume < 33:
        icon = icons[0]
    elif numberVolume < 66:
        icon = icons[1]
    else:
        icon = icons[2]

    print(f"{icon} {numberVolume:.0f}%")

main()
