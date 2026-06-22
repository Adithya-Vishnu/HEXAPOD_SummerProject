# 🦿 HEXAPOD — IITK Robotics Club Summer Project 2025

[![Arduino](https://img.shields.io/badge/Arduino-00979D?style=flat&logo=arduino&logoColor=white)](Codes)
[![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white)](Codes)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](Codes)
[![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=flat&logo=mathworks&logoColor=white)](Codes)
[![Teensy 4.1](https://img.shields.io/badge/MCU-Teensy%204.1-orange)](Codes/Teensy_code.ino)
[![Status](https://img.shields.io/badge/status-active%20development-brightgreen)](#-future-work)

A from-scratch **18-DOF, six-legged walking robot** — custom CAD, inverse/forward kinematics, Euler-Lagrange dynamics, gait generation, and a Teensy 4.1-driven control stack, built end-to-end over Summer 2025 under the **Robotics Club, IIT Kanpur**.

<p align="center">
  <i>Six legs · three joints each · one base · zero off-the-shelf kits.</i>
</p>

---

## 📌 Overview

Hexapod robots trade the simplicity of wheels for the ability to walk over rubble, gaps, and uneven ground — at the cost of having to solve 18 coupled joint angles in real time just to take a step. This project builds that stack from the ground up:

- **Mechanical** — a hexagonal, circularly-symmetric chassis with slide-in, swappable legs
- **Kinematics** — closed-form inverse kinematics per leg, derived and verified in Python
- **Dynamics** — joint torques derived symbolically via the Euler-Lagrange method (SymPy)
- **Control** — three control-architecture iterations, ending on a single Teensy 4.1 driving all 18 servos directly
- **Locomotion** — wave, ripple, and tripod gaits, simulated in MATLAB before deployment
- **Interface** — manual RC joystick control mapped to omnidirectional leg-sector navigation

Full technical writeup: **[`Hexapod_Documentation.pdf`](./Hexapod_Documentation.pdf)** · Final review deck: **[`End-Eval_Presentation.pdf`](./End-Eval_Presentation.pdf)**

---

## ✨ Highlights

| | |
|---|---|
| **Degrees of Freedom** | 18 (6 legs × 3 DOF: coxa / femur / tibia) |
| **Base** | Hexagonal, legs at edge-midpoints for max clearance + load symmetry |
| **Leg joints** | Dual-bearing supported, slide-lock mounted, fully swappable |
| **Actuation** | 18 × DS5160 60 kg·cm metal-gear digital servos |
| **Controller** | Teensy 4.1 (600 MHz ARM Cortex-M7) — direct PWM, no multiplexing |
| **Power** | 2S1P 7.4V LiPo, 3300 mAh, 25C, XT60 |
| **Gaits** | Wave · Ripple · Tripod — all simulated in MATLAB |
| **Control input** | FlySky FS-i6 RC transmitter, atan2-based 6-sector direction mapping |

---

## 📂 Repository Structure

```
HEXAPOD_SummerProject/
├── CAD_Design/              # Fusion 360 source + STEP exports for every part
│   ├── Assembled bot.f3z        — full bot assembly
│   ├── Entire_BODY v4.f3z        — body/base iteration
│   ├── fixed_tibia.f3d           — tibia (cross-braced, lightweight)
│   ├── hexapod_coxa and slidder.step
│   ├── slider mount.step
│   └── Coxa servo motor.SLDPRT / .STEP
│
├── Codes/                   # Firmware, kinematics, and gait code
│   ├── Teensy_code.ino           — single-board 18-servo control (final arch.)
│   ├── 3_GAITS.ino               — wave / ripple / tripod gait state machine
│   ├── hexapod_ik_solution.py    — inverse kinematics solver per leg
│   ├── Forward kinematics.py     — FK verification against IK output
│   ├── Ripple.m.txt              — MATLAB ripple gait simulation
│   └── Code.cpp                  — leg-position / coordinate transform math
│
├── Entry tasks/              # Onboarding tasks completed before the main build
│   (DOF visualizations, early IK attempts, trig derivations)
│
├── Gcodes/                   # Sliced G-code for every 3D-printed part
│
├── timelapse/                 # Build-process videos, print timelapses
│
├── Hexapod_Documentation.pdf   # Full technical report (mechanical + electrical + control)
└── End-Eval_Presentation.pdf   # Final evaluation slide deck
```

---

## 🦾 Mechanical Design

- **Hexagonal base** chosen over circular for the same structural symmetry at lower material cost; legs sit at **edge midpoints** rather than corners for better clearance and base-leg contact area.
- Each leg **slides into the base** through interlocking stepped slots — this maximizes coxa-base contact area (the coxa sees the highest torque in the system) and lets a faulty leg be swapped without touching the rest of the bot.
- The **coxa-femur joint** went through a full redesign cycle: an initial plus-shaped cross-section concentrated stress at multiple points, so it was rebuilt as a solid cuboid with triangular extrusions sandwiched between **dual ball bearings** — countering the single-sided servo shaft and distributing rotational load evenly.
- The **femur** houses both its servos internally with a cross-shaped internal brace to resist bending under load; the **tibia** uses a cross-truss internal lattice to stay light without losing stiffness, with a stepped hinge angle for better load transfer when climbing.

---

## 🧮 Kinematics & Dynamics

Each leg is modeled as a 3-DOF serial manipulator (coxa → femur → tibia). Given a target foot position `(x, y, z)`, the inverse kinematics solves for joint angles:

```
α = atan2(y, x)                         # coxa (yaw)
r = √(x² + y²),  d = √(r² + z²)
γ = acos((a² + b² − d²) / 2ab)          # tibia (knee angle, law of cosines)
β = atan2(z, r) + acos((a² + d² − b²) / 2ad)   # femur (shoulder angle)
```

implemented and verified in [`hexapod_ik_solution.py`](./Codes/hexapod_ik_solution.py) with a forward-kinematics cross-check in [`Forward kinematics.py`](./Codes/Forward%20kinematics.py).

On top of this, joint **torques τ₁, τ₂, τ₃** were derived symbolically with the **Euler-Lagrange method** (kinetic + potential energy of the 3-link leg, differentiated via SymPy) — used to size the actuators and sanity-check the DS5160's torque margin under worst-case moment arm.

---

## ⚡ Control System Evolution

The control architecture went through three iterations before settling on the final design — each one solving a real failure mode of the last:

| # | Architecture | Why tried | Why dropped |
|---|---|---|---|
| 1 | Arduino Mega 2560 + dual PCA9685 | 32 PWM channels over I²C, minimal wiring | PCA9685 capped at 6V servo rail; bypassing it for 7.4V caused PWM cross-talk / erratic signals |
| 2 | Dual Arduino Mega 2560 (master-slave) | Splits 18-servo IK load across two boards | Sync drift between boards, wiring complexity, 8-bit clock ceiling for real-time IK |
| 3 | **Teensy 4.1** ✅ | 600 MHz Cortex-M7, 20+ PWM-capable pins | — final architecture, drives all 18 servos directly at 1 kHz |

**Actuators:** 18 × DS5160 servos (60 kg·cm @ 7.4V, full metal gear, dual ball bearing, ~0.16 s/60°)
**Power:** 7.4V–8.4V 2S1P LiPo, 3300 mAh, 25C continuous discharge, fused per rail
**Manual control:** FlySky FS-i6 + FS-iA6B receiver — joystick X/Y read as PWM pulse widths, converted to a heading via `atan2`, then mapped into 6 × 60° sectors, each assigned to a "lead leg" for omnidirectional driving without conflicting motion commands.

---

## 🚶 Gait Implementation

| Gait | Legs moving at once | Stability | Speed | Best for |
|---|---|---|---|---|
| **Wave** | 1 | Highest (5 always grounded) | Slowest | Rough/uneven terrain |
| **Ripple** | 1 (overlapping) | High | Moderate | Mixed terrain |
| **Tripod** | 3 | Good | Fastest | Flat ground — default gait |

All three were modeled and animated in MATLAB ([`Ripple.m.txt`](./Codes/Ripple.m.txt) and equivalents for wave/tripod) before being ported to the firmware gait state machine in [`3_GAITS.ino`](./Codes/3_GAITS.ino).

---

## 🚀 Getting Started

**Run the IK/FK solvers (Python):**
```bash
pip install numpy
python "Codes/hexapod_ik_solution.py"
python "Codes/Forward kinematics.py"
```

**Flash the firmware:**
1. Open [`Codes/Teensy_code.ino`](./Codes/Teensy_code.ino) in the Arduino IDE
2. Install the **Teensyduino** add-on and the `Servo` library
3. Select **Tools → Board → Teensy 4.1**, connect via USB, and upload
4. For gait testing on the Mega-based setup, use [`3_GAITS.ino`](./Codes/3_GAITS.ino) instead

**3D-print the parts:** sliced files are ready to go in [`Gcodes/`](./Gcodes); source CAD (Fusion 360 `.f3z`/`.f3d` + STEP) is in [`CAD_Design/`](./CAD_Design).

---

## 🔭 Future Work

- Rubber end-effector tips on the tibia for better terrain grip
- Environmental sealing for outdoor/field operation
- Onboard sensor fusion (IMU/distance) for autonomous, terrain-adaptive gait switching
- Migrating from RC manual control to fully autonomous path planning

---

## 👥 Team — Summer Project 2025, Robotics Club IIT Kanpur

**Mentors:** Kishor Kunal · Shivansh Gupta · Vivek Pawar

**Team:** Adithya Vishnu · Arnav Gupta · Ayush Dwivedi · Dibyanshu · Gungun Jain · Harsh Chandwani · Manant · Namya Mayur Jarag · Saket Pratap Singh · Shivam Agrawal · Subhankar Mondal · Suryans Kumar Verma · Swethaa · Vaibhav · Varshini Ridikka · Virendra Kala · Sameer Baranwal · Sandeep Kumar

---

<p align="center"><i>Built leg by leg, bug by bug. 🦿</i></p>
