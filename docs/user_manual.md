# Project Delta Pen (DP-1) User Operation Manual

A practical reference manual for operators using the DP-1 motorized TIG wire feeder in production environments.

---

## 1. Initial Setup
1. Feed the TIG filler wire into the rear PTFE sheath until it interfaces with the V-Groove drive wheel inside the pen assembly.
2. Hold down the **Pulse-Dab Switch** (safety halt) while threading the wire past the drive wheel to prevent manual gear damage.
3. Release the switch once the wire emerges from the copper contact nozzle tip at the front of the pen.
4. Adjust the idler tension thumb screw until the wire is held securely in the V-groove.

---

## 2. Operation Modes

### Grip Force Feed Mode (FSR Control)
* **Start Feeding**: Apply gentle squeeze pressure to the FSR sensor strip on the grip section.
* **Variable Velocity**: Increase squeeze force to speed up the feed rate (ranges from fine dabbing to continuous high-speed deposition).
* **Stop Feeding**: Release finger pressure. The controller immediately stops step pulses.

### Pulse-Dab Switch Interaction (GPIO 15)
* **Instant Pause**: Pressing the Pulse-Dab switch acts as an asynchronous hardware-level interrupt. All stepping stops instantly, and the motor driver coil power is cut to allow manual wire slippage or adjustment.
* **Emergency Halt**: In the event of a sticking wire, pressing this switch disables the stepper outputs.

---

## 3. Calibration Procedures
If the wire feeds too slowly or fails to start at low finger force, adjust the ADC noise floor parameters in [firmware/main.py](file:///home/_____/Documents/antigravity/peaceful-franklin/firmware/main.py):

* **`ADC_MIN_THRESHOLD`**: Lower this value if you have light touch or smaller fingers. Increase it if resting your finger triggers unwanted feeding.
* **`MIN_DELAY_US` / `MAX_DELAY_US`**: Modify these step delays to tune minimum/maximum wire speed to match your welding current.
