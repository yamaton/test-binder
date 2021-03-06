# Auto-generated with h2o

_hisat2_simulate_reads.py()
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
          word_list="  -h --help -d --dna --single-end -r --read-length -f --fragment-length -n --num-fragment -e --expr-profile --repeat-info --error-rate --max-mismatch --random-seed --snp-prob --sanity-check -v --verbose --version" 
          COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
          ;;
    esac

}

## -o bashdefault and -o default are fallback
complete -o bashdefault -o default -F _hisat2_simulate_reads.py hisat2_simulate_reads.py
