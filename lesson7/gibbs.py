import numpy as np

def gibbs(energies: np.ndarray, temperature: float) -> np.ndarray:
    KB = 1.38064852e-23 # Boltzmann's constant in Joules/Kelvin
    partition = np.exp(-1 * energies / (KB*temperature))
    return partition / sum(partition)

def better_gibbs(
      energies: np.ndarray, temperature: float
    ) -> np.ndarray:
    KB = 1.38064852e-23 # Boltzmann's constant in Joules/Kelvin
    min_energy = energies.min()
    partition = np.exp(-1*(energies-min_energy)/(KB*temperature))
    return partition / sum(partition)