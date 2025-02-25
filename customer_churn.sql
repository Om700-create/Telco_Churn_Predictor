use traning;

-- Query 1: Identifying customers with the highest total charges
SELECT customerID, tenure, MonthlyCharges, TotalCharges, Contract, PaymentMethod, Churn 
FROM telco_customer_churn
ORDER BY TotalCharges DESC
LIMIT 20;

-- Observation:
-- The customers with the highest total charges tend to have longer tenures, with many exceeding 60 months.
-- Most of them are on One-year or Two-year contracts, suggesting that long-term contracts contribute to high total charges.
-- The most common payment methods are electronic check, bank transfer (automatic), and credit card (automatic).
-- All customers in this list have churned, meaning high-paying, long-term customers are still leaving, which is a concerning trend.

-- Query 2: Analyzing the average monthly charges and tenure for different payment methods
SELECT PaymentMethod, COUNT(*) AS CustomerCount, AVG(tenure) AS AvgTenure, AVG(MonthlyCharges) AS AvgMonthlyCharges
FROM telco_customer_churn
WHERE Churn = 'Yes'
GROUP BY PaymentMethod
ORDER BY AvgMonthlyCharges DESC;

-- Observation:
-- Customers using bank transfer (automatic) and credit card (automatic) have the highest average monthly charges.
-- Customers using electronic check have the highest churn rate but also a relatively high monthly charge.
-- Mailed check users have the lowest average monthly charges and the shortest tenure, meaning they might be low-value, short-term customers.

-- Query 3: Analyzing churn behavior across different tenure ranges
SELECT 
    CASE 
        WHEN tenure <= 12 THEN '0-12 months'
        WHEN tenure BETWEEN 13 AND 24 THEN '1-2 years'
        WHEN tenure BETWEEN 25 AND 48 THEN '2-4 years'
        WHEN tenure BETWEEN 49 AND 72 THEN '4-6 years'
    END AS TenureRange,
    COUNT(*) AS CustomerCount, 
    AVG(MonthlyCharges) AS AvgMonthlyCharges
FROM telco_customer_churn
WHERE Churn = 'Yes'
GROUP BY TenureRange
ORDER BY AvgMonthlyCharges DESC;

-- Observation:
-- Customers in the '4-6 years' tenure range have the highest average monthly charges but still experience churn.
-- The largest number of churned customers belong to the '0-12 months' range, indicating that new customers leave early.
-- The lowest churn occurs in the '2-4 years' category, possibly due to increased customer loyalty.

-- Query 4: Identifying top churned customers who paid via electronic check
SELECT customerID, tenure, MonthlyCharges, TotalCharges, Contract, PaymentMethod, Churn 
FROM telco_customer_churn
WHERE PaymentMethod = 'Electronic check' AND Churn = 'Yes'
ORDER BY TotalCharges DESC
LIMIT 20;

-- Observation:
-- Customers paying via electronic check seem to be at high risk of churn across all tenure groups.
-- The list contains both long-term and short-term customers, meaning the payment method could be a churn predictor.
-- Electronic check users might prefer flexibility and could switch providers more easily.

-- Query 5: Analyzing churn rate for different contract types
SELECT Contract, COUNT(*) AS CustomerCount, AVG(tenure) AS AvgTenure, AVG(MonthlyCharges) AS AvgMonthlyCharges
FROM telco_customer_churn
WHERE Churn = 'Yes'
GROUP BY Contract
ORDER BY AvgMonthlyCharges DESC;

-- Observation:
-- Month-to-month contract customers contribute the most to churn, with the shortest average tenure and relatively high monthly charges.
-- One-year and Two-year contract customers have a much lower churn rate, possibly due to binding agreements or loyalty benefits.
-- Customers on long-term contracts likely find it less convenient to switch providers, reducing churn.

-- Query 6: Identifying the highest-paying customers who churned
SELECT customerID, tenure, MonthlyCharges, TotalCharges, Contract, PaymentMethod, Churn 
FROM telco_customer_churn
WHERE Churn = 'Yes'
ORDER BY MonthlyCharges DESC
LIMIT 20;

-- Observation:
-- Customers with the highest monthly charges (above 100) tend to be on One-year or Two-year contracts.
-- Despite their high spending, they have still churned, raising concerns about dissatisfaction among premium users.
-- Further investigation into reasons for churn (customer complaints, service quality issues) is necessary.

-- Query 7: Analyzing the churn percentage by contract type
SELECT Contract, COUNT(*) AS TotalChurnedCustomers, 
       (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM telco_customer_churn WHERE Churn = 'Yes')) AS ChurnPercentage
FROM telco_customer_churn
WHERE Churn = 'Yes'
GROUP BY Contract
ORDER BY ChurnPercentage DESC;

-- Observation:
-- The majority of churned customers (88.55%) are on month-to-month contracts, highlighting the importance of contract type in retention.
-- One-year contracts contribute to 8.88% of churn, while Two-year contracts account for only 2.57%.
-- Incentivizing long-term contracts could be an effective strategy for reducing churn.

