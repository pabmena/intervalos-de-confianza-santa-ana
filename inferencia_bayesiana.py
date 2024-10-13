# inferencia_bayesiana.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Datos observados
n = 10  # Número total de clientes
x = 1   # Número de clientes en mora

# Parámetros de la distribución a priori Beta(α, β)
alpha_prior = 1
beta_prior = 5

# Actualización de los parámetros para la distribución posteriori
alpha_posterior = alpha_prior + x
beta_posterior = beta_prior + n - x

# Media y varianza de la distribución posteriori
mean_posterior = alpha_posterior / (alpha_posterior + beta_posterior)
variance_posterior = (alpha_posterior * beta_posterior) / ((alpha_posterior + beta_posterior) ** 2 * (alpha_posterior + beta_posterior + 1))

print(f"Distribución a posteriori: Beta({alpha_posterior}, {beta_posterior})")
print(f"Media posteriori: {mean_posterior:.4f}")
print(f"Varianza posteriori: {variance_posterior:.6f}")

# Gráfico de la distribución a priori y posteriori
p = np.linspace(0, 1, 100)
prior = beta.pdf(p, alpha_prior, beta_prior)
posterior = beta.pdf(p, alpha_posterior, beta_posterior)

plt.figure(figsize=(10, 6))
plt.plot(p, prior, 'r--', label=f'Prior Beta({alpha_prior}, {beta_prior})')
plt.plot(p, posterior, 'b-', label=f'Posterior Beta({alpha_posterior}, {beta_posterior})')
plt.title('Distribuciones a Priori y Posteriori del Porcentaje de Morosidad')
plt.xlabel('Porcentaje de Morosidad (p)')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)

# Guardar el gráfico en un archivo
plt.savefig('distribucion_morosidad.png', dpi=300)
plt.close()

