# Auto-generated with h2o

_spades.py()
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
          word_list="  -o --isolate --sc --meta --bio --corona --rna --plasmid --metaviral --metaplasmid --rnaviral --iontorrent --test -h --help -v --version --12 -1 -2 -s --merged --pe-12 --pe-1 --pe-2 --pe-s --pe-m --pe-or --s --mp-12 --mp-1 --mp-2 --mp-s --mp-or --hqmp-12 --hqmp-1 --hqmp-2 --hqmp-s --hqmp-or --sanger --pacbio --nanopore --trusted-contigs --untrusted-contigs --only-error-correction --only-assembler --careful --checkpoints --continue --restart-from --disable-gzip-output --disable-rr --dataset -t --threads -m --memory --tmp-dir -k --cov-cutoff --phred-offset --custom-hmms" 
          COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
          ;;
    esac

}

## -o bashdefault and -o default are fallback
complete -o bashdefault -o default -F _spades.py spades.py
