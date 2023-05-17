An [analytic signal](https://en.wikipedia.org/wiki/Analytic_signal) has no negative frequency components.
It always constrains the real and imaginary parts of it's Fourier transform to be a Hilbert transform pair.

In other words, if $F(j\omega) = 0 \forall \omega < 0$, it is analytic. This implies that $$ \mbox{Im}[f(t)] = P.V. \left\{ \frac{1}{\pi t}*\mbox{Re}[f(t)] \right\}$$

Let $G(j\omega) = \ln(\vert f(t)\vert +j\arg f(t)$ be the complex logarithm of some function $f(t)$. Under some conditions, $G(j\omega)$ can be analytic (one-sided in $\omega$). This allows the imaginary part of $G(j\omega)$ (the phase of $f(t)$) to be uniquely recoverable from it's real part (which corresponds to the signal's envelope)

