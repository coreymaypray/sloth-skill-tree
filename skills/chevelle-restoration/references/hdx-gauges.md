# Dakota Digital HDX-70C-CVL Gauge System Reference

Complete reference for the Dakota Digital HDX gauge system as installed in Corey's 1972 Chevelle SS with Hi-Tech Classics dash kit.

## System Overview

The HDX-70C-CVL is a hybrid analog/digital gauge system designed as a direct fit for 1970-72 Chevelle SS dashes. It combines traditional analog needle sweeps with modern TFT displays and digital signal processing.

### What's In the Box
- HDX gauge cluster assembly (direct-fit for SS dash opening)
- HDX Control Box (brain unit, mounts behind dash)
- Oil pressure sender (SEN-01-5, 3-wire, 1/8" NPT)
- Water temperature sender (1/8" NPT with bushing adapters)
- Speed sensor/signal generator
- Wiring harness with labeled connectors
- Installation manual (#650572B)

## Control Box Installation

### Mounting Location
- Behind the dash, driver's side preferred
- Must be accessible for future service/updates
- Keep away from heater box and exhaust heat
- Secure with screws or zip ties to a solid bracket

### Power Wiring

| Wire Color | Connection | Specs | Notes |
|-----------|-----------|-------|-------|
| Red | Constant 12V (battery-hot) | 18 AWG min, fused 5-20A | Powers memory, clock, settings |
| Pink | Switched 12V (ignition-hot) | 18 AWG min | Powers gauges when key is ON |
| Black | Chassis ground | 18 AWG min | Clean bare metal, star washer |
| Orange/Dimmer | Headlight switch dimmer | Per harness | Controls backlight brightness |

### Power Wiring Tips
- Route constant 12V from a battery-hot fuse in the fuse box
- Route switched 12V from an ignition-hot fuse
- Ground to a dedicated bolt on the firewall or dash frame — NOT to a shared ground with other accessories
- Use a star washer and sand to bare metal at ground point

## Sensor Installation

### Oil Pressure Sender (SEN-01-5)
- **Type**: 3-wire electronic sender (NOT the old single-wire GM type)
- **Thread**: 1/8" NPT
- **Location**: Engine block, oil gallery port (where factory sender was)
- **Wiring**:
  - White wire = Signal (to Control Box)
  - Red wire = 5V DC power (from Control Box)
  - Black wire = Ground (to engine block or chassis)
- **Install notes**: Apply Teflon tape to threads. Do NOT over-tighten (hand-tight + 1/4 turn). Route wires away from exhaust manifold.

### Water Temperature Sender
- **Type**: 2-wire (signal + ground through block)
- **Thread**: 1/8" NPT (may need bushing adapter for GM intake manifold ports)
- **Location**: Intake manifold water jacket port
- **Wiring**: Single signal wire to Control Box; grounds through engine block
- **Install notes**: Use Teflon tape. Verify thread adapter fits — GM often uses 3/8" or 1/2" NPT ports, so a reducing bushing may be needed.

### Speed Sensor
- **Type**: 3-wire pulse generator
- **Options**:
  - Cable-drive adapter: Replaces mechanical speedo cable at transmission
  - Electronic: Mounts to transmission tailshaft or rear axle
- **Wiring**: Signal, power, and ground to Control Box
- **Calibration**: Required — enter tire size and axle ratio, or use GPS calibration mode

### Fuel Level Sender
- **Uses existing tank sending unit** — no new sender needed (usually)
- **Caveat**: GM 1972 uses 0-90 ohm range. The HDX system can calibrate to match any sender range.
- **Calibration**: Mark empty and full points through HDX menu (drive to empty, set point; fill up, set point)

### Tachometer Signal
- **Source**: Ignition coil negative (-) terminal
- **For HEI ignition**: Use the TACH terminal on the HEI distributor cap
- **Setup**: Set cylinder count in HDX menu (8 for 396/454 big block)

### Voltmeter
- **Internal**: Reads system voltage directly from the power connections
- **No external sender needed**

## Calibration Procedure

### Initial Setup (After First Power-On)
1. Turn ignition to ON (do not start engine)
2. Gauges will sweep through a self-test sequence
3. Use capacitive touch buttons on gauge face to enter setup menu
4. Alternatively, connect via Bluetooth and use Dakota Digital app

### Speedometer Calibration
**Option A — Manual Entry**:
1. Enter tire diameter (e.g., 26.5" for P235/60R15)
2. Enter rear axle ratio (e.g., 3.73:1)
3. Enter pulses per mile from speed sensor spec

**Option B — GPS Calibration**:
1. Enter GPS calibration mode in HDX menu
2. Drive at a steady speed on a straight road
3. System reads GPS speed vs. sensor pulses and auto-calibrates

### Fuel Gauge Calibration
1. Drive/drain tank until fuel light comes on or tank is near empty
2. Enter calibration mode, set "Empty" point
3. Fill tank completely
4. Set "Full" point
5. System interpolates all points between

### Tachometer Setup
1. Enter setup menu
2. Set engine cylinder count: **8**
3. Verify signal type matches your ignition (points, HEI, or aftermarket)

### Backlight Color
1. Enter color menu via touch buttons
2. Cycle through 30+ color options
3. Select preferred color
4. Can also be set via Bluetooth app

## Message Center Displays

The two TFT screens can show various readings. Configurable options include:
- Digital speedometer readout
- Odometer / trip odometer
- Voltage reading
- Oil pressure (digital)
- Water temperature (digital)
- Clock
- Gear indicator (if connected)
- And more depending on firmware version

## Troubleshooting

### No Power to Gauges
1. Check 5-20A fuse on constant 12V (red wire) circuit
2. Verify constant 12V at Control Box red wire with multimeter (should read 12.4V+)
3. Check ground connection — clean bare metal?
4. Check switched 12V (pink wire) — key must be ON

### Gauges Power On But No Readings
1. Verify ignition-switched power (pink wire) is live with key ON
2. Check each sensor connector at Control Box — fully seated?
3. Test individual sensors with multimeter

### Oil Pressure Reads Zero (Engine Running)
1. Confirm SEN-01-5 wiring: white=signal, red=5V, black=ground
2. Check sender is tight in block and Teflon-sealed
3. Swap sender with known-good unit to rule out bad sender
4. Check for pinched or cut wires in engine bay routing

### Speedometer Not Working
1. Verify speed sensor cable adapter is properly seated in trans tailshaft
2. Check 3-wire connection at Control Box
3. Re-run calibration (GPS method is most reliable)

### Fuel Gauge Reads Wrong
1. Re-calibrate empty/full points
2. Check signal wire from tank sender to Control Box (no splices, no grounds)
3. Verify tank sender ohm range with multimeter (disconnect wire, measure resistance at empty vs full)

### Backlight Dim or Flickering
1. Check dimmer wire connection to headlight switch rheostat
2. If dimmer wire is not connected, backlight defaults to full brightness
3. Check for loose connector at gauge cluster

### Bluetooth Won't Connect
1. Ensure ignition is ON (gauges powered)
2. Check that Bluetooth is enabled in HDX settings
3. Try forgetting the device on your phone and re-pairing
4. Update Dakota Digital app to latest version

## Official Resources

- **Installation Manual**: Dakota Digital Manual #650572B
- **PDF Download**: dakotadigital.com — search HDX-70C-CVL
- **Tech Support**: Dakota Digital phone support: (605) 332-6513
- **Firmware Updates**: Available through Dakota Digital — contact tech support
