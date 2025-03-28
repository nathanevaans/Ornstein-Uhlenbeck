## Solution of the Ornstein-Uhlenbeck Process

The solution to this SDE can be derived using the method of integrating factors. First, we rewrite the equation as:

$$
dX_t + \theta X_t dt = \theta \mu dt + \sigma dW_t
$$

This is a first-order linear SDE, and we solve it using an integrating factor. The integrating factor is given by:

$$
e^{\theta t}
$$

Multiplying both sides of the equation by the integrating factor:

$$
e^{\theta t} dX_t + \theta e^{\theta t} X_t dt = \theta \mu e^{\theta t} dt + \sigma e^{\theta t} dW_t
$$

The left-hand side is the derivative of $e^{\theta t} X_t$, so we have:

$$
d( e^{\theta t} X_t ) = \theta \mu e^{\theta t} dt + \sigma e^{\theta t} dW_t
$$

Integrating both sides:

$$
e^{\theta t} X_t = X_0 + \theta \mu \int_0^t e^{\theta s} ds + \sigma \int_0^t e^{\theta s} dW_s
$$

Simplifying the integrals:

$$
e^{\theta t} X_t = X_0 + \frac{\theta \mu}{\theta} \left( e^{\theta t} - 1 \right) + \sigma \int_0^t e^{\theta s} dW_s
$$

Finally, the solution for $X_t$ is:

$$
X_t = X_0 e^{-\theta t} + \mu (1 - e^{-\theta t}) + \sigma \int_0^t e^{-\theta(t-s)} dW_s
$$

## Expectation of $X_t$

The expectation of $X_t$ is:

$$
\mathbb{E}[X_t] = E[X_0] e^{-\theta t} + \mu (1 - e^{-\theta t}) + \mathbb{E}\left[ \sigma e^{-\theta t} \int_0^t e^{-\theta(t-s)} dW_s \right]
$$

Since $\mathbb{E}[dW_s] = 0$, the expectation of the stochastic integral is zero. Thus:

$$
\mathbb{E}[X_t] = \mathbb{E}[X_0] e^{-\theta t} + \mu (1 - e^{-\theta t})
$$

As $t \to \infty$, $e^{-\theta t} \to 0$, so:

$$
\mathbb{E}[X_t] \to \mu
$$

Therefore, the mean of $X_t$ tends to the long-term mean $\mu$ as time $t$ increases.

## Conclusion

The Ornstein-Uhlenbeck process is a mean-reverting process, and the solution shows that the expected value of $X_t$ converges to $\mu$ as $t \to \infty$, which confirms the mean-reverting property of the process.
