import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate a sample time series data
np.random.seed(0)
date_range = pd.date_range(start='1/1/2020', periods=100, freq='M')
trend = np.linspace(10, 50, 100)
seasonal = 10 * np.sin(np.linspace(0, 3 * np.pi, 100))
noise = np.random.normal(0, 2, 100)
data = trend + seasonal + noise

# Create a DataFrame
df = pd.DataFrame({'Date': date_range, 'Value': data})
df.set_index('Date', inplace=True)

# Define trend component (m_t), seasonal component (s_t), and weight (w_k)
t = 20
d = 16
q = 8
X_t = int(input("Enter a number:"))

m_t = []
s_t = []
w_k = []

for i in range(1, 101):
    if i < 50:
        m_t_i = 10 + 0.8 * i + np.random.normal(0, 2)  # Upward trend with noise
    else:
        m_t_i = 50 - 0.5 * (i - 50) + np.random.normal(0, 2)  # Downward trend with noise
    w_k_i = ((2*q-1)**-1)*X_t - i
    s_t_i = 10 * np.sin(2 * np.pi * i / 12)  # Sinusoidal seasonal component
    m_t.append(m_t_i)
    s_t.append(s_t_i)
    w_k.append(w_k_i)

# Convert lists to numpy arrays
m_t = np.array(m_t)
s_t = np.array(s_t)
w_k = np.array(w_k)


# Calculate the result using the given components
result = w_k * (m_t + s_t)

# Calculate residuals
residual_component = df['Value'] - result

# Plot the components
plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(df['Value'], label='Original')
plt.legend(loc='upper left')

plt.subplot(4, 1, 2)
plt.plot(df.index, m_t, label='Trend (m_t)', color='orange')
plt.legend(loc='upper left')

plt.subplot(4, 1, 3)
plt.plot(df.index, s_t, label='Seasonal (s_t)', color='green')
plt.legend(loc='upper left')

plt.subplot(4, 1, 4)
plt.plot(df.index, residual_component, label='Residual', color='red')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
