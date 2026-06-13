# Project Delta Pen (DP-1) Technical Specifications
> **Revision: 1.0.2**

This document details the engineering limits, electrical characteristics, and force sensor curves for the DP-1.

---

## 1. Physical Dimensions & Weights
* **Total Length (Chassis Only)**: 120 mm
* **Grip Diameter**: 14 mm to 18 mm (ergonomic taper)
* **Dry Weight**: 85g (excluding cable harness and stepper motor)
* **Total Operating Weight**: 142g (with NEMA 8 motor attached)

---

## 2. Stepper Actuation Parameters
* **Motor Type**: NEMA 8 Stepper (Dual Phase, bipolar)
* **Rated Current**: 0.6A per phase
* **Step Angle**: 1.8° per step (200 full steps per revolution)
* **Microstepping**: 1/16 microstepping configured on TMC2209 driver (3200 steps/rev)
* **Wire Feed Velocity Range**: 5 mm/s to 120 mm/s (controlled dynamically via FSR)

---

## 3. FSR Pressure Mapping Curve
The Interlink FSR 402 strip input is read through a 10-bit or 12-bit ADC on the RP2040. The force response follows an exponential curve:

| Applied Force (N) | Resistance (Ω) | ADC Voltage (V, 3.3V Ref) | Feed Rate (mm/s) |
|---|---|---|---|
| < 0.2 N | > 1 MΩ (Open) | < 0.15 V | 0 (Idle) |
| 0.5 N | ~ 10 kΩ | ~ 1.10 V | 10 mm/s |
| 2.0 N | ~ 2 kΩ | ~ 2.50 V | 45 mm/s |
| > 10.0 N | < 1 kΩ (Sat) | ~ 3.10 V | 120 mm/s |

---

## 4. Electrical Connections

```
    [RP2040 GPIO]                     [TMC2209 Driver]
    GP2 (Step) ──────────────────────► STEP
    GP3 (Dir)  ──────────────────────► DIR
    GP4 (En)   ──────────────────────► EN (Active Low)
    3.3V OUT   ───────┬──────────────► VDD (Logic)
                      │
                   [FSR]
                      │
    GP26 (ADC0) ◄─────┴───[10kΩ Pulldown]───► GND
```
