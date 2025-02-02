import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# -------------------------------
# Load Data from MIMIC Demo Files
# -------------------------------
# Using the demo files: PATIENTS.csv, ADMISSIONS.csv, DIAGNOSES_ICD.csv
patients = pd.read_csv("PATIENTS.csv")
admissions = pd.read_csv("ADMISSIONS.csv")
diagnoses = pd.read_csv("DIAGNOSES_ICD.csv")

# Normalize column names to uppercase so that our references (e.g., "ADMITTIME") match
patients.columns = patients.columns.str.upper()
admissions.columns = admissions.columns.str.upper()
diagnoses.columns = diagnoses.columns.str.upper()

# -------------------------------
# Preprocess Data
# -------------------------------
# Convert date columns in ADMISSIONS to datetime objects
admissions['ADMITTIME'] = pd.to_datetime(admissions['ADMITTIME'])
admissions['DISCHTIME'] = pd.to_datetime(admissions['DISCHTIME'])

# Merge PATIENTS and ADMISSIONS on SUBJECT_ID to compute age at admission
merged = admissions.merge(patients, on='SUBJECT_ID', how='inner')

# Compute age at admission (Note: this simplistic calculation subtracts birth year from admission year)
merged['age'] = merged['ADMITTIME'].dt.year - pd.to_datetime(merged['DOB']).dt.year

# -------------------------------
# Figure 1: Patient Age Distribution at Admission
# -------------------------------
plt.figure(figsize=(8, 6))
sns.histplot(merged['age'], bins=20, kde=True, color="skyblue")
plt.title("Patient Age Distribution at Admission")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("figure1_age_distribution.png")
plt.show()

# -------------------------------
# Figure 2: Patient Gender Distribution
# -------------------------------
plt.figure(figsize=(6, 6))
gender_counts = patients['GENDER'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%',
        startangle=140, colors=sns.color_palette("pastel"))
plt.title("Patient Gender Distribution")
plt.savefig("figure2_gender_distribution.png")
plt.show()

# -------------------------------
# Figure 3: Admissions per Year
# -------------------------------
# Extract the year from ADMITTIME
admissions['ADMISSION_YEAR'] = admissions['ADMITTIME'].dt.year
admission_counts = admissions.groupby('ADMISSION_YEAR').size()

plt.figure(figsize=(10, 6))
admission_counts.plot(kind='line', marker='o', color="coral")
plt.title("Number of Admissions per Year")
plt.xlabel("Year")
plt.ylabel("Admissions Count")
plt.savefig("figure3_admissions_per_year.png")
plt.show()

# -------------------------------
# Figure 4: Top 10 ICD-9 Diagnoses Codes
# -------------------------------
top10_icd = diagnoses['ICD9_CODE'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top10_icd.index, y=top10_icd.values, palette="viridis")
plt.title("Top 10 ICD-9 Diagnoses Codes")
plt.xlabel("ICD-9 Code")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.savefig("figure4_top10_icd_codes.png")
plt.show()

# -------------------------------
# Figure 5: Length of Stay (LOS) by Outcome
# -------------------------------
# Calculate Length of Stay (in hours) from the difference between DISCHTIME and ADMITTIME
admissions['LOS'] = (admissions['DISCHTIME'] - admissions['ADMITTIME']).dt.total_seconds() / 3600

plt.figure(figsize=(10, 6))
sns.boxplot(x='HOSPITAL_EXPIRE_FLAG', y='LOS', data=admissions, palette="Set2")
plt.title("Length of Stay (Hours) by Outcome")
plt.xlabel("Hospital Expire Flag (0 = Alive, 1 = Expired)")
plt.ylabel("Length of Stay (Hours)")
plt.savefig("figure5_length_of_stay.png")
plt.show()
