import matplotlib.pyplot as plt

# Given time series data
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
X_t = [0, 4, 8, 7, 3, 1, 5, 8, 15, 13, 13, 10, 8, 12, 15, 18, 23, 20, 17, 15, 19, 22, 25, 29, 27, 24, 22, 26, 29]

# Calculate the trend component
d = 8
q = d // 2
m_t = []
for i in range(len(X_t)):
    sum = 0
    for j in range(-q, q+1):
        if 0 <= i+j < len(X_t):
            sum += X_t[i+j]
    m_t.append(sum / d)

# Calculate the seasonal component
w_k = []
for k in range(q, len(X_t)-q):
    sum = 0
    for j in range(-q, q+1):
        sum += X_t[k+j] - m_t[k+j]
    w_k.append(sum / (2*q+1))

# Repeat the seasonal component to match the length of the original data
s_t = w_k * (len(X_t) // len(w_k)) + w_k[:len(X_t) % len(w_k)]

# Calculate the residual component
res_t = [X_t[i] - m_t[i] - s_t[i] for i in range(len(X_t))]

# Plot the original data, trend, seasonal, and residual components
plt.figure(figsize=(10, 6))
plt.plot(t, X_t, label='Original Data')
plt.plot(t, m_t, label='Trend')
plt.plot(t, s_t, label='Seasonal')
plt.plot(t, res_t, label='Residual')
plt.legend()
plt.show()
