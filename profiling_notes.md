# Profiling Notes – Customer Churn Dataset

## Dataset Shape
- Rows: 7043
- Columns: 21

## Column Info
- 18 columns are categorical (object)
- 2 columns are integer (`SeniorCitizen`, `tenure`)
- 1 column is float (`MonthlyCharges`)
- `TotalCharges` is stored as object but should be numeric

## Missing Values
- No missing values in any column

## Duplicates
- No duplicate rows found

## Basic Statistics
- **SeniorCitizen:** Mostly 0 (non-senior), only ~16% are senior citizens
- **tenure:** Ranges from 0 to 72 months, average ~32 months
- **MonthlyCharges:** Ranges from 18.25 to 118.75, average ~64.76
