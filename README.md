

An [analytic signal](https://en.wikipedia.org/wiki/Analytic_signal) has no negative frequency components.
It always constrains the real and imaginary parts of it's Fourier transform to be a Hilbert transform pair.

In other words, if $F(j\omega) = 0 \forall \omega < 0$, it is analytic. This implies that $$ \Im[f(t)] = P.V. \left\{ \frac{1}{\pi t}*\Re[f(t)] \right\}$$

If the frequency domain function is a complex logarithm, which also happens to be analytic, then this allows the phase to be uniquely recoverable from the logarithm of the magnitude (which is basically the signal's envelope).

