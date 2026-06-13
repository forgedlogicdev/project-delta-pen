# Project Delta Pen (DP-1) Engineering & Design Blueprint
> **Version**: 1.1.0  
> **Classification**: Technical Design Proposal / R&D Guide  
> **Authors**: Lead Systems Architect & Engineering Team  

This document serves as the high-level structural, mechanical, and electrical blueprint for the **Project Delta Pen (DP-1)**. It addresses the engineering challenges of miniaturized, coaxial wire-feeding, structural thermodynamics, and force-sensitive control loops.

---

## 1. Ergonomic & Structural Architecture

The primary design challenge of the DP-1 is maintaining hand comfort over long duty cycles while carrying an active actuator (NEMA 8 stepper motor).

```
                     [ CENTER OF MASS ]
                             ▼
  ┌───────────────────────────────────┬──────────────┐
  │         ERGO GRIP SECTION         │ MOTOR BLOCK  │ ===> Rear Harness
  │  (Lightweight SLS Nylon / Carbon) │ (6061 Alum)  │      (Power & Gas)
  └───────────────────────────────────┴──────────────┘
  ◄────────────── 100mm ─────────────►◄──── 20mm ────►
```

### Material Selection Comparison
We evaluated three primary fabrication paths for the pen housing:

| Fabrication Method | Recommended Materials | Tensile Strength | Thermal Conductivity | Pro/Con Analysis |
|---|---|---|---|---|
| **SLS 3D Printing (Recommended)** | Nylon PA12 / Carbon-Filled | ~48 MPa | Low (~0.25 W/m·K) | **Pros**: Excellent weight distribution, complex internal wire routing. <br>**Cons**: Poor heat dissipation. |
| **CNC Machining** | 6061-T6 Anodized Aluminum | ~310 MPa | High (~167 W/m·K) | **Pros**: Extreme durability, acts as a heatsink. <br>**Cons**: Increases hand weight (fatigue), requires electrical isolation. |
| **FDM 3D Printing** | PETG / Polycarbonate (PC) | ~60 MPa | Low | **Pros**: Fast prototyping, low cost. <br>**Cons**: Anisotropic strength (weak layer bonding under wire tension). |

### Engineering Decision
* **Chassis Body**: Select **SLS Nylon PA12** for its structural density, toughness, and thermal isolation from the welding environment.
* **Motor & Tension Block**: Select CNC machined **6061-T6 Aluminum**. This block mounts directly to the NEMA 8 motor to act as a heat-sink, protecting the user's hand from motor-coil heat.

---

## 2. Mechanical Drive & Torque Physics

Feeding rigid filler wire (such as 2.4mm ER70S-6 steel or ER4043 aluminum) requires significant linear push force without buckling or crushing the wire.

```
       Force (Idler Pressure)
              │
              ▼
   [ U-Groove Idler Bearing ]
  ═════════════════════════════  ◄─── Filler Wire
   [ V-Groove Drive Gear ]
              ▲
              │
         Motor Torque
```

### Torque Calculations
To calculate the minimum holding torque required for the stepper motor ($T_{motor}$):
$$T_{motor} = F_{push} \times r_{drive}$$

Where:
* $F_{push}$ = Linear force required to feed wire through the PTFE tube (typically 12 N to 20 N depending on bends).
* $r_{drive}$ = Radius of the drive wheel ($6\text{ mm} = 0.006\text{ m}$).

$$T_{motor} = 20\text{ N} \times 0.006\text{ m} = 0.12\text{ N·m} = 12\text{ N·cm}$$

* **Motor Specification**: A standard NEMA 8 stepper motor (e.g., 20mm body) provides approximately $1.6\text{ to }3.0\text{ N·cm}$ holding torque. This is **insufficient** for direct drive under heavy friction.
* **Solution**: 
  1. Use a **geared NEMA 8** (e.g., 5:1 planetary gearbox) to multiply torque to $15\text{ N·cm}$ while maintaining low weight.
  2. Implement ultra-low friction **polished PTFE liners** (1.8mm ID for 1.6mm wire) to keep $F_{push}$ under $4\text{ N}$, which keeps direct drive viable.

---

## 3. Electronics & Driver Configuration

The **TMC2209** stepper driver must be software-configured via UART or physical hardware pins to balance noise, heat, and torque.

### StealthChop™ vs. SpreadCycle™
* **StealthChop (Quiet)**: Reduces motor noise to near silent. However, high-current peaks can cause step losses when the filler wire encounters friction.
* **SpreadCycle (High Torque)**: Offers superior torque dynamics and speed control, but introduces standard stepper motor whine.
* **Hybrid Configuration (Recommended)**: Set the threshold velocity in firmware. Below 20 mm/s (normal welding speeds), run StealthChop for silent operation. Above 20 mm/s, transition to SpreadCycle for peak driving torque.

### Thermal Dissipation
Operating a NEMA 8 motor close to its current limit (0.6A) inside a hand-held plastic pen causes heat accumulation. 
* Set motor current limit ($I_{rms}$) to **70% of rated capacity** ($0.4A$) in the driver settings.
* Implement an auto-standby power down: if the FSR has not registered force for 5 seconds, cut driver coil current to **10%** to prevent pen heat buildup.

---

## 4. Force-Sensitive Control Loop

A simple linear mapping of pressure to speed results in jerky wire feeding. The control loop must implement smoothing and threshold curves.

```
 Feed Rate (mm/s)
   │
120│                                  / (Exponential ramp)
   │                                 /
   │                                /
   │                       ________/
  0│───────────────────────
   └───[Deadzone]───────────► FSR ADC Value (0-65535)
     0 - 8000            60000
```

### Proportional-Derivative (PD) Signal Smoothing
The firmware reads the FSR ADC value and processes it using a low-pass filter (Exponential Moving Average) to prevent jitter:

$$V_{smooth} = \alpha \cdot V_{raw} + (1 - \alpha) \cdot V_{prev}$$

Where $\alpha = 0.15$ provides clean damping without noticeable input lag.

### Safety State Machine
The safety interrupt must follow a strict non-blocking hardware design:

```
  ┌──────────────┐      FSR Squeezed      ┌──────────────┐
  │  Idle State  ├───────────────────────►│ Feeding State│
  └──────▲───────┘                        └──────┬───────┘
         │                                       │
         │          Pulse-Dab Pressed            │
         └───────────────────────────────────────┘
```
When the `Pulse-Dab` switch is closed (pull-up pulled low), the RP2040 triggers an immediate interrupt, disabling the `EN` pin of the TMC2209 and ignoring FSR values until the switch is reset.

---

## 5. Welding Gas & Arc Integration

Shielding gas (Argon) must flow coaxially to shield the weld puddle from atmospheric contamination.

* **Gas Seal**: The shielding gas channel runs parallel to the wire feeding channel. It exits through internal gas diffusers in the front housing to create laminar flow.
* **Heat Shielding**: The ceramic gas cup (typically Size 6 or 8) is threaded onto a custom brass gas lens adapter. This lens isolates the printed plastic pen chassis from the high heat of the tungsten electrode.
