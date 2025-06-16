"""Command-line interface for the plasmid design demo."""

from __future__ import annotations

import argparse

from assembler import assemble_plasmid
from nlp_parser import parse_user_request
from optimizer import optimize_gene


_DEF_GENE = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"


def choose_default_parts(organism: str) -> dict:
    if organism == "ecoli":
        return {"promoter": "T7", "terminator": "T7_terminator"}
    if organism == "yeast":
        return {"promoter": "TEF1", "terminator": "ADH1_terminator"}
    return {"promoter": "Pxyl", "terminator": "Bsub_terminator"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Plasmid designer demo")
    parser.add_argument("description", help="Experiment description")
    parser.add_argument("--gene-seq", dest="gene_seq", help="DNA sequence of the gene")
    args = parser.parse_args()

    reqs = parse_user_request(args.description)
    design = choose_default_parts(reqs["organism"])
    design.update(reqs)

    gene = (args.gene_seq or _DEF_GENE).upper()
    optimized = optimize_gene(gene, reqs["organism"])
    plasmid = assemble_plasmid(design, optimized)

    print("Design parameters:", design)
    print("Optimized gene:", optimized)
    print("Plasmid sequence:", plasmid.seq)


if __name__ == "__main__":
    main()
