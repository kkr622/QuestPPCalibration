# 02_calc_pumping_time

The pumping delay of the permeation probe (\(\tau\)) and the conversion coefficient from ion current to permeation flux (\(a\)) are calculated using a hydrogen standard leak.

The permeation flux \(\Gamma_{pdp}\) is defined as:

\[
\Gamma_{pdp} = a \cdot \left( I - I_0 + \tau\frac{dI}{dt}\right)
\]

Where:

- **\(a\)**: Calibration coefficient to convert QMS current into particle flux for steady-state pressures (\(\tau\frac{dI}{dt} \ll I\))
- **\(\tau = \frac{V}{S}\)**: Effective pumping time
- **\(I\)**: Measured ion current
- **\(I_0\)**: Background current