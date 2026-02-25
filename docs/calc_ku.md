# 05_calc_ku

## Overview

The recombination coefficient (\(k_u\)) on the plasma-facing surface of the metal membrane is estimated by fitting an analytical solution to the decay behavior of the permeation flux after the discharge ends.

## Analytical Model

The decay behavior of the permeation flux is modeled using the following analytical solution:

\[
J(t) = J_f \left( \frac{A(t) - 1}{A(t) + 1} \right)^2
\]

Where \(A(t)\) is defined as:

\[
A(t) = \frac{1 + \sqrt{J_i / J_f}}{1 - \sqrt{J_i / J_f}} \exp(\lambda t)
\]

And the decay constant \(\lambda\) is given by:

\[
\lambda = \frac{2(k_u + k_d) \sqrt{J_f}}{\sqrt{k_d} L}
\]

The initial condition at the end of the discharge (\(t=0\)) is:

\[
J(0) = J_i
\]

### Parameter Definitions:
- **\(J_i\)**: Permeation flux at the onset of the fitting
- **\(J_f\)**: Final steady-state permeation flux (background level)
- **\(k_u\)**: Recombination coefficient on the upstream (plasma-facing) side
- **\(k_d\)**: Recombination coefficient on the downstream side
- **\(L\)**: Thickness of the metal membrane

### References

I. Takagi, et al., J. Nucl. Mater. **258-263**, 1082-1086 (1998). 

## Analysis of "Kink" Behavior in Decay Curves

In short-duration discharges, a distinct **kink** is observed in the decay signal. 

To account for this behavior in discharges **#34313–#34320**, we performed separate fits for the regions before and after the kink.
