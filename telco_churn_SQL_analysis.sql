use traning;

SELECT * 
FROM telco_customer_churn
LIMIT 5;

-- Observations:
-- 1. The dataset appears to have customer-related information, including IDs, demographics, services, contract details, and charges.
-- 2. The first column looks like a customer ID, which should be the primary key.
-- 3. There are categorical values like gender, internet service type, and payment method.
-- 4. There are numerical values such as tenure (likely months), monthly charges, and total charges.
-- 5. The last column seems to indicate churn status (Yes/No).
-- 
-- Next step: Let's inspect the column names and their data types to understand the schema.

DESC telco_customer_churn;

-- Observations:
-- 1. The `customerID` column is of type `text`, but it should ideally be a primary key.
-- 2. Most columns are `text`, which might need conversion if we plan on performing numerical analysis.
-- 3. `SeniorCitizen`, `tenure`, `MonthlyCharges`, and `TotalCharges` are numerical, but we need to check for inconsistencies (e.g., null values or incorrect data types).
-- 4. The `Churn` column is categorical (Yes/No), which will be useful for analysis.
-- 
-- Next step: Let's check for NULL or empty values in each column to ensure data consistency.
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN customerID IS NULL OR customerID = '' THEN 1 ELSE 0 END) AS customerID_nulls,
    SUM(CASE WHEN gender IS NULL OR gender = '' THEN 1 ELSE 0 END) AS gender_nulls,
    SUM(CASE WHEN SeniorCitizen IS NULL THEN 1 ELSE 0 END) AS SeniorCitizen_nulls,
    SUM(CASE WHEN Partner IS NULL OR Partner = '' THEN 1 ELSE 0 END) AS Partner_nulls,
    SUM(CASE WHEN Dependents IS NULL OR Dependents = '' THEN 1 ELSE 0 END) AS Dependents_nulls,
    SUM(CASE WHEN tenure IS NULL THEN 1 ELSE 0 END) AS tenure_nulls,
    SUM(CASE WHEN PhoneService IS NULL OR PhoneService = '' THEN 1 ELSE 0 END) AS PhoneService_nulls,
    SUM(CASE WHEN MultipleLines IS NULL OR MultipleLines = '' THEN 1 ELSE 0 END) AS MultipleLines_nulls,
    SUM(CASE WHEN InternetService IS NULL OR InternetService = '' THEN 1 ELSE 0 END) AS InternetService_nulls,
    SUM(CASE WHEN OnlineSecurity IS NULL OR OnlineSecurity = '' THEN 1 ELSE 0 END) AS OnlineSecurity_nulls,
    SUM(CASE WHEN OnlineBackup IS NULL OR OnlineBackup = '' THEN 1 ELSE 0 END) AS OnlineBackup_nulls,
    SUM(CASE WHEN DeviceProtection IS NULL OR DeviceProtection = '' THEN 1 ELSE 0 END) AS DeviceProtection_nulls,
    SUM(CASE WHEN TechSupport IS NULL OR TechSupport = '' THEN 1 ELSE 0 END) AS TechSupport_nulls,
    SUM(CASE WHEN StreamingTV IS NULL OR StreamingTV = '' THEN 1 ELSE 0 END) AS StreamingTV_nulls,
    SUM(CASE WHEN StreamingMovies IS NULL OR StreamingMovies = '' THEN 1 ELSE 0 END) AS StreamingMovies_nulls,
    SUM(CASE WHEN Contract IS NULL OR Contract = '' THEN 1 ELSE 0 END) AS Contract_nulls,
    SUM(CASE WHEN PaperlessBilling IS NULL OR PaperlessBilling = '' THEN 1 ELSE 0 END) AS PaperlessBilling_nulls,
    SUM(CASE WHEN PaymentMethod IS NULL OR PaymentMethod = '' THEN 1 ELSE 0 END) AS PaymentMethod_nulls,
    SUM(CASE WHEN MonthlyCharges IS NULL THEN 1 ELSE 0 END) AS MonthlyCharges_nulls,
    SUM(CASE WHEN TotalCharges IS NULL THEN 1 ELSE 0 END) AS TotalCharges_nulls,
    SUM(CASE WHEN Churn IS NULL OR Churn = '' THEN 1 ELSE 0 END) AS Churn_nulls
FROM telco_customer_churn;

-- Observations:
-- 1. The dataset contains 7,032 rows.
-- 2. There are no NULL or empty values in any column, which is good for analysis.
-- 3. Since `TotalCharges` is stored as a `double`, we should verify that all values are numeric (sometimes datasets store numbers as text).
-- 
-- Next step: Let's check for any non-numeric values in `TotalCharges`.

SELECT customerID, TotalCharges 
FROM telco_customer_churn 
WHERE NOT TotalCharges REGEXP '^[0-9]+(\.[0-9]+)?$';

-- Observations:
-- 1. All `TotalCharges` values are numeric, which means we can use this column for calculations without any issues.
-- 2. Since there are no missing or inconsistent values, we can proceed with exploratory data analysis.
-- 
-- Next step: Let's analyze the distribution of tenure, monthly charges, and total charges.
SELECT 
    MIN(tenure) AS min_tenure, 
    MAX(tenure) AS max_tenure, 
    AVG(tenure) AS avg_tenure, 
    MIN(MonthlyCharges) AS min_monthly, 
    MAX(MonthlyCharges) AS max_monthly, 
    AVG(MonthlyCharges) AS avg_monthly, 
    MIN(TotalCharges) AS min_total, 
    MAX(TotalCharges) AS max_total, 
    AVG(TotalCharges) AS avg_total
FROM telco_customer_churn;

-- Observations:
-- 1. The tenure ranges from 1 to 72 months, meaning the dataset includes customers from their first month to six years.
-- 2. Monthly charges range from $18.25 to $118.75, with an average of $64.80.
-- 3. Total charges range from $18.80 to $8,684.80, with an average of $2,283.30.
-- 4. There seems to be a logical relationship between tenure, monthly charges, and total charges, which we can explore further.
-- 
-- Next step: Let's analyze the churn rate in the dataset.
SELECT 
    Churn, 
    COUNT(*) AS count, 
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM telco_customer_churn), 2) AS percentage
FROM telco_customer_churn
GROUP BY Churn;

-- Observations:
-- 1. The dataset shows that **73.42%** of customers did not churn, while **26.58%** of customers churned.
-- 2. The dataset is imbalanced, as the number of customers who did not churn is significantly higher than those who did.
-- 3. This imbalance is common in churn datasets and might affect predictive models later if not handled properly.
-- 
-- Next step: Let's analyze the distribution of churn based on gender, senior citizen status, and partner status to understand if these demographics impact churn.
SELECT 
    gender,
    SeniorCitizen,
    Partner,
    Churn,
    COUNT(*) AS count
FROM telco_customer_churn
GROUP BY gender, SeniorCitizen, Partner, Churn
ORDER BY Churn DESC, count DESC;

-- Observations:
-- 1. Gender does not seem to have a strong influence on churn since both males and females have similar churn counts.
-- 2. Senior citizens have a higher churn rate compared to non-senior citizens, indicating they might be more likely to leave the service.
-- 3. Customers with partners tend to churn less compared to those without partners. This suggests that relationship status could influence customer retention.
-- 4. The highest churn occurs among non-senior customers without partners, meaning they might be more price-sensitive or less loyal.
-- 
-- Next step: Let's analyze churn based on contract type, as contract length often impacts churn behavior.
SELECT 
    Contract,
    Churn,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Contract), 2) AS churn_rate
FROM telco_customer_churn
GROUP BY Contract, Churn
ORDER BY Contract, Churn DESC;


-- Observations:
-- 1. Churn is **highest among month-to-month contracts (42.71%)**, meaning customers without long-term commitments are more likely to leave.
-- 2. **One-year contract customers have a much lower churn rate (11.28%)**, suggesting they are more stable.
-- 3. **Two-year contract customers have the lowest churn rate (2.85%)**, showing strong retention.
-- 4. This indicates that longer contract terms significantly reduce churn, possibly due to customer commitment or incentives.
-- 
-- Next step: Let's analyze the impact of payment methods on churn, as auto-pay options might improve retention.

SELECT 
    PaymentMethod,
    Churn,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY PaymentMethod), 2) AS churn_rate
FROM telco_customer_churn
GROUP BY PaymentMethod, Churn
ORDER BY PaymentMethod, Churn DESC;

-- Observations:
-- 1. **Electronic check users have the highest churn rate (45.29%)**, which suggests these customers may be less committed or experience payment-related issues.
-- 2. **Automatic payment methods (bank transfer and credit card) have the lowest churn rates (16.73% and 15.25%)**, meaning customers using auto-pay are more likely to stay.
-- 3. **Mailed check users have a moderate churn rate (19.20%)**, indicating they are more stable than electronic check users but less so than auto-pay users.
-- 4. Encouraging electronic check users to switch to automatic payments could help reduce churn.
-- 
-- Next step: Let's analyze the impact of internet service type on churn.


SELECT 
    InternetService,
    Churn,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY InternetService), 2) AS churn_rate
FROM telco_customer_churn
GROUP BY InternetService, Churn
ORDER BY InternetService, Churn DESC;

-- Observations:
-- 1. **Fiber optic users have the highest churn rate (41.89%)**, suggesting that they might face issues like higher costs or service dissatisfaction.
-- 2. **DSL users have a much lower churn rate (19.00%)**, meaning they are more likely to stay.
-- 3. **Customers without internet service have the lowest churn rate (7.43%)**, possibly because they are using only phone services, which might have better retention.
-- 4. This indicates that fiber optic customers are more at risk of churning, and strategies should be implemented to improve their experience.
-- 
-- Next step: Let's analyze the impact of tenure on churn by grouping customers into tenure brackets.
SELECT 
    CASE 
        WHEN tenure BETWEEN 0 AND 12 THEN '0-12 months'
        WHEN tenure BETWEEN 13 AND 24 THEN '13-24 months'
        WHEN tenure BETWEEN 25 AND 36 THEN '25-36 months'
        WHEN tenure BETWEEN 37 AND 48 THEN '37-48 months'
        WHEN tenure BETWEEN 49 AND 60 THEN '49-60 months'
        ELSE '61+ months'
    END AS tenure_group,
    Churn,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY 
    CASE 
        WHEN tenure BETWEEN 0 AND 12 THEN '0-12 months'
        WHEN tenure BETWEEN 13 AND 24 THEN '13-24 months'
        WHEN tenure BETWEEN 25 AND 36 THEN '25-36 months'
        WHEN tenure BETWEEN 37 AND 48 THEN '37-48 months'
        WHEN tenure BETWEEN 49 AND 60 THEN '49-60 months'
        ELSE '61+ months'
    END), 2) AS churn_rate
FROM telco_customer_churn
GROUP BY tenure_group, Churn
ORDER BY tenure_group, Churn DESC;

-- Observations:
-- 1. **Churn is highest among customers with a tenure of 0-12 months (47.68%)**, indicating that new customers are most likely to leave.
-- 2. **As tenure increases, churn rate decreases**, showing that long-term customers are much more likely to stay.
-- 3. **Customers with 61+ months of tenure have the lowest churn rate (6.61%)**, meaning retention strategies should focus more on new customers.
-- 4. This suggests that improving the early customer experience (e.g., better onboarding, discounts, or personalized support) could help reduce churn.
-- 
-- Next step: Let's create a final aggregated table summarizing key metrics, which we can export for Power BI analysis.

SELECT 
    Churn,
    COUNT(*) AS total_customers,
    ROUND(AVG(tenure), 2) AS avg_tenure,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(AVG(TotalCharges), 2) AS avg_total_charges,
    SUM(CASE WHEN Contract = 'Month-to-month' THEN 1 ELSE 0 END) AS month_to_month_customers,
    SUM(CASE WHEN Contract = 'One year' THEN 1 ELSE 0 END) AS one_year_customers,
    SUM(CASE WHEN Contract = 'Two year' THEN 1 ELSE 0 END) AS two_year_customers,
    SUM(CASE WHEN PaymentMethod = 'Electronic check' THEN 1 ELSE 0 END) AS electronic_check_customers,
    SUM(CASE WHEN PaymentMethod IN ('Bank transfer (automatic)', 'Credit card (automatic)') THEN 1 ELSE 0 END) AS auto_pay_customers
FROM telco_customer_churn
GROUP BY Churn;


-- Final Observations:
-- 1. Customers who churn have a **much lower average tenure (17.98 months)** than those who stay (37.65 months), confirming that new customers are at higher risk of leaving.
-- 2. Churned customers pay **higher average monthly charges ($74.44)** compared to non-churned customers ($61.31), suggesting price sensitivity as a churn factor.
-- 3. The total charges for churned customers are significantly lower ($1,531.80) compared to retained customers ($2,555.34), reinforcing the impact of tenure.
-- 4. **Most churned customers (1,655 out of 1,869) have month-to-month contracts**, which aligns with earlier findings that shorter commitments lead to higher churn.
-- 5. **Electronic check is the most common payment method for churned customers (1,071 out of 1,869),** reinforcing that customers using this method are more likely to leave.
-- 6. **Customers with auto-pay (bank transfer or credit card) have a much lower churn rate (490 churned vs. 2,573 retained),** suggesting auto-pay improves retention.
-- 
-- Next step: Let's save the final table as a CSV file for Power BI.

CREATE TABLE final_telco_data AS
SELECT 
    customerID,
    gender,
    SeniorCitizen,
    Partner,
    Dependents,
    tenure,
    PhoneService,
    MultipleLines,
    InternetService,
    OnlineSecurity,
    OnlineBackup,
    DeviceProtection,
    TechSupport,
    StreamingTV,
    StreamingMovies,
    Contract,
    PaperlessBilling,
    PaymentMethod,
    MonthlyCharges,
    TotalCharges,
    Churn
FROM telco_customer_churn;

SHOW VARIABLES LIKE 'secure_file_priv';

SELECT * FROM final_telco_data
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/final_telco_data.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';

