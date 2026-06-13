import time
import board
import digitalio
import analogio

# ==========================================
# PIN CONFIGURATION (RP2040)
# ==========================================
# Stepper driver interface (TMC2209)
STEP_PIN = board.GP2
DIR_PIN = board.GP3
EN_PIN = board.GP4

# Sensors and User Input
FSR_PIN = board.GP26          # ADC0
PULSE_DAB_PIN = board.GP15    # Digital Interrupt Switch

# ==========================================
# HARDWARE INITIALIZATION
# ==========================================
# Stepper Outputs
step_out = digitalio.DigitalInOut(STEP_PIN)
step_out.direction = digitalio.Direction.OUTPUT

dir_out = digitalio.DigitalInOut(DIR_PIN)
dir_out.direction = digitalio.Direction.OUTPUT

en_out = digitalio.DigitalInOut(EN_PIN)
en_out.direction = digitalio.Direction.OUTPUT
en_out.value = True  # Start disabled (Active Low)

# Analog Input (Force Sensitive Resistor)
fsr_in = analogio.AnalogIn(FSR_PIN)

# Safety Pulse-Dab Switch (Normally open, pull-up triggers on press)
dab_switch = digitalio.DigitalInOut(PULSE_DAB_PIN)
dab_switch.direction = digitalio.Direction.INPUT
dab_switch.pull = digitalio.Pull.UP

# ==========================================
# PARAMETERS & CALIBRATION
# ==========================================
ADC_MIN_THRESHOLD = 5000   # Noise deadzone threshold (out of 65535)
ADC_MAX_LIMIT = 60000       # Max force saturation threshold
MIN_DELAY_US = 200          # Fast speed delay (lower is faster)
MAX_DELAY_US = 5000         # Slow speed delay (higher is slower)

# ==========================================
# UTILITY & DRIVER LOGIC
# ==========================================
def map_value(val, in_min, in_max, out_min, out_max):
    """Linearly maps a value from one range to another."""
    if val <= in_min:
        return out_max
    if val >= in_max:
        return out_min
    return out_min + (val - in_min) * (out_max - out_min) / (in_max - in_min)

def execute_step():
    """Generates a single step pulse to the TMC2209 driver."""
    step_out.value = True
    time.sleep_seconds(0.000002)  # 2 microsecond step pulse high
    step_out.value = False

# ==========================================
# MAIN EXECUTION LOOP
# ==========================================
print("DP-1 Control Firmware initialized.")
en_out.value = False  # Enable motor outputs

while True:
    # --- Safety Interrupt Check ---
    # The Pulse-Dab switch acts as an immediate safety pause or pulse activator.
    # If the switch is pressed (reading Low due to pull-up), halt motor operation.
    if not dab_switch.value:
        en_out.value = True  # Cut power to motor coils (coast)
        print("[SAFETY] Pulse-Dab switch pressed. Motion paused.")
        
        # Debounce/wait until released
        while not dab_switch.value:
            time.sleep(0.05)
            
        en_out.value = False  # Re-enable motor
        print("[SAFETY] System armed. Resuming operation.")
        continue

    # --- Read Grip Pressure (FSR) ---
    raw_force = fsr_in.value
    
    # --- Motor Feed Logic ---
    if raw_force > ADC_MIN_THRESHOLD:
        dir_out.value = True  # Feed forward
        
        # Map analog force directly to dynamic step frequency
        step_delay = map_value(raw_force, ADC_MIN_THRESHOLD, ADC_MAX_LIMIT, MIN_DELAY_US, MAX_DELAY_US)
        
        # Execute feed step
        execute_step()
        
        # Delay between steps (CircuitPython sleep)
        time.sleep(step_delay / 1000000.0)
    else:
        # Idle state - wait briefly to avoid spinning CPU cycles
        time.sleep(0.01)
