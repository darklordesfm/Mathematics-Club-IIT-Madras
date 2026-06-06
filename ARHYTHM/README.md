**The Problem Statement:** How to determine stability of an interconnected system?

**Setup:** The system is shown as a network of vertices and edges, and modeled using first-order linear differential equations $Ax=\dot{x}$
**Condition for stability:** For this system to be stable, the real parts of its eigenvalues must be non-positive

**Spontaneous Synchronization:**
**The Kuramoto Model:** This phenomenon is modeled using a population of N globally coupled oscillators
**Equation:** The phase $\theta_i$ of each oscillator changes over time based on its own natural frequency  $\omega_i$, and the pull of all the other oscillators (coupling strength K):
$$\dot{\theta_i}=\omega_i+\frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j-\theta_i)$$
**Measuring the synchrony:** To measure how well the system as a whole is moving together, a complex order parameter r(t) is used. If r(t)=0, the system is an incoherent mess completely; if r(t)=1, the system is in perfect locked synchronization
