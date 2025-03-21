import streamlit as st

from pathlib import Path

from maths import plot

st.markdown(
    """
    # Ornstein-Uhlenbeck Process

    The Ornstein-Uhlenbeck Process is a stochastic process that satisfies the following Stochastic Differential Equation (SDE):

    $$
    dX_t = \\theta(\\mu - X_t) dt + \\sigma dW_t
    $$

    where:

    - $\\theta > 0$ : The rate at which  $X_t$ reverts to the mean $\mu$.
    - $\mu$ : The long-term mean.
    - $\sigma$ : The volatility (diffusion strength).
    - $W_t$ : Standard Brownian motion.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    theta = st.slider("$\\theta$", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
with col2:
    mu = st.slider("$\mu$", min_value=-5.0, max_value=5.0, value=0.0, step=0.1)
with col3:
    sigma = st.slider("$\sigma$", min_value=0.1, max_value=2.0, value=0.5, step=0.1)

plot_data = plot(theta, mu, sigma)
# st.line_chart(plot_data)
st.altair_chart(plot_data, use_container_width=True)

file = Path('./article.md').read_text()
st.markdown(file)
