#!/bin/sh
alias Qtile='/usr/bin/python /usr/bin/qtile start'
[ -f ~/.xprofile ] && . ~/.xprofile &
[[ -f ~/.Xresources ]] && /usr/bin/xrdb -merge -I$HOME ~/.Xresources &
/usr/bin/setxkbmap cz -variant coder &
Qtile
