**The Problem Statement:** How to determine stability of an interconnected system?

**Setup:** The system is shown as a network of vertices and edges, and modeled using first-order linear differential equations $Ax=\dot{x}$
**Condition for stability:** For this system to be stable, the real parts of its eigenvalues must be non-positive

**Spontaneous Synchronization:**
**The Kuramoto Model:** This phenomenon is modeled using a population of N globally coupled oscillators
**Equation:** The phase $\theta_i$ of each oscillator changes over time based on its own natural frequency  $\omega_i$, and the pull of all the other oscillators (coupling strength K):
$$\dot{\theta_i}=\omega_i+\frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j-\theta_i)$$
**Measuring the synchrony:** To measure how well the system as a whole is moving together, a complex order parameter r(t) is used. If r(t)=0, the system is an incoherent mess completely; if r(t)=1, the system is in perfect locked synchronization.

The model is scaled up to an infinite number of oscillators ($N\rightarrow\infty$) and uses a density function $\rho(\theta,\omega,t)$ to track them. The evolution of this density is governed by a conservation equation: $$\frac{\partial\rho}{\partial t}=-\frac{\partial}{\partial\theta}(\rho v)$$. By assuming a steady state, the oscillators are divided into two distinct groups: "_locked_" (moving together) and "_drifting_" (moving independently).
Evaluating the integrals for these two groups as $r\rightarrow0+$ reveals the critical threshold where synchronization begins: $K_c=\frac{2}{\pi g(0)}$. This sudden transition point is classified mathematically as a supercritical pitchfork bifurcation.

**Simulation:** 100 independent oscillators are initialized with normally distributed natural frequencies and uniform starting phases. The output graphs clearly visualize the phases locking together as time progresses. Furthermore, plotting the order parameter against the coupling constant confirms the theoretical math: the system's synchrony ($r$) jumps up dramatically only after $K$ surpasses the critical threshold. 

Used https://github.com/fabridamicelli/kuramoto to help with our simulations.
Idea came up after seeing https://www.youtube.com/watch?v=t-_VPRCtiUg Veritasium video
