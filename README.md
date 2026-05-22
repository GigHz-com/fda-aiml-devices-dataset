# FDA AI/ML-Enabled Medical Device Authorizations Dataset (1995–2025)

[![DOI](https://zenodo.org/badge/1246157249.svg)](https://doi.org/10.5281/zenodo.20336151)

Cumulative dataset of all U.S. Food and Drug Administration (FDA) marketing authorizations for artificial-intelligence and machine-learning (AI/ML)-enabled medical devices recorded between September 29, 1995 and December 30, 2025 (n = 1,430).

This repository accompanies the manuscript:

> Golshani P, Joseph M. **Three Decades of FDA Authorizations of AI/ML-Enabled Medical Devices: Persistent Specialty Concentration and the Care-Delivery Gap (1995–2025).** *Cureus Journal of Medical Science.* 2026 (in press). Preprint: medRxiv. DOI: [10.64898/2026.05.08.26352766](https://doi.org/10.64898/2026.05.08.26352766)

## What's in this repository

| Path | Contents |
|------|----------|
| `data/fda_aiml_devices_1995_2025.csv` | The 1,430-row authorization dataset analyzed in the paper. Columns: Date of Final Decision, Submission Number, Device, Company, Panel (Lead), Primary Product Code. |
| `analysis/compute_panel_counts.py` | Reproduces Table/Figure 2 — counts and percentages of authorizations by FDA lead review panel. |
| `analysis/compute_manufacturer_concentration.py` | Reproduces Figure 4 — manufacturer concentration by authorization-count tier. |
| `analysis/compute_annual_cumulative.py` | Reproduces Figure 1 — annual and cumulative authorization counts. |
| `figures/` | The four figures from the manuscript at publication resolution. |
| `METHODS.md` | Plain-language description of how the dataset was assembled and analyzed. |
| `CITATION.cff` | Machine-readable citation file (used by GitHub's "Cite this repository" button and by Zenodo when archiving). |

## Data source

The underlying records were retrieved directly from the FDA's publicly maintained list of AI/ML-enabled medical devices:

> US Food and Drug Administration. *Artificial Intelligence and Machine Learning (AI/ML)-Enabled Medical Devices.* https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices

The FDA periodically updates the list as additional authorizations are recorded; the snapshot in this repository was retrieved through December 30, 2025 and is the version analyzed in the manuscript. The FDA list is itself a public record; this repository simply makes the specific version used in the paper available for verification and reuse.

## Reproducing the analysis

```bash
git clone https://github.com/GigHz-com/fda-aiml-devices-dataset.git
cd fda-aiml-devices-dataset
pip install pandas matplotlib
python analysis/compute_panel_counts.py
python analysis/compute_manufacturer_concentration.py
python analysis/compute_annual_cumulative.py
```

All scripts are pure Python 3.11+ and depend only on `pandas` and `matplotlib`.

## Related resources

A continuously updated, interactive version of this dataset — including discovery-based metadata not analyzed in the present paper (intended use, clinical setting, vendor categorization, etc.) — is maintained at [PhysicianAITools.com](https://physicianaitools.com). The version archived here is the static snapshot used in the published analysis and is what should be cited for replication purposes.

## License

The CSV dataset and analysis scripts are released under the [MIT License](LICENSE). The underlying device-authorization records are U.S. government public-domain data published by the FDA.

## Citation

If you use this dataset or repository in your work, please cite the accompanying manuscript and this repository. See `CITATION.cff` for the machine-readable form.

## Contact

Pouyan Golshani, MD — `signal@gighz.com`
