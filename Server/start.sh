./playit -s>/dev/null &
java -Xmx640M -DPurpur.IReallyDontWantSpark=true --add-modules=jdk.incubator.vector -jar purpur-1.19.3.jar nogui
