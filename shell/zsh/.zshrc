# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="ys"

# Set list of themes to load
# Setting this variable when ZSH_THEME=random
# cause zsh load theme from this variable instead of
# looking in ~/.oh-my-zsh/themes/
# An empty array have no effect
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# Berrabe Alias
alias ls='ls -l --color=auto'
alias ll='ls -al'
LS_COLORS=$LS_COLORS:'di=1;95:fi=1;94:ex=1;33:' ; export LS_COLORS
ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor)
#toilet "                  berrabe" -f standard --gay

download_playlist(){
#!/bin/bash
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White
	
	clear
    echo -e $BWhite" "
    echo -e $BCyan " [?] Input Playlist youtube URL"; echo -n "  >> ";tput sgr0 ;read _input_playlist_url ;echo " "
    echo -ne $BCyan " [?] Playlist Start  >> ";tput sgr0; read _input_playlist_start ;echo " "
    echo -ne $BCyan " [?] Playlist End  >> ";tput sgr0; read _input_playlist_end ; echo " "
    
    result_URL=$(echo $_input_playlist_url | sed 's/https:\/\/www.youtube.com\/playlist?list=/[playlist] /g')
    echo " " 
    
    echo -e $BGreen" [+] S U M M A R Y"
    echo -e $BGreen"       Download URL   >> $result_URL"
    echo -e $BGreen"       Download Start >> $_input_playlist_start"
    echo -e $BGreen"       Download End   >> $_input_playlist_end" #;eval _input_playlist_end=$(_input_playlist_end + '1'); tput sgr0

    echo " "

    echo -ne $BYellow" [+] Is Summary Correct? [y/n] >> " ;tput sgr0;read _state
        if [[ $_state = 'y' ]] || [[ $_state = '' ]]
            then 
            clear

            STATUS=$(/usr/bin/pgrep youtube-dl | wc -l)
			count=$_input_playlist_start
			digits=${#count}


	while [ $STATUS -eq 0 ]; do
		echo -e $BGreen"[+] Downloaded file - $count "$BYellow"<== ($result_URL)" ;tput sgr0
		
		#standard_output="'%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'"
				standard_output="%(uploader)s/%(playlist)s/$count - %(title)s.%(ext)s'"

			if youtube-dl --playlist-items $count --write-auto-sub -o $standard_output $_input_playlist_url #2> /dev/null

				then
					echo " "
					echo -e $BGreen"[+] SUCCES"
				else
					echo -e $BRed"[-] ERROR | Exiting"
					return 1
			fi		


		sleep 1

        echo " "
        count=$(printf "%0${digits}d\n" "$((10#$count + 1))")
        if [[ $count = $_input_playlist_end ]] ; then return 0 ; fi 
    done    

	elif [[ $_state = 'n' ]]
		then
		echo " "
		echo -ne $BRed" [-] Exiting"
		return 1

        else
        	echo " "
            echo -ne $BRed" [-] ERROR | Input Not Found"
            return 1
        fi
    echo " "
}
[[ "$TERM" == "xterm" ]] && export TERM=xterm-256color
alias py="python3"
