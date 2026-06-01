# Data Dictionary - Customer Churn Dataset
## CustomerID
- **Data Type:** object
- **Meaning:** Unique identifier for each customer
- **Business Relevance:** Used to track customers, not useful for analysis

## Gender
- **Data Type:** object
- **Meaning:** Gender of the customer (Male/Female)
- **Business Relevance:** Can be used to analyze churn patterns by gender

## SeniorCitizen
- **Data Type:** int64
- **Meaning:** Indicates if the customer is a senior citizen (0 = No, 1 = Yes)
- **Business Relevance:** Helps analyze churn behavior among older customers

## Partner
- **Data Type:** object
- **Meaning:** Whether the customer has a partner (Yes/No)
- **Business Relevance:** Helps analyze churn patterns based on relationship status

## Dependents
- **Data Type:** object
- **Meaning:** Whether the customer has dependents (Yes/No)
- **Business Relevance:** Useful for understanding churn among customers with families

## Tenure
- **Data Type:** int64
- **Meaning:** Number of months the customer has stayed with the company
- **Business Relevance:** Key factor in churn analysis; longer tenure often means lower churn

## PhoneService
- **Data Type:** object
- **Meaning:** Whether the customer has a phone service (Yes/No)
- **Business Relevance:** Helps analyze churn based on service usage

## MultipleLines
- **Data Type:** object
-**Meaning:**Whether the customer has multiple phone lines
-**Business Relevance:**Indicates service complexity and potential satisfaction

## InternetService
- **Data Type:** object
- **Meaning:** Type of internet service (DSL, Fiber optic, No)
- **Business Relevance:** Important for churn analysis; service type may affect satisfaction

## OnlineSecurity
- **Data Type:** object
- **Meaning:** Whether the customer has online security add-on (Yes/No/No internet service)
- **Business Relevance:** Can show if extra services reduce churn

## OnlineBackup
- **Data Type:** object
- **Meaning:** Whether the customer has online backup add-on
- **Business Relevance:** Indicates value-added services that may influence retention

## DeviceProtection
- **Data Type:** object
- **Meaning:** Whether the customer has device protection add-on
- **Business Relevance:** May improve satisfaction and reduce churn

 ## TechSupport
- **Data Type:** object
- **Meaning:** Whether the customer has tech support add-on
- **Business Relevance:** Lack of support may increase churn

## StreamingTV
- **Data Type:** object
- **Meaning:** Whether the customer has streaming TV service
- **Business Relevance:** Entertainment services may affect retention

## StreamingMovies
- **Data Type:** object
- **Meaning:** Whether the customer has streaming movies service
- **Business Relevance:** Entertainment services may affect retention

## Contract
- **Data Type:** object
- **Meaning:** Type of contract (Month-to-month, One year, Two year)
- **Business Relevance:** Strong predictor of churn; longer contracts reduce churn

## PaperlessBilling
- **Data Type:** object
- **Meaning:** Whether the customer uses paperless billing (Yes/No)
- **Business Relevance:** May indicate digital adoption and convenience

## PaymentMethod
- **Data Type:** object
- **Meaning:** Customer’s payment method (Electronic check, Mailed check, Bank transfer, Credit card)
- **Business Relevance:** Payment flexibility can affect churn

## MonthlyCharges
- **Data Type:** float64
- **Meaning:** Amount charged to the customer monthly
- **Business Relevance:** High charges may increase churn risk

## TotalCharges
- **Data Type:** object (convert to numeric)
- **Meaning:** Total amount charged to the customer
- **Business Relevance:** Useful for lifetime value analysis

## Churn
- **Data Type:** object
- **Meaning:** Whether the customer left the company (Yes/No)
- **Business Relevance:** Target variable for churn prediction
