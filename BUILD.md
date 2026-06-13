# BUILD.md: Project Delta Pen Assembly Guide
> **Model: DP-1**  
> **Precision Level: Toolroom/R&D**

This guide covers the step-by-step physical assembly of the Delta Pen housing, driving components, and electronic sensors.

---

## Bill of Materials (BOM)

### 1. Actuation & Drive
* **Motor**: NEMA 8 Stepper Motor (20mm length, 1.8° step angle).
* **Drive Wheel**: Hardened steel V-Groove wheel (5mm bore, matching wire gauge).
* **Idler**: Ball-bearing U-groove pressure wheel.
* **Tensioner**: M3 steel adjustment thumb screw with compression spring.

### 2. Sensors & Electronics
* **Microcontroller**: RP2040 (e.g., Raspberry Pi Pico or Qt Py RP2040).
* **Driver**: TMC2209 StepStick module.
* **Force Sensor**: Interlink FSR 402 strip (or equivalent analog force-sensitive resistor).
* **Interrupt Switch**: SPST momentary micro-switch (Pulse-Dab Switch).

---

## Assembly Sequence

### Step 1: Drive Assembly Prep
1. Press-fit the **V-groove drive wheel** onto the NEMA 8 stepper motor shaft.
2. Align the groove with the central axis line of the motor faceplate.
3. Torque the M3 grub screws on the drive wheel to **0.6 N·m** using a hex key.

### Step 2: Idler Tensioner Mounting
1. Mount the spring-loaded idler arm onto the CAD-printed chassis base.
2. Insert the compression spring and secure the M3 thumb screw through the tensioner block.
3. Verify the idler arm moves freely without binding.

### Step 3: Coaxial Path Alignment
1. Thread the **PTFE liner** (inner diameter matching the wire size + 0.2mm) through the rear entry channel of the pen chassis.
2. Position the exit nozzle guide within **2.0 mm** of the V-groove pinch zone to prevent the filler wire from buckling under load.

### Step 4: FSR Strip Placement
1. Adhere the **FSR sensor strip** along the ergonomic index finger indentation on the chassis exterior.
2. Route the flexible tail through the chassis internal cable channel to the RP2040 compartment.
3. Ensure no sharp plastic edges bend the sensor tail.

### Step 5: Wiring & Controller Integration
1. Solder the FSR sensor to a voltage divider circuit (10kΩ pulldown resistor to ground, analog terminal to RP2040 **GP26/ADC0**).
2. Wire the pulse-dab switch to **GPIO 15** (internal pull-up enabled).
3. Connect the step/dir interface to the TMC2209 driver board according to the pin configuration.

---

## Validation & Calibration

Before powering on the motor driver, perform the following mechanical checks:
* **Friction Check**: Feed a length of wire manually by turning the motor shaft. There should be uniform friction and no slippage.
* **Tension Adjustment**: Tighten the M3 tensioner thumb screw until the wire feeds against slight hand resistance, then tighten another half-turn. Do not overtighten to avoid flattening soft filler wires (like aluminum).
