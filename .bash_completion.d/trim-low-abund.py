# Auto-generated with h2o

_trimlowabundpy()
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
          word_list="  --version --info -h --help -k --ksize -U --unique-kmers --fp-rate -M --max-memory-usage --small-count -C --cutoff -Z --trim-at-coverage --normalize-to -o --output -V --variable-coverage -l --loadgraph -s --savegraph -q --quiet --summary-info --force --ignore-pairs -T --tempdir --gzip --bzip --diginorm --diginorm-coverage --single-pass"
          COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
          ;;
    esac

}

## -o bashdefault and -o default are fallback
complete -o bashdefault -o default -F _trimlowabundpy trim-low-abund.py
