**The Problem Statement:** How to determine stability of an interconnected system?

**Setup:** The system is shown as a network of vertices and edges, and modeled using first-order linear differential equations $Ax=\dot{x}$
**Condition for stability:** For this system to be stable, the real parts of its eigenvalues must be non-positive

**Spontaneous Synchronization:**
**The Kuramoto Model:** This phenomenon is modeled using a population of N globally coupled oscillators
Equation: The phase $\theta_i$ of each oscillator changes over time based on its own natural frequency  $\omega_i$, and the pull of all the other oscillators (coupling strength K)
$$\dot{\theta_i}=\omega_i+\frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j-\theta_i)$$
