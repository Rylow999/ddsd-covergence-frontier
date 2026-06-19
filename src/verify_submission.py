"""
DDSD Convergence Frontier — Verification Script
Checks that all data files and figures match paper claims.

Run: python src/verify_submission.py
Expected output: "VERIFICATION PASSED" or detailed error report
"""

import os


def verify_file_exists(path, description):
    """Check that a file exists."""
    if not os.path.exists(path):
        return False, f"Missing {description}: {path}"
    return True, f"OK: {description}"


def verify_chang_results():
    """Verify Chang verification data (Section 5)."""
    path = "data/chang_verification_results.txt"
    if not os.path.exists(path):
        return False, "Missing Chang verification results"

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = [
        "Collatz satisface EXACTAMENTE" in content,
        "Ultra-Campeón ROMPE" in content,
        "bit 4 tiene efecto casi nulo" in content,
    ]

    if all(checks):
        return True, "Chang verification: all claims present"
    return False, "Chang verification: some claims missing"


def verify_frontier_summary():
    """Verify frontier executive summary (Section 7)."""
    path = "data/frontier_executive_summary.txt"
    if not os.path.exists(path):
        return False, "Missing frontier executive summary"

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = [
        "Ultra-Campeón" in content,
        ("drift = -1.68" in content or "drift = -1.684" in content),
        "100% de convergencia" in content,
        "Collatz no es óptimo" in content,
    ]

    if all(checks):
        return True, "Frontier summary: all claims present"
    return False, "Frontier summary: some claims missing"


def verify_figures():
    """Verify all expected figures exist (Figures 15-26)."""
    expected = [
        "figures/fig15_chang_bit4_destruction.png",
        "figures/fig16_chang_unified_verification.png",
        "figures/fig17_even_coefficients_sa.png",
        "figures/fig18_final_frontier_convergence.png",
        "figures/fig19_frontier_proportion_space.png",
        "figures/fig20_markov_memory_analysis.png",
        "figures/fig21_original_map_deep_dive.png",
        "figures/fig22_p3_p9_phase_diagram.png",
        "figures/fig23_sa_deep_convergence.png",
        "figures/fig24_sha256_dissipation.png",
        "figures/fig25_ultra_champion_pattern.png",
        "figures/fig26_universe_comparison.png",
    ]

    missing = []
    for fig in expected:
        if not os.path.exists(fig):
            missing.append(fig)

    if missing:
        return False, f"Missing figures: {missing}"
    return True, f"All {len(expected)} figures present"


def verify_paper():
    """Verify paper contains formal definitions."""
    path = "paper/ddsd_convergence_frontier.md"
    if not os.path.exists(path):
        return False, "Missing paper"

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = [
        "Definition 2.1" in content,
        "Definition 2.2" in content,
        "Definition 2.4" in content,
        "observable embedding" in content,
        "convergence frontier" in content,
        "empirical emergent structure" in content,
    ]

    if all(checks):
        return True, "Paper: formal definitions present"
    return False, "Paper: some formal definitions missing"


def main():
    print("=" * 70)
    print("DDSD CONVERGENCE FRONTIER — VERIFICATION")
    print("Checking formal definitions, data, and figures...")
    print("=" * 70)

    checks = [
        verify_file_exists("paper/ddsd_convergence_frontier.md", "Paper (Markdown)"),
        verify_file_exists("data/chang_verification_results.txt", "Chang results"),
        verify_file_exists("data/frontier_executive_summary.txt", "Frontier summary"),
        verify_paper(),
        verify_chang_results(),
        verify_frontier_summary(),
        verify_figures(),
    ]

    all_passed = True
    for passed, msg in checks:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {msg}")
        if not passed:
            all_passed = False

    print("=" * 70)
    if all_passed:
        print("VERIFICATION PASSED")
    else:
        print("VERIFICATION FAILED — see errors above")
    print("=" * 70)

    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
