if status is-interactive
    # Commands to run in interactive sessions can go here
end

complete -c doas

function fish_greeting
	ufetch
end
function cls
	clear $argv
end

export RANGER_LOAD_DEFAULT_RC=false
