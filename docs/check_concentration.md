# 04_check_concentration

## Considerations for Continuous Discharges (Short Interval Discharges)
If a subsequent discharge begins before the hydrogen particles trapped within the metal membrane (from the previous discharge) are fully released, the calculation must account for the initial permeation flux and the hydrogen concentration within the membrane at the start of the discharge.
*(Note: Current calibration assumes an offset where \(t=0\).)*

![画像のタイトル](images/shot_170112.png)

### 1. Estimation of Recombination Coefficient (\(k_u\))
It is necessary to account for the permeation flux at the onset of the discharge (\(t=0\)).
If \(k_u\) is estimated using the default \(t=0\) offset (ignoring residual flux), the fitting curve will not accurately represent the physical behavior.

### 2. Inverse Calculation for Incident Flux (Not included in this project)
To calculate the incident flux from the permeation data, both the initial permeation flux and the initial hydrogen concentration within the metal membrane must be considered.