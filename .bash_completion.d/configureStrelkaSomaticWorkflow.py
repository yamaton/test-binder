# Auto-generated with h2o

_configureStrelkaSomaticWorkflowpy()
{
    local i=1 cmd cur word_list
    cur="${COMP_WORDS[COMP_CWORD]}"

    # take the last word that's NOT starting with -
    while [[ ( "$i" < "$COMP_CWORD" ) ]]; do
        local s="${COMP_WORDS[i]}"
        case "$s" in
          -*) ;;
          *)
            cmd="$s"
            ;;
        esac
        (( i++ ))
    done

    case "$cmd" in
      *)
          word_list="  --version -h --help --config --allHelp --normalBam --tumorBam --tumourBam --outputCallableRegions --referenceFasta --indelCandidates --forcedGT --exome --targeted --callRegions --runDir"
          COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
          ;;
    esac

}

## -o bashdefault and -o default are fallback
complete -o bashdefault -o default -F _configureStrelkaSomaticWorkflowpy configureStrelkaSomaticWorkflow.py
