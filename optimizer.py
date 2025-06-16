"""Gene optimization utilities using DNA Chisel."""

from __future__ import annotations

from typing import Optional

from dnachisel import (
    DnaOptimizationProblem,
    EnforceTranslation,
    CodonOptimize,
    AvoidPattern,
)


_SPECIES_MAP = {
    "ecoli": "e_coli",
    "yeast": "s_cerevisiae",
    "bacillus": "b_subtilis",
}


_DEF_PATTERNS = [
    "EcoRI_site",
    "XhoI_site",
    "BamHI_site",
]


def optimize_gene(seq: str, organism: str) -> str:
    """Optimize the gene sequence for the target organism."""
    species = _SPECIES_MAP.get(organism, "e_coli")
    constraints = [EnforceTranslation()]
    constraints += [AvoidPattern(p) for p in _DEF_PATTERNS]
    objectives = [CodonOptimize(species=species)]
    problem = DnaOptimizationProblem(
        sequence=seq,
        constraints=constraints,
        objectives=objectives,
    )
    problem.resolve_constraints()
    problem.optimize()
    return str(problem.sequence)
