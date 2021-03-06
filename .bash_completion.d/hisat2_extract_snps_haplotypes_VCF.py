# Auto-generated with h2o

_hisat2_extract_snps_haplotypes_VCF.py()
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
          word_list="  -h --help --reference-type --inter-gap --intra-gap --non-rs --genotype-vcf --genotype-gene-list --extra-files -v --verbose" 
          COMPREPLY=( $(compgen -W "${word_list}" -- "${cur}") )
          ;;
    esac

}

## -o bashdefault and -o default are fallback
complete -o bashdefault -o default -F _hisat2_extract_snps_haplotypes_VCF.py hisat2_extract_snps_haplotypes_VCF.py
