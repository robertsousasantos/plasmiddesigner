# Plasmid Designer Demo

This repository contains a minimal prototype for a plasmid design system.
The code illustrates how a large language model (e.g. Gemini) could be
used together with local bioinformatics tools to assemble plasmid sequences.

## Files

- `parts_db.py` – simplified database of plasmid parts.
- `nlp_parser.py` – uses the Gemini SDK when available to parse natural
  language requests, falling back to heuristic parsing when offline.
- `optimizer.py` – codon-optimizes a gene using DNA Chisel.
- `assembler.py` – joins backbone, promoter, optimized gene and terminator
  into a final plasmid sequence.
- `main.py` – command line script demonstrating the workflow.

## Example

```bash
python main.py "Express GFP in E. coli" --gene-seq ATGC...
```

This will print the design parameters and resulting plasmid sequence.
