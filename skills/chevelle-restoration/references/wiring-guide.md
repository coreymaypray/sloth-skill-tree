# 1972 Chevelle SS Wiring & Electrical Guide

Connector identification, wire color codes, and harness routing for the Hi-Tech Classics SS dash conversion and full interior wiring.

## Table of Contents
1. [Harness Overview](#harness-overview)
2. [Bulkhead Connector](#bulkhead-connector)
3. [Dash Harness Connections](#dash-harness-connections)
4. [Gauge Connections](#gauge-connections)
5. [Lighting Circuits](#lighting-circuits)
6. [Accessory Wiring](#accessory-wiring)
7. [Wire Color Code Chart](#wire-color-code-chart)
8. [Grounding Points](#grounding-points)
9. [Troubleshooting](#troubleshooting)

---

## Harness Overview

The 1972 Chevelle uses 3 main harness sections:

1. **Engine/Front Light Harness**: Headlights, markers, horn, engine sensors → connects through bulkhead
2. **Dash Harness** (replaced by Hi-Tech SS harness): Gauges, ignition switch, fuse box, dash lights, radio, heater → connects at bulkhead and to rear harness
3. **Rear Body Harness**: Tail lights, backup lights, fuel sender, dome light, trunk light

### Critical Rule
The Hi-Tech Classics SS dash harness includes its own **integrated fuse box**. This replaces the factory fuse box entirely. Route the new harness through the same paths as the original.

### Year-Specific Warning
- 1970-1971 Chevelle wiring is similar but NOT identical to 1972
- 1972 introduced changes for emissions and ignition
- Bulkhead connector pin assignments vary by year AND factory options
- Always match connectors to YOUR year. Do not use a 70/71 diagram for a 72.

---

## Bulkhead Connector

The bulkhead connector passes through the firewall, connecting the engine harness to the dash harness. It's a large multi-pin rectangular connector.

### Location
- Firewall, driver's side, approximately 6" left of center
- Accessible from both engine bay and under-dash

### Inspection Before Connecting
1. Check for corroded pins — clean with electrical contact cleaner
2. Check for melted or burned terminals (especially power feeds)
3. Verify rubber grommet/seal is intact (prevents water intrusion)
4. If pins are damaged, replace the connector — do NOT solder-patch bulkhead connectors

### Connection
- Aligns with a keyed slot — can only go in one way
- Push firmly until the retaining clip snaps
- Tug-test to verify locked
- Apply dielectric grease to exterior of connector to prevent corrosion

---

## Dash Harness Connections

The Hi-Tech SS dash harness connects to the following, roughly from left to right behind the dash:

### Driver's Side (Left)
1. **Headlight switch**: Large round connector, 3 terminals + internal circuit breaker
2. **Dimmer switch feed**: From headlight switch to floor dimmer
3. **Turn signal switch**: Multi-pin connector at column
4. **Ignition switch**: Large connector at column, key-switched power
5. **Wiper switch**: 2-3 wire connector at column or dash

### Center
6. **Fuse box** (integrated in Hi-Tech harness): Mounts to driver's side kick panel area or under-dash bracket
7. **Heater/AC controls**: 2-4 wire connector for blower switch
8. **Radio power**: Single power feed + speaker wires
9. **Instrument voltage regulator**: If applicable (some Hi-Tech kits have internal regulation)

### Passenger Side (Right)
10. **Glove box light**: Single wire + ground
11. **Courtesy light feed**: Ties to door jamb switches

### Rear Harness Connection
12. **Rear harness plug**: Located behind center of dash, connects to rear body harness for tail lights, fuel sender, dome light, backup lights

---

## Gauge Connections

### Hi-Tech Classics SS Gauge Cluster

Each gauge in the Hi-Tech kit connects to the harness via individual or grouped connectors:

| Gauge | Signal Wire | Sender/Source | Notes |
|-------|-------------|---------------|-------|
| Tachometer | Tach signal (white) | Ignition coil (-) terminal | Connect to coil negative |
| Speedometer | Speed signal | Mechanical cable from trans | Cable drive, not electrical |
| Temperature | Temp sender (dark green) | Engine block sender | Single wire, grounds through block |
| Fuel Level | Fuel sender (dark blue/pink) | Tank sending unit | Verify sender ohm range matches gauge |
| Ammeter | Battery/alternator | In-line with charge wire | Carries full charging current |
| Clock | 12V constant | Fuse box | Constant power (not ignition-switched) |

### Sender Compatibility Warning
The Hi-Tech gauges may require specific ohm-range senders. GM used 0-90 ohm senders for fuel (empty-full). If the gauge reads backwards, the sender range is inverted. Verify before installation.

### Tachometer Connection
- Connect the tach signal wire to the **negative (-) terminal** of the ignition coil
- Do NOT connect to the positive terminal
- For HEI ignition: Connect to the TACH terminal on the HEI distributor cap

---

## Lighting Circuits

### Dash Illumination
- 10 bulbs included in Hi-Tech kit
- Twist-lock sockets: Insert, rotate 1/4 turn clockwise
- Controlled by headlight switch rheostat (dimmer knob)
- Bulb types: #194 (indicators), #1895 (gauge backlighting)

### Indicator Lights
| Indicator | Color | Triggered By |
|-----------|-------|-------------|
| Turn signals | Green (L/R) | Turn signal switch |
| High beam | Blue | Dimmer switch |
| Oil pressure | Red | Oil pressure sender |
| Gen/Alt | Red | Alternator |
| Brake | Red | Brake fluid switch / parking brake |

### Courtesy / Dome Lights
- Door jamb switches ground the circuit when door opens
- If dome light doesn't work: Check door jamb switch ground, then trace wire to harness

---

## Accessory Wiring

### Stereo / Head Unit (Aftermarket)
| Wire | Source | Notes |
|------|--------|-------|
| 12V Constant (Yellow) | Fuse box, battery-hot fuse | Memory/presets |
| 12V Ignition (Red) | Fuse box, ignition-hot fuse | On/off with key |
| Ground (Black) | Chassis bolt behind dash | Clean, bare metal |
| Illumination (Orange) | Headlight switch dimmer circuit | Dims with dash lights |
| Speakers | Run new wire to each location | 16-18 gauge minimum |

### Power Windows (If Equipped)
- Separate harness from door to body through rubber boot in door jamb
- Window switch connectors: Reversible polarity type (up/down)

### Cigarette Lighter / Power Outlet
- Constant 12V through its own fuse
- Heavy gauge wire (12-14 AWG) due to current draw

---

## Wire Color Code Chart

Standard GM color codes used in 1972 Chevelle:

| Color | Circuit |
|-------|---------|
| Red | Battery / starter feed |
| Pink | Ignition-switched power (from ignition switch) |
| Orange | Battery feed (to fuse box, always hot) |
| Brown | Tail lights / marker lights |
| Dark Green | Temperature sender |
| Light Green | Fuel sender / backup lights |
| Dark Blue | High beam indicator |
| Light Blue | Windshield wipers |
| Yellow | Left turn signal |
| White | Right turn signal / tach signal |
| Purple | Horn / fuel gauge |
| Black | Ground |
| Tan | Parking brake warning |
| Gray | Dome light / courtesy |

**Note**: Wire colors may have stripe variations (e.g., dark green with white stripe). Always verify against the factory wiring diagram for your specific car. GM color codes can vary between harness manufacturers.

---

## Grounding Points

Good grounds are the #1 cause of electrical gremlins in classic cars. Verify ALL of these:

| Ground Point | Location | Services |
|-------------|----------|----------|
| Battery negative | Engine block bolt | Primary ground |
| Engine to firewall | Braided strap, upper driver side | Engine accessories |
| Dash ground | Bolt to cowl/firewall, behind dash | All dash gauges, lights, radio |
| Body ground | Frame-to-body bolt, driver side | Tail lights, fuel sender |
| Headlight grounds | Inner fender bolts | Headlights, markers |

### Ground Maintenance
1. Remove each ground connection
2. Wire brush or sandpaper the contact area to bare, shiny metal
3. Apply a thin coat of dielectric grease (prevents future corrosion)
4. Re-bolt with star washer for bite into metal
5. Tug-test each ground

---

## Troubleshooting

### Gauges Don't Work
1. Check fuse box — verify correct fuse amp rating and that fuse is good
2. Check instrument voltage regulator (if applicable)
3. Verify dash ground connection
4. Test individual sender with multimeter (ohm reading)
5. Verify Hi-Tech harness connectors are fully seated

### No Dash Lights
1. Check headlight switch rheostat (turn inner knob)
2. Check bulbs — remove socket, inspect filament
3. Verify power at headlight switch connector
4. Check ground at dash

### Gauge Reads Wrong
- **Fuel gauge reads backwards**: Sender ohm range doesn't match gauge. Swap sender or verify wiring polarity.
- **Temp gauge pegged**: Sender wire grounded to block (reads hot). Disconnect sender wire — if gauge drops, sender or wire is grounded.
- **Ammeter fluctuates wildly**: Loose connection on charge wire. Check at alternator and at ammeter terminal.

### Turn Signals Don't Flash
1. Check flasher unit (round can behind dash)
2. Check bulbs — a burned-out bulb changes the circuit resistance
3. Verify turn signal switch connector is fully seated
4. Check grounds at front and rear light housings

### Dome Light Always On / Never On
- **Always on**: Door jamb switch stuck or grounded wire
- **Never on**: Bulb burned, or switch not making ground contact. Clean switch mounting hole to bare metal.
