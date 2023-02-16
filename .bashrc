#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && # return
	source 

# alias ls='ls --color=auto'
# PS1='[\u@\h \W]\$ '

# doas command completion
complete -cf doas

export PATH="/home/filip/.local/bin:$PATH"

ls='ls -G'
alias nv='nvim'
alias cls='clear'
alias ffetch='fm6000 -l 8 -m 1 -d qtile -f ~/Pictures/artix-ascii -c cyan'
alias Dmenu='$HOME/.local/bin/Dmenu'

bind 'set show-all-if-ambiguous on'
bind 'TAB:menu-complete'

ufetch
# alias ytdl-music='youtube-dl -i -x --add-metadata --audio-quality 0 -o "%(uploader)s | %(title)s.%(ext)s"'
