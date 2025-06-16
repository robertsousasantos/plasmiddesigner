"""Local database of standard plasmid parts.
Sequences are simplified placeholders for demonstration purposes.
"""

PARTS_DB = {
    "ecoli": {
        "backbone": "AAAACCCCGGGGTTTT",
        "promoters": {
            "T7": "TAATACGACTCACTATAGGG",
            "lac": "TGTTACACTTTATGCTTCCGGCTCG"
        },
        "terminators": {
            "T7_terminator": "AATAACCCCTCAAGG"
        }
    },
    "yeast": {
        "backbone": "GGGGAAAATTTTCCCC",
        "promoters": {
            "TEF1": "AAAAACTTTTGGGGCCCC",
            "GAL1": "GGGCCCAAATTTTT"
        },
        "terminators": {
            "ADH1_terminator": "CCCCCCTTTTTGGG"
        }
    },
    "bacillus": {
        "backbone": "TTTTGGGGCCCCAAAA",
        "promoters": {
            "Pxyl": "TTAACGGTAGCTT",
            "Pgrac": "CCGGAATTCCCT"
        },
        "terminators": {
            "Bsub_terminator": "GGGGTTTTAAAA"
        }
    }
}
