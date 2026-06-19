# Ddsd-convergence-frontier

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**The Convergence Frontier in Discrete Dynamical Systems: A Computational Study of Dissipative Families Beyond Collatz.**

This repository is a companion to [ddsd-framework](https://github.com/Rylow999/ddsd-framework). While the parent repository establishes the DDSD (Discrete Dynamical Systems Dissipation) framework and applies it to Collatz, 5x+1, perturbed families, critical maps, 2-adic variable fields, toy cryptographic hashes, and evolved maps, this repository extends the framework by:

1. **Formalizing an observable embedding** $\Phi: \mathcal{D} \rightarrow \mathbb{R}^k$ that maps dynamical systems into a real vector space via computable statistics.
2. **Defining the convergence frontier** as an emergent geometric structure in embedding space, induced by density clustering of systems with distinct statistical behaviors.
3. **Verifying Chang's (2026) one-bit mixing structure** on pure Collatz and demonstrating its failure on strategically mixed maps.
4. **Discovering the Ultra-Champion map** via genetic algorithm — 3.6$\times$ more dissipative than Collatz, with 100% termination and 4$\times$ faster convergence.
5. **Exploring the proportion space frontier** through systematic sweep and simulated annealing.
6. **Analyzing a toy cryptographic hash model** as a computational proxy for hyper-dissipative behavior.

All claims are framed as empirical observations under defined sampling regimes. No proof of boundedness for general families is claimed.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run complete reproduction suite (takes ~10-15 minutes)
python src/master_simulation.py

# Verify data integrity against paper claims
python src/verify_submission.py
```

## Structure

```
.
├── README.md                          # This file
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
├── src/
│   ├── master_simulation.py           # Complete reproduction suite (all experiments)
│   └── verify_submission.py           # Automated verification script
├── data/
│   ├── chang_verification_results.txt   # Chang verification results
│   └── frontier_executive_summary.txt   # Frontier exploration summary
├── figures/
│   ├── fig15_chang_bit4_destruction.png
│   ├── fig16_chang_unified_verification.png
│   ├── fig17_even_coefficients_sa.png
│   ├── fig18_final_frontier_convergence.png
│   ├── fig19_frontier_proportion_space.png
│   ├── fig20_markov_memory_analysis.png
│   ├── fig21_original_map_deep_dive.png
│   ├── fig22_p3_p9_phase_diagram.png
│   ├── fig23_sa_deep_convergence.png
│   ├── fig24_sha256_dissipation.png
│   ├── fig25_ultra_champion_pattern.png
│   └── fig26_universe_comparison.png
└── paper/
    └── ddsd_convergence_frontier.md   # Markdown version (GitHub-ready)
```

## Reproducibility

All simulations use fixed random seed `42` for full reproducibility.
The complete suite regenerates all data, figures, and verification reports.

**Expected outputs:**

- `data/*.txt` — Verification summaries
- `figures/*.png` — Figures 15-26
- Console report with all metrics

## Key Results

### Observable Embedding Framework
We define $\Phi: \mathcal{D} \rightarrow \mathbb{R}^4$ with components:
- $\Phi_1$: resolution-dependent decorrelation ($R^2$ at $K=6$)
- $\Phi_2$: intrafiber output dispersion (normalized entropy)
- $\Phi_3$: scale-dependent drift (Bonferroni-corrected)
- $\Phi_4$: pathwise recurrence frequency

The **convergence frontier** $\mathcal{F} \subset \mathbb{R}^4$ is the boundary induced by density clustering in this embedding space.

### Chang Verification
- **Collatz pure**: Satisfies Chang's one-bit mixing **exactly** — bit 4 determines gap outcome with probability ~0.505
- **Ultra-Champion**: **Breaks** Chang's structure — gap outcomes independent of bit 4 (~0.122 each)
- **Implication**: Collatz's rigidity is its difficulty; mixed maps with multi-bit mixing may be easier to prove

### The Ultra-Champion Map
Discovered via genetic algorithm + intensive search:

```
Chromosome: [3, 7, 3, 5, 7, 3, 3, 9, 9, 7, 3, 5, 3, 3, 9, 9,
             7, 3, 3, 5, 5, 3, 7, 3, 7, 7, 3, 5, 5, 3, 5, 9]
Proportion: 13×3, 7×5, 7×7, 5×9
```

| Metric | Collatz | Ultra-Champion | Ratio |
|--------|---------|----------------|-------|
| Drift (accelerated) | -0.465 | **-1.684** | 3.6× |
| Drift (original map) | -0.155 | **-0.344** | 2.2× |
| Steps to 1 (μ) | 82.6 | **20.7** | 4.0× |
| Steps to 1 (med) | 81.0 | **21.0** | 3.9× |
| Max bits reached | 35.2 | **34.2** | Similar |
| Termination rate | 100% | **100%** | Same |

**Exhaustive verification**: 100% convergence for all 2,097,152 odd integers in [1, 2²²).

### Frontier Findings
- **Collatz is NOT optimal** — sits in a local valley of the fitness landscape
- **Disposition is everything** — Same proportion, different arrangement: drift from +0.44 to -1.70
- **Mod 32 is the sweet spot** — Mod 64 and mod 128 do not improve dissipation
- **No known theoretical lower bound** — Empirical drift of -1.68 is 56× beyond the 2-adic theoretical limit

### Toy Hash Model (Computational Proxy)
- Drift: **-1.29** per round (15× stronger than Collatz)
- Perfect decorrelation (A1 R² ≈ 0)
- Maximum entropy mixing (A2 ≈ 0.998)
- Instant convergence, no recurrence

**Disclaimer:** No theoretical equivalence with dynamical invariants is claimed. The hash model is a computational proxy with structurally analogous features.

## Verification

Before submission to any venue, run:

```bash
python src/verify_submission.py
```

This checks that all data files match the paper's claims. If it prints "VERIFICATION PASSED", the submission is internally consistent.

## Parent Repository

This work builds directly on:
- [github.com/Rylow999/ddsd-framework](https://github.com/Rylow999/ddsd-framework) — DDSD Framework v2.0

## Citation

```bibtex
@article{Nieto2026Frontier,
  title={The Convergence Frontier in Discrete Dynamical Systems: A Computational Study of Dissipative Families Beyond Collatz},
  author={Nieto, Luciano Benjamín},
  year={2026},
  note={Companion repository to DDSD Framework v2.0}
}
```

## Contact

For questions or issues, please open a GitHub issue or contact the authors.

* * *

_Generated: 2026-06-19_  
_Framework: DDSD Companion — Convergence Frontier_  
_Seed: 42_
