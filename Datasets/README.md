Dataset Cleaning and Preprocessing Workflow

The raw datasets underwent a structured multi-stage cleaning and preprocessing pipeline to ensure consistency, reliability, and suitability for downstream analysis.

1. Initial Manual Cleaning (Microsoft Excel)

Preliminary inspection and manual cleaning were performed in Microsoft Excel to address obvious formatting and structural inconsistencies, including:

Removal of duplicate records
Correction of inconsistent column naming conventions
Standardization of units and categorical labels
Identification of visually detectable anomalies

2. Column Restructuring Using Python

Several columns contained concatenated or improperly formatted values. These were processed programmatically using Python string manipulation functions such as split() to separate composite data fields into structured columns.

After restructuring:

Redundant intermediate columns were removed
Column formats were standardized
Data schema was aligned across all datasets

3. Data Consistency Validation (Power BI)

The cleaned datasets were imported into Power BI for exploratory validation and inconsistency detection.

This step helped identify:

Outlier distributions
Missing or irregular values
Logical inconsistencies across related variables
Unexpected data patterns requiring correction

4. Programmatic Error Correction Using Python

Based on inconsistencies detected during validation, appropriate Python preprocessing functions were applied, including:

Value normalization
String standardization
Data type conversion
Conditional replacement and correction rules

5. Missing Value Handling

Null, blank, and incomplete entries were handled using Python-based preprocessing techniques, depending on data context:

Removal of non-informative records
Replacement where appropriate
Filtering of invalid observations

6. Final Output

After completion of these preprocessing stages, the datasets were transformed into a clean, structured, and analysis-ready format suitable for:

Exploratory Data Analysis (EDA)
Statistical modeling
Machine Learning / Deep Learning model development
Visualization and reporting
Machine Learning / Deep Learning model development
Visualization and reporting
