## =======================================
##             ENV variables
## =======================================
export LANG=en_US.UTF-8
export EDITOR=vim
export PAGER=less
export SHELL=zsh
export LC_NUMERIC=en_US.UTF-8

# XDG
[[ "$(uname -s)" == "Linux" ]] && export XDG_CONFIG_HOME="$HOME/.config"

# zsh fpath
fpath=( ~/.config/zsh/zsh-completions-bio/completions ~/.config/zsh/completions "${fpath[@]}" )

# zsh history
export HISTFILE=~/.zsh_history
export HISTSIZE=80000
export SAVEHIST=80000

# zsh syntax highlighting
export ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor)
typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[alias]='fg=yellow,bold'
ZSH_HIGHLIGHT_STYLES[path]='fg=cyan'

## local bin
export PATH="$HOME/.local/bin:$PATH"
