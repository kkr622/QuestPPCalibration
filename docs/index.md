# quest-pp-calibration

This project focuses on the calibration of data from the permeation probes used in QUEST. It primarily includes the following:

- **Calculation of the pumping speed** of the permeation probe.
- **Conversion of QMS ion current** into permeation flux.
- **Calculation of the recombination coefficient (\(k_u\))** on the metal membrane surface.

## Examples
The `example` folder contains the calibration results for the permeation flux, based on the PP8 measurement data from discharges **#34313–#34320** on **January 12, 2017**.

| Shot number | Discharge duration | Fueling \( \text{H}_2 \) |
| :--- | :---: | :--- |
| #34313 | ~20 s | 5.0 ml/min (1 ~ 10s) <br> 2.8 ml/min (10 ~ 20s) |
| #34314 | ~20 s | 5.0 ml/min (1 ~ 10s) <br> 2.2 ml/min (10 ~ 20s) |
| #34315 | ~20 s | 2.0 ml/min (1 ~ 10s) |
| #34316 | ~60 s | 2.0 ml/min (1 ~ 10s) |
| #34317 | ~60 s | 2.0 ml/min (1 ~ 10s) <br> 1.2 ml/min (10 ~ 25s) <br> 0.2 ml/min (25 ~ 40s) |
| #34318 | ~60 s | 2.0 ml/min (1 ~ 10s) <br> 0.7 ml/min (10 ~ 25s) |
| #34319 | ~60 s | 2.0 ml/min (1 ~ 10s) <br> 0.8 ml/min (10 ~ 25s) |
| #34320 | ~300 s | 2.0 ml/min (1 ~ 10s) <br> 0.8 ml/min (10 ~ 25s) |

For details on the permeation probe used in this study, please refer to:

- A. Kuzmin, et al., Vacuum, **129**, 178-182 (2016).