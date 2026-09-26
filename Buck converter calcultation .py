```python
# Buck Converter Calculator
# Basic CCM (Continuous Conduction Mode) calculations

import math

print("===================================")
print("       BUCK CONVERTER CALCULATOR")
print("===================================")

Vin = float(input("Input voltage Vin (V): "))
Vout = float(input("Output voltage Vout (V): "))
Iout = float(input("Output current Iout (A): "))
fs = float(input("Switching frequency (kHz): ")) * 1000
efficiency = float(input("Estimated efficiency (%): ")) / 100
inductor_ripple_percent = float(
    input("Inductor ripple current (% of Iout): ")
)
capacitor_ripple = float(
    input("Allowed output voltage ripple (V): ")
)

# -----------------------------
# 1. Duty Cycle
# -----------------------------
D = Vout / Vin

# -----------------------------
# 2. Inductor ripple current
# -----------------------------
delta_IL = Iout * inductor_ripple_percent / 100

# -----------------------------
# 3. Inductor value
# ΔIL = ((Vin - Vout) * D) / (L * fs)
# L = ((Vin - Vout) * D) / (ΔIL * fs)
# -----------------------------
L = ((Vin - Vout) * D) / (delta_IL * fs)

# -----------------------------
# 4. Output capacitor
# ΔV = ΔIL / (8 * fs * C)
# C = ΔIL / (8 * fs * ΔV)
# -----------------------------
C = delta_IL / (8 * fs * capacitor_ripple)

# -----------------------------
# 5. Input current
# Pin = Pout / efficiency
# Iin = Pin / Vin
# -----------------------------
Pout = Vout * Iout
Pin = Pout / efficiency
Iin = Pin / Vin

# -----------------------------
# 6. Inductor peak and minimum current
# -----------------------------
IL_peak = Iout + (delta_IL / 2)
IL_min = Iout - (delta_IL / 2)

# -----------------------------
# 7. MOSFET voltage stress
# -----------------------------
MOSFET_voltage = Vin

# -----------------------------
# 8. Diode voltage stress
# -----------------------------
Diode_voltage = Vin

# -----------------------------
# Display results
# -----------------------------
print("\n========== RESULTS ==========")

print(f"Duty Cycle              : {D * 100:.2f} %")
print(f"Output Power            : {Pout:.2f} W")
print(f"Estimated Input Power   : {Pin:.2f} W")
print(f"Average Input Current   : {Iin:.2f} A")

print("\n--- Inductor ---")
print(f"Inductor Ripple Current : {delta_IL:.3f} A")
print(f"Inductor Value          : {L * 1e6:.2f} uH")
print(f"Inductor Peak Current   : {IL_peak:.3f} A")
print(f"Inductor Minimum Current: {IL_min:.3f} A")

print("\n--- Capacitor ---")
print(f"Output Capacitor        : {C * 1e6:.2f} uF")
print(f"Allowed Voltage Ripple  : {capacitor_ripple:.3f} V")

print("\n--- Switch / Diode ---")
print(f"MOSFET Voltage Stress   : {MOSFET_voltage:.2f} V")
print(f"Diode Voltage Stress    : {Diode_voltage:.2f} V")

print("\n===================================")
print("Use suitable voltage/current safety")
print("margins when selecting components.")
print("===================================")
```

**Example input:**

* Vin = 24 V
* Vout = 12 V
* Iout = 5 A
* Switching frequency = 100 kHz
* Efficiency = 90%
* Inductor ripple = 30%
* Output ripple = 0.1 V

The program then calculates the required **duty cycle, inductance, capacitance, ripple current, peak inductor current, input current, and approximate switch/diode voltage stress**.
