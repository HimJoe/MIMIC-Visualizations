# MIMIC-Visualizations
This repository contains five visualizations built using the MIMIC III demo dataset. The project is designed to provide insights into patient data from electronic health records (EHR), including demographics, admission trends, diagnosis frequencies, and patient outcomes. The visualizations cover:

1. Patient Age Distribution at Admission:
   A histogram with a KDE overlay of patient ages at admission.

2. Patient Gender Distribution:
   A pie chart showing the distribution of genders in the dataset.

3. Admissions per Year:  
   A line plot of the number of admissions by year.

4. Top 10 ICD-9 Diagnoses Codes:  
   A bar chart displaying the most frequent ICD-9 codes.

5. Length of Stay by Outcome: 
   A box plot comparing the length of hospital stay for survivors versus non-survivors.

Files

- `mimic_visualizations.py`: Python code for generating the visualizations.
- `figures/`: Directory containing the generated PNG files.
- `slides/`: (Optional) Contains the slide deck presentation used to explain the visualizations.

How to Run

1. Ensure you have Python 3 installed with the required packages:
   - pandas
   - matplotlib
   - seaborn

2. Install the packages (if needed):

   ```bash
   pip install pandas matplotlib seaborn
