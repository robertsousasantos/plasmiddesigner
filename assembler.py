"""Plasmid assembly utilities using BioPython."""

from __future__ import annotations

from typing import Dict

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from parts_db import PARTS_DB


def assemble_plasmid(design: Dict[str, str], gene_seq: str) -> SeqRecord:
    """Return the assembled plasmid as a SeqRecord."""
    org = design["organism"]
    backbone = PARTS_DB[org]["backbone"]
    prom_seq = PARTS_DB[org]["promoters"][design["promoter"]]
    term_seq = PARTS_DB[org]["terminators"][design["terminator"]]
    plasmid_seq = backbone + prom_seq + gene_seq + term_seq
    record = SeqRecord(Seq(plasmid_seq), id="designed_plasmid", description="")
    return record
