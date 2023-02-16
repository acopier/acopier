# Created by newuser for 5.9
skip_global_compinit=1

# Window title

precmd_functions+=(set_win_title)
function set_win_title(){
    echo -ne "\033]0; $(basename "$PWD") \007"
}

# starship_precmd_user_func="setwintitle"

## ZSH

export HISTFILE=~/.zshistory
export HISTSIZE=100
export SAVEHIST=$HISTSIZE
export PATH="/home/filip/.local/bin":$PATH

setopt correct
## aliases

alias nv='nvim'
alias cls='clear'
alias ffetch='fm6000 -l 8 -m 1 -d qtile -f ~/Pictures/artix-ascii -c cyan'
# alias qtile='qtile start'
# compadd -u doas
alias ytdl-music='youtube-dl -i -x --add-metadata --audio-quality 0 -o "%(uploader)s | %(title)s.%(ext)s"'

## Keyboard

bindkey ";5C" forward-word
bindkey ";5D" backward-word
bindkey ";2D" beginning-of-line
bindkey ";2C" end-of-line

## commands

ufetch

#autoload -Uz vcs_info
#precmd() { vcs_info }
#setopt PROMPT_SUBST
#PROMPT='%n in ${PWD/#HOME/~} ${vcs_info_msg_0_} %{$fg_bold[white]%}>%{$reset_color%}'

#source ~/.config/zsh/plugins/zsh-autocomplete/zsh-autocomplete.plugin.zsh

source ~/.config/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /home/filip/.config/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /home/filip/.config/zsh/plugins/powerlevel10k/powerlevel9k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
