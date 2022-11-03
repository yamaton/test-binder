# Auto-generated with h2o

_agatconvertspgxf2gxfpl()
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
          word_list="  -g --gff -c --ct --efl --expose --ml --merge_loci -v --nc --no_check --tabix --throw_fasta --debug -o --output --gvi --gff_version_input --gvo --gff_version_output --no_progressbar -h --help"
          COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
          ;;
    esac

}

## -o bashdefault and -o default are fallback
complete -o bashdefault -o default -F _agatconvertspgxf2gxfpl agat_convert_sp_gxf2gxf.pl
