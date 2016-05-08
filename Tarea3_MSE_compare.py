#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Plot the difference between MSE(S^2) and MSE(\hat{\sigma}^2) to
# know which MSE is larger.

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(2, 100, 0.1)

sigma = 1  # Sigma is irrelevant for function behavior
delta_MSE = [(n_i + 1)/(n_i * (n_i - 1)) * sigma**4 for n_i in n]

plt.plot(n, delta_MSE)
plt.xlabel('n')
plt.ylabel('$\Delta$ MSE = MSE($S^{2}$) - MSE($\hat{\sigma}^{2}$)')
# plt.savefig('T3_MSE_compare.pdf')
plt.show()