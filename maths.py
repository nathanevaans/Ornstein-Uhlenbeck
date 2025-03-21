import numpy as np
import pandas as pd
import altair as alt


def plot(theta, mu, sigma):
    T = 5
    N = 500
    dt = T / N
    sqrt_dt = np.sqrt(dt)
    ts = np.linspace(0, T, N)
    num_paths = 5

    # Generate a random X_0 such that it will still converge
    X_0 = 5

    # Euler-Maruyama Scheme
    X = np.zeros((num_paths, N))
    X[:, 0] = X_0
    for i in range(1, N):
        dW = sqrt_dt * np.random.randn(num_paths)
        X[:, i] = X[:, i - 1] + theta * (mu - X[:, i - 1]) * dt + sigma * dW

    # return pd.DataFrame(X.T, columns=[f"Path {i+1}" for i in range(num_paths)], index=ts)
    df = pd.DataFrame(X.T, columns=[f"Path {i + 1}" for i in range(num_paths)], index=ts)

    # Reshape data for Altair
    df_reset = df.reset_index().melt(id_vars=['index'], value_vars=[f"Path {i + 1}" for i in range(num_paths)],
                                     var_name='Path', value_name='X(t)')
    df_reset.rename(columns={'index': 'Time'}, inplace=True)

    # Create the base Altair plot
    chart = alt.Chart(df_reset).mark_line().encode(
        x='Time',
        y=alt.Y('X(t)', scale=alt.Scale(domain=[-6.5, 6.5]), title='X'),  # Set the fixed y-axis range
        color=alt.Color('Path', legend=None)  # Remove the legend
    ).properties(
        width=800,
        height=400
    )

    # Add horizontal line for mu
    line_mu = alt.Chart(pd.DataFrame({'y': [mu]})).mark_rule(color='white', size=2, strokeDash=[4, 4]).encode(
        y='y'
    )

    # Combine the plot with the horizontal line
    final_chart = chart + line_mu

    # Set fixed axis limits
    final_chart = final_chart.configure_axis(
        domainColor='black',
        tickColor='black',
    ).configure_view(
        strokeWidth=0
    )

    return final_chart
