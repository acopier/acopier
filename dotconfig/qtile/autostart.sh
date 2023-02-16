#!/bin/sh

## sound
pipewire &
pipewire-pulse &
wireplumber &
# mpd &

## extras
#picom --experimental-backends &
dunst &
udiskie -s -m nested &
