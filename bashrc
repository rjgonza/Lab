function parse_git_branch () {                                                                                                                                                                                │···························
       git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'                                                                                                                                     │···························
}    

function slash_and_burn(){                                                                                                                                                                                    │···························
    git pull                                                                                                                                                                                                  │···························
    git fetch -p                                                                                                                                                                                              │···························
    for i in $(git branch|awk '{print $NF}'); do                                                                                                                                                              │···························
        git branch -r | grep -q $i || git branch -d $i;                                                                                                                                                       │···························
    done                                                                                                                                                                                                      │···························
}   

# TODO: add ssh-agent function
# TODO: setup role to deploy bash settings