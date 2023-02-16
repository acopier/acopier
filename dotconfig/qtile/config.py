import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List

@hook.subscribe.startup_once 
def autostart():
    subprocess.run('/home/filip/.config/qtile/autostart.sh'),

mod = "mod4"
terminal = "kitty"
browser = "librewolf"
launcher = "/home/filip/.local/bin/DmenuBash"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "h", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "return", lazy.spawn("kitty"), desc="Launch kitty"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Internet Browser"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "mod1"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "mod1"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
#    Key([mod], "r", lazy.spawn("rofi -combi-modi window,drun,ssh,combi,run -show combi"), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("DmenuBash")),
    Key([mod], "s", lazy.spawn("scrot %Y-%m-%d-%s.png -e 'mv $f ~/Pictures/'"), desc="screenshot"),
    Key([mod], "l", lazy.spawn("i3lock -i /home/filip/.config/qtile/wp/bg.jpeg")),
]

# groups = [Group(i) for i in ["", "", "", "", "", ""]]
#groups = [Group(i) for i in ["1", "2", "3", "4", "5"]]
group_hotkeys = "123456789"

groups = [Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='max'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          ]
for g, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[g.name].toscreen(),
                desc="Switch to group {}".format(g.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(g.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(g.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #layout.Columns(border_focus_stack=["#c5c8c6", "#8f3d3d"], border_width=4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(           
           font = "JetBrainsMono Nerd Font Mono",
           margin = 2,
           border_focus="#ebdbb2", border_normal="#928374", border_width=2),
    layout.Max(
           font = "JetBrainsMono Nerd Font Mono",
             border_focus="#ebdbb2", border_normal="#928374", border_width=0),
    layout.Matrix(
        border_focus="#ebdbb2", border_normal="#928374", border_width=1,
        margin = 2),
#    layout.MonadTall(
#           font = "JetBrainsMono Nerd Font Mono",
#           margin = 4),
#    layout.MonadWide(
#           font = "JetBrainsMono Nerd Font Mono",
#           margin = 4),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(
        border_focus="#ebdbb2", border_normal="#928374", border_width=1,
        margin = 2),
]

widget_defaults = dict(
    font='JetBrainsMono Nerd Font',
    fontsize=13,
    padding=13,
    scroll=False,
    scroll_clear=True,
    scroll_repeat=True,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='~/.config/qtile/wp/bg.jpeg',
        wallpaper_mode='fill',
        
       top=bar.Bar(
            [
#                widget_defaults == dict(
#                    font = "JetBrains Mono",
#                    fontsize=14,
#                    padding=3,
#)
                widget.CurrentLayout(),
                widget.Sep(linewidth=1),
#                widget.Spacer(length=3),
                widget.GroupBox(highlight_method='line', disable_drag=True, highlight_color=['928374','282828'], urgent_border='cc241d', urgent_text='fb4934', this_current_screen_border='a89984', this_screen_border='ebdbb2', use_mouse_wheel=False),
#                widget.Spacer(length=3),
                widget.Sep(linewidth=1),
                widget.WindowName(format='{name}', max_chars=50),
                widget.Chord(
#                    chords_colors={
#                        "launch": ("#ff0000", "#ffffff"),
#                    },
#                   name_transform=lambda name: name.upper(),
                 ),
#                widget.TextBox("default config", name="default"),
#                widget.TextBox("Press Mod+R to spawn", foreground="#d75f5f"),
                widget.Wttr(emoji=False, location={'Všestary':'home'}, format='%l: %t\n'),
                widget.Sep(linewidth=1),
                widget.Mpd2(status_format='{play_status} {title}', idle_format='{play_status} {idle_message}', idle_message='MPD'),
#                widget.Spacer(length=5),
#                widget.Spacer(length=7),
#                widget.KeyboardLayout(update_interval="60"),
#                widget.Clipboard(),
#               widget.CheckUpdates(distro="Arch", "Arch_checkupdates", "Arch_Sup", "Arch_yay"),
                widget.Sep(linewidth=1),
                widget.Clock(format="%a %I:%M %p %d-%m-%Y"),
                widget.Sep(linewidth=1),
                widget.Systray(),
#    widget.QuickExit(),
            ],
           32,
            border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background=(0, 0, 0, 0), opacity=1
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
	    Match(title="polybar"), # polybar
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = False

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
