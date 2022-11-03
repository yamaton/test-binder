# Auto-generated with h2o

_rnaspadespy()
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
          word_list="  -o --iontorrent --test -h --help -v --version --12 -1 -2 -s --merged --pe-12 --pe-1 --pe-2 --pe-s --pe-m --pe-or --s --pacbio --nanopore --trusted-contigs --untrusted-contigs --fl-rna --ss --checkpoints --continue --restart-from --disable-gzip-output --disable-rr --dataset -t --threads -m --memory --tmp-dir -k --phred-offset --custom-hmms"
          COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
          ;;
    esac

}

## -o bashdefault and -o default are fallback
complete -o bashdefault -o default -F _rnaspadespy rnaspades.py
