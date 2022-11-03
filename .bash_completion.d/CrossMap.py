# Auto-generated with h2o

_CrossMappy()
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
          bed) _CrossMappy_bed
            return
            ;;

          bam) _CrossMappy_bam
            return
            ;;

          gff) _CrossMappy_gff
            return
            ;;

          wig) _CrossMappy_wig
            return
            ;;

          bigwig) _CrossMappy_bigwig
            return
            ;;

          vcf) _CrossMappy_vcf
            return
            ;;

          gvcf) _CrossMappy_gvcf
            return
            ;;

          maf) _CrossMappy_maf
            return
            ;;

          region) _CrossMappy_region
            return
            ;;

          viewchain) _CrossMappy_viewchain
            return
            ;;

      *)
          word_list=" bed bam gff wig bigwig vcf gvcf maf region viewchain -h --help -v --version"
          COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
          ;;
    esac

}

_CrossMappy_bed ()
{
    local cur word_list
    word_list=" -h --help --chromid --unmap-file" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

_CrossMappy_bam ()
{
    local cur word_list
    word_list=" -h --help -m --mean -s --stdev -t --times -a --append-tags --chromid" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

_CrossMappy_gff ()
{
    local cur word_list
    word_list=" -h --help --chromid" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

_CrossMappy_wig ()
{
    local cur word_list
    word_list=" -h --help --chromid" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

_CrossMappy_bigwig ()
{
    local cur word_list
    word_list=" -h --help --chromid" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

_CrossMappy_vcf ()
{
    local cur word_list
    word_list=" -h --help --chromid --no-comp-alleles --compress" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

_CrossMappy_gvcf ()
{
    local cur word_list
    word_list=" -h --help --chromid --no-comp-alleles --compress" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

_CrossMappy_maf ()
{
    local cur word_list
    word_list=" -h --help --chromid" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

_CrossMappy_region ()
{
    local cur word_list
    word_list=" -h --help --chromid -r --ratio" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

_CrossMappy_viewchain ()
{
    local cur word_list
    word_list=" -h --help" 
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
}

## -o bashdefault and -o default are fallback
complete -o bashdefault -o default -F _CrossMappy CrossMap.py
