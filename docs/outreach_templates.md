# Project Delta Pen (DP-1) Outreach Email Templates
> **Classification: External Communication & Marketing Briefs**

This document tracks outreach templates (in both plain text and styled HTML format) used for pitching the DP-1 technology.

---

## 1. Styled HTML Templates
HTML files are fully styled with embedded images, buttons, and custom layout tables:

*   **[docs/adafruit_pitch.html](file:///home/_____/Documents/antigravity/peaceful-franklin/docs/adafruit_pitch.html)**: Styled pitch for Adafruit featuring the RP2040 Silicon and CircuitPython stack.
*   **[docs/ck_pitch.html](file:///home/_____/Documents/antigravity/peaceful-franklin/docs/ck_pitch.html)**: Styled B2B proposal for CK Worldwide featuring the physical mockup render and engineering specifications.

---

## 2. Plain Text Outreach Emails

### Pitch 1: Adafruit (support@adafruit.com)
```text
Subject: Project Showcase: Motorized Coaxial TIG Welding Pen (Powered by RP2040 & CircuitPython)

Hi Adafruit Team,

I wanted to share a project I've been developing that applies Adafruit's favorite ecosystem—the RP2040 and CircuitPython—directly to industrial metal fabrication. 

It’s called Project Delta Pen (DP-1): an ergonomic, motorized coaxial TIG welding wire feeder. 

The pen uses an FSR strip on the index grip to dynamically map finger force to stepper motor feed speed, letting welders deposit filler metal with high precision. It is driven by a TMC2209 silent stepper driver and is powered entirely by CircuitPython on the RP2040. 

I’ve engineered a safety halt state machine using hardware interrupts on the RP2040 to guarantee instant feed stops, preventing wire overrun in industrial conditions.

Here is the GitHub repository detailing the OpenSCAD chassis files, build sheets, and current control loop:
https://github.com/forgedlogicdev/project-delta-pen

I’d love to know if this is something you would be interested in featuring on the Adafruit blog, or if you'd be open to a quick chat about optimizing FSR input conditioning.

Best regards,
ForgedLogic
```

### Pitch 2: CK Worldwide (tech@ckworldwide.com)
```text
Subject: Technical Proposal: Integrated Coaxial Motorized Wire Feeder Retrofit for TIG Torches

Dear CK Worldwide Technical Team,

As a manufacturer of industry-leading TIG welding equipment, you are well-aware of the primary ergonomic bottlenecks in manual TIG welding: hand fatigue, rotational torque from off-axis wire feeding, and deposit consistency over long duty cycles.

To address this, we have prototyped the Project Delta Pen (DP-1), a lightweight, motorized coaxial TIG wire feeder that mounts directly inline with the torch axis. 

By routing the filler wire coaxially through the centerline axis of the pen-like modifier, we eliminate off-axis drag and rotational torque. The device is powered by an embedded RP2040 microcontroller and driven by a micro-stepper motor mated to a hardened V-groove pinch wheel. It utilizes a Force Sensitive Resistor (FSR) strip along the index grip, allowing the operator to dynamically adjust the feed rate (0 to 120 mm/s) with simple finger pressure.

We have published our high-level mechanical design blueprint and initial specifications here:
https://github.com/forgedlogicdev/project-delta-pen/blob/main/docs/design_blueprint.md

We believe this concept represents a significant leap forward in automated/semi-automated TIG ergonomics. We would be eager to share our CAD files, engineering parameters, and prototype performance data with your engineering team, or set up a brief technical call to discuss potential collaboration.

Sincerely,
ForgedLogic
```
