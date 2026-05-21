# Methods

## Data source

The records in `data/fda_aiml_devices_1995_2025.csv` were retrieved from the U.S. Food and Drug Administration's publicly maintained list of AI/ML-enabled medical devices, available at:

https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices

The FDA list reports devices that have received marketing authorization through the 510(k), De Novo, or Premarket Approval (PMA) pathways and that the FDA has identified as containing AI/ML functionality. The dataset snapshot in this repository contains 1,430 authorizations with final-decision dates between September 29, 1995 and December 30, 2025.

## Variables

| Column | Description |
|--------|-------------|
| Date of Final Decision | FDA final-decision date for the authorization (MM/DD/YYYY). |
| Submission Number | FDA submission identifier. Numbers beginning with `K` indicate 510(k); `DEN` indicates De Novo; `P` indicates PMA. |
| Device | Trade name of the authorized device. |
| Company | Sponsor or manufacturer of record. |
| Panel (Lead) | FDA lead review panel (an FDA classification corresponding broadly to the medical specialty of intended use). |
| Primary Product Code | FDA product code assigned to the device. |

## Derived classifications

Regulatory pathway was derived from the prefix of the Submission Number column (`K` → 510(k); `DEN` → De Novo; `P` → PMA). Manufacturer-concentration tiers were derived by counting unique `Company` strings and binning each company by its authorization count: 1 device, 2–4 devices, 5–9 devices, and ≥10 devices.

## Analysis environment

Analyses in the manuscript were performed in Python 3.11 with pandas 2.x and matplotlib 3.x. All scripts in `analysis/` are reproducible from the CSV in `data/`.

## Notes

- The FDA list is updated irregularly as additional authorizations are recorded; the snapshot here is the version used in the published analysis and is fixed at the December 30, 2025 cutoff.
- The `Company` column treats each sponsor string as a unique entity and does not consolidate corporate parent–subsidiary relationships.
- The `Panel (Lead)` column reflects the FDA's regulatory classification and may not align exactly with clinical specialty of intended use.

For a continuously updated, interactive version of this dataset with additional discovery-based metadata, see [PhysicianAITools.com](https://physicianaitools.com). The version archived here is the static snapshot to cite for replication.
