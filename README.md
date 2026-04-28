# Interactive IT GRC Compliance Dashboard

## Project Overview
This project demonstrates the automation of compliance reporting using Python and Plotly. Instead of static spreadsheets, this dashboard provides an interactive view of control maturity across key NIST 800-53 domains.

## GRC Skills Demonstrated
*   **Data-Driven Reporting:** Transforming raw audit data into board-ready visualizations.
*   **Security Control Mapping:** Visualizing maturity levels for Access Control, IR, and MFA.
*   **Automation:** Using Python to generate reproducible compliance snapshots.

## 📋 Control Mapping (NIST 800-53 Rev. 5)
The dashboard tracks maturity levels for the following critical control families:


| Dashboard Metric | NIST Family | Control Examples | Why it Matters |
| :--- | :--- | :--- | :--- |
| **Access Control** | AC | AC-2 (Account Mgmt), AC-3 (Access Enforcement) | Prevents unauthorized system entry. |
| **Audit/Log** | AU | AU-2 (Event Logging), AU-6 (Audit Review) | Provides the "trail" needed for incident forensics. |
| **IR Plan** | IR | IR-4 (Incident Handling), IR-8 (Incident Response Plan) | Ensures the org can react to a breach effectively. |
| **Risk Assessment** | RA | RA-3 (Risk Assessment), RA-5 (Vulnerability Monitoring) | Identifies where the "crown jewels" are vulnerable. |
| **MFA** | IA | IA-2 (Identification & Authentication) | The strongest defense against credential theft. |

## How to View
The live interactive dashboard can be found here: https://github.com/spardman/grc-dashboard


---
## 🔗 Connected GRC Modules
This dashboard visualizes the maturity of controls designed to mitigate the risks documented in my:
*   [**IT Risk Register**](https://github.com) 

