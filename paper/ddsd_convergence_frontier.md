# The Convergence Frontier in Discrete Dynamical Systems: A Computational Study of Dissipative Families Beyond Collatz

**Abstract.** We extend the DDSD (Discrete Dynamical Systems Dissipation) framework by formalizing an observable embedding function $\Phi$ that maps discrete dynamical systems into a finite-dimensional real space. Within this embedding space, we identify an emergent geometric structure — the *convergence frontier* — as a boundary induced by density clustering of systems with distinct statistical behaviors. We instantiate this construction on a family of Collatz-like maps with mod-32 coefficient rules, conducting computational verification on 952 trajectories up to $2^{40}$ and exhaustive testing on 2,097,152 odd integers up to $2^{22}$. We verify Chang's (2026) one-bit mixing structure on pure Collatz and observe its failure on the Ultra-Champion map (Section 6), where multi-bit mixing yields empirical drift $\Phi = -1.68$ (3.6$\times$ beyond the 2-adic theoretical limit of $\log_2(3) - 2 \approx -0.42$). A genetic algorithm discovers maps with 100% termination and 4$\times$ faster convergence than Collatz. We analyze a toy cryptographic hash model as a computational proxy exhibiting hyper-dissipative behavior (drift $-1.29$ per round, Section 8). All claims are framed as empirical observations under defined sampling regimes; no proof of boundedness for general families is claimed. See Section 10.2 for explicit limitations of the framework.

---

## 1. Introduction

The Collatz conjecture asks whether every orbit of the map $T(n) = n/2$ (even) or $3n+1$ (odd) reaches the cycle $(1,4,2)$. Tao (2019) proved that almost all orbits attain almost bounded values. We ask a different question: what structural properties of the map make boundedness plausible, and can we characterize the space of maps sharing these properties?

We formalize an **observable embedding framework** (Definition 2.2) that maps discrete dynamical systems into a real vector space via computable observables. Within this space, we study an emergent geometric structure — the **convergence frontier** (Definition 2.4) — that separates systems exhibiting statistical decay behavior from those exhibiting growth. This paper does **not** prove boundedness for any family. It provides a **computational characterization** of structural properties that empirically correlate with convergent behavior, and explores the phase boundary between decaying and expanding systems.

The structure of the paper is as follows. Section 1 introduces the problem and framework. Section 2 formalizes the base space of systems, the observable embedding, and the convergence frontier. Section 3 presents computational verification of the four observables on Collatz and 5x+1. Section 4 establishes the exact 2-adic drift as a theoretical boundary. Section 5 verifies Chang's one-bit mixing structure. Section 6 describes the genetic algorithm discovery of the Ultra-Champion map. Section 7 explores the frontier in proportion space. Section 8 analyzes the toy hash model as a computational proxy. Section 9 presents the machine learning regression of observables. Section 10 discusses what the framework does and does not do, including honest negative results and a separated interpretative mapping. Section 11 concludes.

---

## 2. Formal Framework

### 2.1 The Base Space of Systems

**Definition 2.1 (System Family).** Let $\mathcal{D}$ be a family of discrete dynamical systems $T: \mathbb{N} \to \mathbb{N}$. We specialize to *Collatz-like maps* defined by a mod-$M$ rule:

$$T_a(n) = \begin{cases} n/2 & \text{if } n \text{ even} \\ a_{n \bmod M} \cdot n + 1 & \text{if } n \text{ odd} \end{cases}$$

where $a = (a_0, a_1, \ldots, a_{M-1})$ is a coefficient vector with $a_i \in \{3,5,7,9\}$ (odd integers).

For the accelerated map, we write:

$$R_a(n) = \frac{a_{n \bmod M} \cdot n + 1}{2^{\nu_2(a_{n \bmod M} \cdot n + 1)}}$$

where $\nu_2(m)$ denotes the 2-adic valuation (exponent of the highest power of 2 dividing $m$).

### 2.2 Observable Embedding

**Definition 2.2 (Observable Embedding).** An *observable embedding* is a function:

$$\Phi: \mathcal{D} \rightarrow \mathbb{R}^k$$

where each component $\Phi_i(T)$ is a computable statistic of the system's trajectories. For this study, we define $k = 4$ with:

- $\Phi_1(T)$ = **resolution-dependent decorrelation**: $R^2(E, \pi_K)$ at fixed resolution $K = 6$
- $\Phi_2(T)$ = **intrafiber output dispersion**: normalized Shannon entropy of $\pi_K(T(x))$ within fibers
- $\Phi_3(T)$ = **scale-dependent drift**: $\mathbb{E}[\Delta_K E]$ under Bonferroni-corrected testing
- $\Phi_4(T)$ = **pathwise recurrence frequency**: empirical frequency of visits to $\{x : E(x) < \varepsilon\}$

The energy function is $E(n) = \nu_2(n+1)$, measuring log-growth observables.

**Definition 2.3 (Statistical Decay Behavior).** A system $T \in \mathcal{D}$ exhibits *statistical decay behavior* (colloquially, "dissipation") if $\Phi_3(T) < 0$ with statistical significance under the testing regime of Section 3.1. The term "dissipation" is used throughout as a *structural metaphor* for this property, not as a physical quantity. All uses are formally grounded in Definitions 2.2 and 2.3.

### 2.4 The Convergence Frontier

**Definition 2.4 (Convergence Frontier).** The *convergence frontier* $\mathcal{F} \subset \mathbb{R}^k$ is the geometric structure induced in the observable embedding space by density clustering of systems. Formally:

$$\mathcal{F} := \partial \left\{ \Phi(T) \in \mathbb{R}^k : \text{density}(\Phi(T)) > \theta_{\text{crit}} \right\}$$

where the density is computed via kernel density estimation over a finite sample $\mathcal{S} \subset \mathcal{D}$, and $\theta_{\text{crit}}$ is a threshold separating high-density (convergent-behavior) clusters from low-density (divergent-behavior) regions.

**Important:** The frontier is an *empirical emergent structure*, not a formally defined invariant. It depends on the sampling regime and the choice of observables.

---

## 3. Computational Verification

### 3.1 Setup

**Collatz (pure):** 1,000 random odd seeds across four scales: $[3,2^{18})$, $[2^{18},2^{30})$, $[2^{30},2^{35})$, $[2^{35},2^{40})$. Accelerated map $R(n) = (3n+1)/2^{\nu_2(3n+1)}$. 952 valid trajectories ($>20$ steps). Energy: $E(n) = \nu_2(n+1)$.

**5x+1 (control):** 200 seeds (20 known divergent + 60 random per scale). Max 200 steps, 256-bit ceiling.

**Ultra-Champion (evolved):** Exhaustive verification on all 2,097,152 odd integers in $[1, 2^{22})$. See Section 6 for discovery method and Section 6.5 for verification results.

### 3.2 Observable Results

#### A1: Resolution-Dependent Decorrelation

We measure the predictive power of coarse-graining $\pi_K$ for energy $E$ at varying resolutions $K$. Results are shown in Figure 15 (Chang bit-4 destruction analysis) and Figure 16 (unified verification).

| $K$ | Collatz Cor$(E,\pi_K)$ | $R^2$ | 5x+1 Cor$(E,\pi_K)$ | $R^2$ |
|-----|------------------------|-------|---------------------|-------|
| 2 | 0.725 | 0.525 | 0.700 | 0.490 |
| 4 | 0.471 | 0.222 | 0.466 | 0.217 |
| 6 | 0.182 | 0.033 | 0.203 | 0.041 |
| 8 | 0.103 | 0.011 | 0.081 | 0.007 |
| 10 | 0.061 | 0.004 | 0.039 | 0.002 |

Both maps show monotonic decay. At $K \geq 6$, predictive power is negligible ($R^2 < 0.05$). This is a shared structural property, not a discriminant. See Section 10.1 for the role of $\Phi_1$ in the framework.

#### A2: Intrafiber Output Dispersion

**Collatz:** Mean normalized entropy = 0.971 (32 of 64 fibers contain data; accelerated map preserves odd parity).
**5x+1:** Mean normalized entropy = 0.995.

Both maps exhibit high intrafiber dispersion. 5x+1 is slightly higher. See Figure 19 (frontier proportion space) for context on how dispersion varies across the coefficient space.

#### A3: Scale-Dependent Drift (Bonferroni-Corrected)

We test 9 values of $K \in \{1,2,4,6,8,10,12,16,20\}$. Bonferroni threshold: $\alpha = 0.01/9 = 0.0011$.

**Collatz K-sweep:** Significant negative drift for all $K \geq 2$ (see Figure 18, final frontier convergence, and Figure 26, universe comparison).
**5x+1 K-sweep:** Drift statistically indistinguishable from zero at all scales.

A3 is the **discriminant observable** between convergent and divergent behavior in our sample. This is an empirical observation from the specific sampling regime described in Section 3.1, not a derived theorem.

#### A4: Pathwise Recurrence

Both maps visit low-energy regions with comparable frequency (see Figure 20, Markov memory analysis). A4 is a shared property, not a discriminant. This negative result is discussed in Section 10.3.

| $\varepsilon$ | Collatz mean freq | min freq | 5x+1 mean freq | min freq |
|---------------|-------------------|----------|----------------|----------|
| 2 | 0.522 | 0.390 | 0.493 | 0.250 |
| 3 | 0.762 | 0.610 | 0.754 | 0.682 |

---

## 4. The 2-Adic Exact Drift and Theoretical Boundary

### 4.1 Theoretical Result

For the accelerated map $R_a(n) = (an+1)/2^{\nu_2(an+1)}$ with $a$ odd, operating on $\mathbb{Z}_2$ with Haar measure:

$$\mathbb{E}[\nu_2(an+1)] = 2 \quad \text{(independent of } a\text{)}$$

Therefore, the drift in log-coordinates is exactly:

$$\Phi_{\text{2-adic}}(a) = \log_2(a) - 2$$

**Proof sketch:** For $a$ odd, $an+1$ is always even. The probability that $\nu_2(an+1) \geq k$ is exactly $1/2^{k-1}$ for all $k \geq 1$, because $a$ is invertible modulo $2^k$. The expectation follows from $\sum_{k=1}^{\infty} k/2^k = 2$. $\square$

### 4.2 The Boundary

The critical boundary is at $a = 4$, where $\Phi(4) = 0$. However, $a = 4$ is **even**, so there exists no accelerated map with odd coefficient on the boundary. The odd integers "jump" from $a=3$ (drift $-0.415$) to $a=5$ (drift $+0.322$) without touching the boundary.

| $a$ | $\log_2(a)$ | Drift $\Phi(a)$ | Behavior |
|-----|-------------|-----------------|----------|
| 1 | 0.000 | $-2.000$ | Trivially collapsing |
| 3 | 1.585 | $-0.415$ | **Collatz (decaying)** |
| 5 | 2.322 | $+0.322$ | **5x+1 (expanding)** |
| 7 | 2.807 | $+0.807$ | Explosive |
| 9 | 3.170 | $+1.170$ | More explosive |

Collatz is the **last odd map** before the inaccessible boundary at $a=4$. This is an exact arithmetic result, not an empirical observation. See Figure 22 (p3-p9 phase diagram) for the empirical regime map, and Section 7.3 for the relationship between the 2-adic limit and empirical drift in mixed maps.

---

## 5. Chang Verification: One-Bit Mixing Structure

### 5.1 Chang's Framework

Chang (2026) states a "Map Balance Theorem": for all $K \geq 5$, burst residues modulo $2^K$ that initiate gaps map to classes 3 and 7 (mod 8) with an exact difference of 1. For the dominant class $n \equiv 1 \pmod{8}$, the gap outcome depends on a single binary variable: bit 4 of the value at burst-ending times.

### 5.2 Verification on Pure Collatz

For $n \equiv 1 \pmod{8}$:
- bit 4 = 0: gap $\to$ 7 with probability 0.505, gap $\to$ 3 with 0.000
- bit 4 = 1: gap $\to$ 3 with probability 0.508, gap $\to$ 7 with 0.000

**Observation:** Pure Collatz satisfies Chang's prediction within sampling error. The one-bit structure is confirmed in our sample. See Figure 15 (Chang bit-4 destruction).

### 5.3 Verification on Ultra-Champion

For $n \equiv 1 \pmod{8}$:
- bit 4 = 0: gap $\to$ 3 = 0.122, gap $\to$ 7 = 0.124
- bit 4 = 1: gap $\to$ 3 = 0.121, gap $\to$ 7 = 0.126

**Observation:** The Ultra-Champion **breaks** Chang's one-bit structure. The gap outcome is statistically independent of bit 4 (difference $< 0.003$, within sampling error). See Figure 15 and Figure 16.

**Interpretation (heuristic, Section 10.4):** The Ultra-Champion achieves stronger empirical drift precisely by destroying the deterministic one-bit correlations of pure Collatz and replacing them with multi-bit mixing. This suggests that the difficulty of the Collatz conjecture may be partially attributable to its rigid one-bit structure, and that mixed maps with stronger mixing may be more amenable to analysis. This is speculative, not proven. See Section 6 for the genetic algorithm discovery and Section 7 for the frontier exploration.

---

## 6. The Ultra-Champion: Genetic Algorithm Discovery

### 6.1 Fitness Function

$$\text{fitness} = -2 \times \text{drift} + \text{termination rate} + \text{simplicity bonus}$$

where simplicity bonus rewards using fewer distinct coefficients.

### 6.2 Evolution Parameters

- Population: 20 individuals
- Generations: 15
- Selection: Tournament from top 50%
- Crossover: Single-point
- Mutation rate: 15%
- Elite preservation: 4 individuals
- Fitness evaluation: 50 random seeds per individual

### 6.3 Results

| Map | Fitness | Drift | Termination | Chromosome |
|-----|---------|-------|-------------|------------|
| **Ultra-Champion** | **1.81** | **$-$1.68** | **100%** | Mixed (13$\times$3, 7$\times$5, 7$\times$7, 5$\times$9) |
| Collatz pure | 1.25 | $-$0.09 | 100% | All 3 |
| 5x+1 pure | 0.04 | $+$0.32 | 0% | All 5 |

**Chromosome:**
```
[3, 7, 3, 5, 7, 3, 3, 9, 9, 7, 3, 5, 3, 3, 9, 9,
 7, 3, 3, 5, 5, 3, 7, 3, 7, 7, 3, 5, 5, 3, 5, 9]
```

See Figure 25 (Ultra-Champion pattern) for the coefficient map and autocorrelation structure. See Figure 17 (even coefficients SA) for comparison with SA results.

### 6.4 Runtime Coefficient Distribution

| Coefficient | Chromosome frequency | Runtime usage |
|-------------|---------------------|---------------|
| $a=3$ | 40.6% | 41.2% |
| $a=5$ | 21.9% | 39.9% |
| $a=7$ | 21.9% | 12.1% |
| $a=9$ | 15.6% | 6.9% |

Despite the chromosome having only 43.75% classes with $a=3$, the runtime distribution is nearly balanced. The larger coefficients are used in positions that accelerate descent without causing explosion. This is an empirical observation from trajectory analysis, not a derived property.

### 6.5 Exhaustive Verification

| Metric | Value |
|--------|-------|
| Numbers verified | 2,097,152 (all odd integers in $[1, 2^{22})$) |
| Non-terminating | 0 (100% convergence) |
| Maximum steps | 124 |
| Mean steps | 61.2 |
| Median steps | 61.0 |
| P99 | 89 steps |
| P99.9 | 99 steps |
| Maximum value reached | 76,527,496 ($2^{26.2}$) |

**Comparison with Collatz:**
- Collatz original: mean 174.8 steps
- Ultra-Champion: mean 70.0 steps (original map), 20.7 steps (accelerated)
- Ratio: 2.5$\times$ faster (original map), 4.0$\times$ faster (accelerated)

See Figure 18 (final frontier convergence) and Figure 21 (original map deep dive) for visual comparisons. See Figure 26 (universe comparison) for the full system comparison.

---

## 7. Frontier Exploration: Proportion Space

### 7.1 Systematic Sweep

We sweep 6,545 combinations of proportions $(n_3, n_5, n_7, n_9)$ with $n_3 + n_5 + n_7 + n_9 = 32$. See Figure 19 (frontier proportion space) for the heatmap and Figure 23 (SA deep convergence) for the optimization trajectory.

### 7.2 Key Observation

The frontier between decaying and expanding behavior is **non-monotonic** in proportions:

| Proportion | Random disposition | Optimized disposition | Difference |
|------------|-------------------|----------------------|------------|
| 3:13, 5:7, 7:7, 9:5 | drift = +0.44 | drift = $-$1.70 | **2.14 units** |

**Observation:** Disposition (arrangement) dominates proportion. The same proportion can be expansive or dissipative depending on coefficient ordering. This is an empirical finding from our systematic sweep, not a theoretical result. See Section 2.4 for the formal definition of the frontier and Section 10.3 for honest limitations.

### 7.3 Empirical Regime Map in $(p_3, p_9)$ Space

The empirical regime map (Figure 22) shows:
- Green zone (decaying): high $p_3$, low $p_9$, with aggressive mixing
- Red zone (expanding): low $p_3$, high $p_9$
- Yellow transition: intermediate regimes

The 2-adic limit $\Phi_{\text{2-adic}}(a) = \log_2(a) - 2$ is **irrelevant** for empirical drift in mixed maps. The observed drift of $-1.68$ is 56$\times$ beyond the theoretical 2-adic bound. This amplification is attributable to dynamic correlations created by strategic coefficient arrangement, not to any modification of the 2-adic structure. See Section 4 for the exact 2-adic result and Section 10.4 for the interpretative mapping.

### 7.4 Scale Exploration

| Modulus | Best drift | Termination | Observation |
|---------|-----------|-------------|-------------|
| 32 | $-$1.68 | 100% | Sweet spot |
| 64 | $-$1.62 | 100% | No improvement |
| 128 | $-$0.88 | 100% | Worse (harder to optimize) |

**Observation:** Mod 32 is the optimal bandwidth for this coefficient family. Additional complexity does not translate to greater dissipation. See Figure 17 (even coefficients SA) and Figure 23 (SA deep convergence) for exploration details.

---

## 8. Toy Hash Model: Computational Proxy

We construct a toy cryptographic hash model (64-bit state, 4 words of 16 bits, 32 rounds) as a **computational proxy** for hyper-dissipative behavior. We define energy as Hamming distance to the final state. See Figure 24 (SHA-256 dissipation analysis).

### 8.1 Observable Results

| Metric | Toy Hash | Collatz | Interpretation |
|--------|----------|---------|----------------|
| A1 Cor($E, \pi_6$) | 0.009 | 0.182 | Perfect decorrelation |
| A1 $R^2$ | 0.0001 | 0.033 | Energy unpredictable |
| A2 Entropy | 0.998 | 0.971 | Maximum mixing |
| A3 $\Phi_8$ | **$-$1.29** | **$-$0.081** | 15$\times$ stronger drift |
| A4 Freq ($\varepsilon=10$) | 3% | 52% | No recurrence (converges) |

### 8.2 Disclaimer

**No theoretical equivalence with dynamical invariants is claimed.** The hash model is presented as a computational proxy exhibiting features structurally analogous to dissipative discrete systems: local expansion dominated by mixing and compression. The analogy is heuristic and not mathematically formal. See Section 10.4 for the interpretative mapping and Section 10.2 for explicit limitations.

---

## 9. Machine Learning: Regression of Observables

We fit an MLP (32-16-8, tanh, L-BFGS, $\alpha=0.01$) to the empirical density in 64 log-bins using 6 engineered features. Evaluation uses leave-one-out cross-validation on 64 data points. See Figure 26 (universe comparison) for ML metrics in context.

| Metric | Value |
|--------|-------|
| $R^2$ (LOO-CV) | 0.959 |
| Pearson $\rho$ | 0.981 |
| KL divergence | 0.025 |

**Interpretation:** The model approximates the empirical density shape. The high $R^2$ reflects the simplicity of the density (unimodal decay) rather than deep structural learning. This is exploratory evidence for smoothness in log-coordinates, not proof of invariant measure existence. See Section 10.2 for limitations.

---

## 10. Discussion

### 10.1 What the Framework Does

The observable embedding $\Phi$ (Definition 2.2) provides a **taxonomic lens**:
- $\Phi_1$ measures whether energy is predictable from coarse state
- $\Phi_2$ measures whether dynamics are dispersive within fibers
- $\Phi_3$ measures whether macroscopic drift is negative (Definition 2.3)
- $\Phi_4$ measures whether orbits return to low-energy regions

Applied to Collatz and 5x+1, $\Phi_3$ is the sole discriminant in our sample. This is an empirical observation from the specific sampling regime described in Section 3.1.

### 10.2 What the Framework Does Not Do

- **Does not prove boundedness.** $\Phi_3$ is a measured observable, not a derived consequence of $\Phi_1$ + $\Phi_2$ + $\Phi_4$.
- **Does not prove convergence to (1,4,2).** Boundedness (if established) does not imply cycle uniqueness.
- **Does not establish an invariant measure.** The ML fit (Section 9) is exploratory regression, not measure-theoretic proof.
- **Does not connect to primes.** The apparent prime enrichment in the inverse tree is a statistical artifact of value distribution, not a structural mechanism.
- **Does not generalize beyond the sampled family.** Results for mod-32 maps with coefficients $\{3,5,7,9\}$ may not extend to other families.

### 10.3 Honest Negative Results

- **A4 failure as discriminant:** We initially hypothesized A4 as a decaying property, but it holds for both maps. This is an honest negative result. See Section 3.2.
- **K-scaling:** The preliminary observation $K_{\text{crit}} \approx \log_2(n)/5$ does not hold with increased data. We report raw values without claiming a scaling law. See Section 3.2.
- **Phase boundary:** The exact boundary at $a=4$ is theoretically elegant but inaccessible to odd-integer maps. The artificial critical map (Section 6.2 of parent paper) shows bimodal behavior, not a smooth transition. See Section 4.
- **Evolved map:** The genetic algorithm found a map better than Collatz within the fitness landscape. This does not invalidate Collatz; it shows that the landscape is richer than previously explored. See Section 6.
- **Scale exploration:** Mod 64 and mod 128 do not improve dissipation. See Section 7.4.

### 10.4 Interpretative Mapping (Heuristic)

The following analogies are offered as **heuristic intuition**, not formal claims. They are separated from the quantitative results to avoid conflating observation with interpretation. See Section 2.3 for the formal grounding.

- **"Dissipation"** = statistical decay in log-growth observables (negative drift, Definition 2.3)
- **"Energy"** = $\nu_2(n+1)$, a log-growth observable, not a physical quantity
- **"Frontier"** = empirical boundary in observable embedding space between decaying and expanding clusters (Definition 2.4)
- **"Hyper-dissipative"** = systems with strong negative drift and rapid convergence (e.g., toy hash model, Section 8)
- **"Phase locking"** (not observed): hypothetical synchronization of dynamics in phase space; our data shows irreducible phase noise in all finite embeddings

These interpretations are non-formal and serve to guide intuition. All quantitative claims are grounded in Definitions 2.1–2.4 and the computational procedures of Section 3.

---

## 11. Conclusion

We have formalized an observable embedding framework $\Phi$ (Definition 2.2) that maps discrete dynamical systems into a real vector space, and identified the convergence frontier $\mathcal{F}$ (Definition 2.4) as an emergent geometric structure in this space. Computational verification on 952 Collatz trajectories and 200 5x+1 trajectories shows that negative macroscopic drift ($\Phi_3$) is the observable that discriminates decaying from expanding behavior in our sample.

The exact 2-adic drift formula $\Phi_{\text{2-adic}}(a) = \log_2(a) - 2$ (Section 4) places Collatz as the last odd decaying map before an inaccessible boundary. A genetic algorithm discovers maps with empirical drift $-1.68$ (56$\times$ beyond the 2-adic limit), 100% termination, and 4$\times$ faster convergence (Section 6). Chang's one-bit mixing structure, valid for pure Collatz, is broken by strategically mixed maps (Section 5), suggesting that family-level approaches may be more tractable than the specific Collatz map.

The toy hash model (Section 8) demonstrates that computational proxies can exhibit structurally analogous behavior with different dissipation strength. The framework is a taxonomic and computational tool, not a proof of the Collatz conjecture, but it unifies diverse systems under a single structural language and points toward a family-level approach to the problem.

---

## References

1. T. Tao, "Almost all Collatz orbits attain almost bounded values," *arXiv:1909.03562*, 2019.
2. J. C. Lagarias, "The $3x+1$ problem and its generalizations," *Amer. Math. Monthly*, 92(1):3--23, 1985.
3. R. Bradley, *Introduction to Strong Mixing Conditions*, Heldermann Verlag, 2005.
4. Chang, "Map Balance Theorem and One-Bit Mixing in Collatz Dynamics," 2026.
