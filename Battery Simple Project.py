"""
Author : Kwadwo Sarpong
Date : 11/05/2025
Subject : Simple Battery Project
"""

import numpy as np
import matplotlib.pyplot as plt

class ThermalBattery:
    #definifng the battery attributes
    def __init__(self, mass_kg, cp_kJ_per_kgC, t_hot, t_cold, efficiency):
        self.mass_kg = mass_kg
        self.cp_kJ_per_kgC = cp_kJ_per_kgC
        self.t_hot = t_hot
        self.t_cold = t_cold
        self.efficiency = efficiency

    def energy_stored_kWh(self):
        #calculating energy stored
        return (self.mass_kg * self.cp_kJ_per_kgC * (self.t_hot - self.t_cold) * self.efficiency) / 3600


battery = ThermalBattery(50000, 1.0, 800, 200, 0.95)
print(battery.energy_stored_kWh())

t_hot_values = np.arange(200, 1001, 100)  # from 200°C to 1000°C in steps of 100

energies = []
for T in t_hot_values:
    battery = ThermalBattery(mass_kg=50000, cp_kJ_per_kgC=1.0, t_hot=T, t_cold=200, efficiency=0.95)
    energies.append(battery.energy_stored_kWh())

plt.plot(t_hot_values, energies, marker='o')
plt.title("Thermal Energy Stored vs Temperature")
plt.xlabel("Hot Temperature (°C)")
plt.ylabel("Energy Stored (kWh)")
plt.grid(True)
plt.show()
