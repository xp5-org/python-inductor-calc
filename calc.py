import math

# Input values in picofarads and microhenries
capacitance_pf = float(input("Enter capacitance (in picofarads): "))
inductance_uh = float(input("Enter inductance (in microhenries): "))
resistance = float(input("Enter resistance (in ohms): "))

# Convert capacitance to farads and inductance to henrys
capacitance = capacitance_pf * 1e-12  # 1 picofarad = 1e-12 farads
inductance = inductance_uh * 1e-6     # 1 microhenry = 1e-6 henrys

# Calculate resonant frequency (in kilohertz)
resonant_frequency = 1 / (2 * math.pi * math.sqrt(inductance * capacitance)) / 1e3

# Calculate Q factor
q_factor = 1 / resistance * math.sqrt(inductance / capacitance)

# Calculate bandwidth (in kilohertz)
bandwidth = resonant_frequency / q_factor

# Calculate damping ratio
#damping_ratio = 1 / (2 * resistance) * math.sqrt(inductance / capacitance)
damping_ratio = resistance / (2 * math.sqrt(inductance / capacitance))

# Output the results
print("\nResults:")
print(f"Resonant Frequency: {resonant_frequency:.4f} kHz")
print(f"Q Factor: {q_factor:.2f}")
print(f"Bandwidth: {bandwidth:.4f} kHz")
print(f"Damping Ratio: {damping_ratio:.8f}")