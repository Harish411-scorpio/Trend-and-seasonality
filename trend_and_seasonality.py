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
m_t = np.linspace(10, 50, 100)  # Linear trend
s_t = 10 * np.sin(np.linspace(0, 3 * np.pi, 100))  # Sinusoidal seasonality
w_k = 1  # Weight (can be adjusted as needed)

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
