#!/bin/bash

session="kafka"
venv="source venv/bin/activate"

# set up tmux
tmux start-server

# create a new tmux session, starting zookeeper-server ans kafka-server in different panels in the new window
tmux new-session -d -s $session -n 'all-panels'

# Select pane 0, launch zookeeper-server
tmux send-keys "zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties" C-m

# Split pane 0 horizontally by 50%, start kafka-server
tmux splitw -v -p 50
#tmux send-keys "sleep 4; nvim" C-m

tmux selectp -t 0
tmux splitw -h -p 66
tmux send-keys "sleep 2; kafka-server-start /usr/local/etc/kafka/server.properties" C-m

# add htop
tmux splitw -h -p 33
tmux send-keys "htop" C-m

# split pane 3 vertically by 33 % (Producers and the consumer)
tmux selectp -t 3
tmux send-keys "$venv; sleep 2; python3.7 Producer\ A.py" C-m

tmux splitw -h -p 66
tmux send-keys "$venv; sleep 2; python3.7 Producer\ B.py" C-m

tmux splitw -h -p 33
tmux send-keys "$venv; while True; do sleep 1; python3.7 Consumer\ C.py; done" C-m

#tmux selectp -t 4

tmux attach-session -t $session


