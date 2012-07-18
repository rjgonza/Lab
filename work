#!/bin/bash

session="WORK"

function attach { tmux attach-session -t $session; exit; }

tmux has-session -t "$session" && attach

tmux new-session -d -s $session

tmux set -g default-terminal "screen-256color"
#tmux set -g default-terminal "xterm"
#tmux set -g default-terminal "screen-256color"
tmux set -g history-limit 50000

# HARDSTATUS
tmux set-option -g status-bg black
tmux set-option -g status-fg white
tmux set-option -g status-interval 60
tmux set-option -g status-left-length 30
tmux set-option -g status-right '#[fg=yellow]#(cut -d " " -f 1-3 /proc/loadavg)#[default] #[fg=red]%H:%M#[default]'

tmux set-window-option -g clock-mode-style 12
tmux set-window-option mode-mouse off
tmux set-option mouse-select-pane off
tmux set-option lock-server off
tmux set-option lock-after-time 1200
tmux set-option lock-command vlock
tmux bind-key z lock
tmux bind-key -n        C-n     next-window             # next window
tmux bind-key -n        C-h     previous-window         # prev window
tmux bind-key -n        C-t     select-pane -t :.+      # next pane
tmux bind-key -n        C-y     setw synchronize-panes  # broadcast mode on/off
tmux bind-key -n        C-Up    resize-pane -U          # resize pain using C-arrows
tmux bind-key -n        C-Down  resize-pane -D
tmux bind-key -n        C-Left  resize-pane -L
tmux bind-key -n        C-Right resize-pane -R

index=0
for i in carcore ashcore carrash ashrash carblob ashblob carpats ashpats caract ashact carbrace ashbrace cartape ashtape cargic ashgic caranus carpoem1 carpoem2 carpoem3 carpoem4 carpore1 lunfrej carnemo1 ashnemo1 cardata ashntf nom2otf carcoreutil; do
        let index=$index+1
        tmux new-window -t WORK -n "$i" "ssh $i"
done
tmux new-window -t WORK -n 'RASH_REJECTS' 'ssh carrash'

tmux select-window -t WORK:0
tmux -2 attach-session -t WORK
