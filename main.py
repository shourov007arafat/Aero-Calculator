import pandas as pd
import math

print("This is a very basic calculator fo some important Aerospace related calculations")

print("press\n"
      "1-to calculate Lift\n"
      "2-to calculate Drag\n"
      "3-to calculate Thrust\n"
      "4-to calculate pH\n"
      "5-to calculate Potential of a cell by Nernst equation\n"
      "6-to calculate Propulsion Brake Specific Fuel Consumption (BSFC)\n"
      "7-to calculate Reynolds Number\n"
      "8-to calculate Stability and Control Calculations")


# def again_val_taker( ):
#     val = (input(" "))

def calculate_lift_force(air_density, velocity, wing_area, lift_coefficient):
    # Calculate lift force using the formula L = 0.5 * rho * V^2 * S * CL
    lift_force = 0.5 * air_density * velocity ** 2 * wing_area * lift_coefficient
    print(f"Lift Force: {lift_force:.2f} N")


def lift_force_input_taker():
    rho = float(input("Enter air density (kg/m³): "))
    velocity = float(input("Enter velocity (m/s): "))
    wing_area = float(input("Enter wing area (m²): "))
    lift_coefficient = float(input("Enter lift coefficient: "))

    calculate_lift_force(rho, velocity, wing_area, lift_coefficient)


def calculate_drag_force(rho, velocity, drag_coefficient, area):
    # Drag force formula: D = 0.5 * rho * V^2 * C_D * A
    drag_force = 0.5 * rho * velocity ** 2 * drag_coefficient * area
    print(f"The drag force is {drag_force:.2f} N")


def drag_force_input_taker():
    rho = float(input("Enter air density (kg/m³): "))
    velocity = float(input("Enter velocity (m/s): "))
    drag_coefficient = float(input("Enter drag_coefficient: "))
    area = float(input("Enter area: "))

    calculate_drag_force(rho, velocity, drag_coefficient, area)


def calculate_thrust(mass_flow_rate, exhaust_velocity, inlet_velocity):
    # Formula to calculate thrust force
    thrust_force = mass_flow_rate * (exhaust_velocity - inlet_velocity)
    print(f"The thrust force is: {thrust_force:.2f} N")


def thrust_input_taker():
    mass_flow_rate = float(input("Enter the mass flow rate (kg/s): "))
    exhaust_velocity = float(input("Enter the exhaust velocity (m/s): "))
    inlet_velocity = float(input("Enter the inlet velocity (m/s): "))
    calculate_thrust(mass_flow_rate, exhaust_velocity, inlet_velocity)


def nernst_potential(E_standard, n, Q, T):
    # Constants
    R = 8.314  # Gas constant in J/(mol·K)
    F = 96500  # Faraday constant in C/mol

    # Nernst equation calculation
    E = E_standard - (R * T / (n * F)) * math.log(Q)
    print(f"The cell potential is: {E:.4f} V")


# Example usage:
def nernst_potential_input_taker():
    E_standard = float(input("Enter the standard cell potential (E°) in volts: "))
    n = int(input("Enter the number of moles of electrons (n): "))
    Q = float(input("Enter the reaction quotient (Q): "))
    T = float(input("Temperature (in Kelvin): "))

    nernst_potential(E_standard, n, Q, T)


def calculate_bsfc():
    # Get user input for weight of fuel, thrust, and time
    W_fuel = float(input("Enter the weight of fuel consumed (kg): "))  # Weight of fuel
    T = float(input("Enter the thrust produced (kN): "))  # Thrust
    t = float(input("Enter the time of fuel consumption (hours): "))  # Time

    # Calculate BSFC
    BSFC = W_fuel / (T * t)  # kg/kN·h

    # Output the result
    print(f"Brake Specific Fuel Consumption (BSFC): {BSFC:.4f} kg/kN·h")


def calculate_ph():
    # Take input from the user
    h_concentration = float(input("Enter the concentration of hydrogen ions (H+) in mol/L: "))

    if h_concentration <= 0:
        print("Concentration must be greater than 0.")
    else:
        # Calculate pH
        ph = -math.log10(h_concentration)
        print(f"The pH of the solution is: {ph:.2f}")


def calculate_reynolds_number():
    # Get user input for each variable
    density = float(input("Enter the fluid density (kg/m³): "))
    velocity = float(input("Enter the fluid velocity (m/s): "))
    length = float(input("Enter the characteristic length (m): "))
    viscosity = float(input("Enter the dynamic viscosity (Pa·s or kg/(m·s)): "))

    # Calculate Reynolds number
    Re = (density * velocity * length) / viscosity
    print(f"The Reynolds number is: {Re}")

val = input("")

if not val.isdigit():
    print("This is not an integer.Please provide an integer between 1-9")

else:
    val = int(val)
    if val <= 9 and val >= 1:
        if val == 1:
            lift_force_input_taker()
        if val == 2:
            drag_force_input_taker()
        if val == 3:
            thrust_input_taker()
        if val == 4:
            calculate_ph()
        if val == 5:
            nernst_potential_input_taker()
        if val == 6:
            calculate_bsfc()
        if val == 7:
            calculate_reynolds_number()

    else:
        print("please put the value in between 1-9")

