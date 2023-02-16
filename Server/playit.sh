#!/bin/sh
killall playit >/dev/null &
exec /home/filip/Server/playit -s >/dev/null
