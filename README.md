# Nike Backend Database Systems - Data Architecture & Analytics

## Project Overview
This project designs and implements the backend database infrastructure for **Nike**, a Fortune 500 company. The goal is to develop an integrated system that supports daily operations, decision-making, and a new business application.

### Key Components:
1. **Existing Systems:**  
   - RDBMS for structured data storage (MySQL)  
   - NoSQL databases for unstructured data (MongoDB, DynamoDB)  
   - Data warehouse for big data analytics (Hive)  
   - ETL pipelines for data integration  

2. **New Business Application:**  
   - A motivational platform that delivers personalized workout recommendations and quotes  
   - Backend powered by MySQL, MongoDB, and PySpark for real-time data processing  

3. **Decision-Making & Analytics:**  
   - Data Warehouse (Star Schema) in MySQL  
   - ETL processing for insights generation  
   - Visualization of key metrics for business strategy  

---

## 📌 Part 1: Design of Existing Systems  

### 🔹 Relational Database (OLTP - MySQL)
The **RDBMS** is responsible for structured data related to operations and transactions.  
**Key Tables:**
- `users`: Stores user profiles (Nike customers)  
- `vendors`: Details suppliers for Nike's supply chain  
- `employees`: Nike's workforce database  
- `stores`: Physical and online Nike store information  

📌 **Data Generation:**  
- Used **PySpark** and the **Faker library** to generate large datasets (1M+ records).  
- Saved data in **Parquet files** for batch processing.  
- Loaded into **AWS RDS (MySQL)** via the **MySQL connector**.  

### 🔹 NoSQL Databases  
- **MongoDB**: Stores **unstructured product & user preference data**.  
- **DynamoDB**: Handles **session management** for Nike's applications.  

📌 **Why NoSQL?**  
- **MongoDB** allows flexible schema for product metadata & fitness preferences.  
- **DynamoDB** ensures high-speed read/write for session handling.  

### 🔹 Data Warehouse (Hive)
- Stores historical data for **big data analytics**.  
- Designed for **querying & processing large-scale Nike operations data**.  

---

## 📌 Part 2: New Business Application  

### 🚀 **Nike Inspire - Personalized Motivational Hub**
A **new business application** that enhances Nike’s engagement by delivering **personalized motivational messages & workout recommendations** based on user preferences.
Unlike existing Nike platforms (Nike Run Club, Nike Training Club), this application prioritizes emotional engagement through personalized fitness inspiration.

### **🔹 Data Model**
- **User Data** (`users` table - MySQL)  
- **Activity Data** (MongoDB - daily workout logs)  
- **Preference Data** (MongoDB - fitness goals & notifications)  
- **Quotes Data** (`quotes` table - MySQL)  

### **🔹 Functionality**
1. Users register on the **front-end interface** which can be done through the normal registration   
2. System captures **fitness goals & activity logs** (e.g., running, yoga).  
3. **Personalized workout & motivational quotes** are sent via email/SMS.  

📌 **Tech Stack:**  
- **MySQL + MongoDB** for backend storage.  
- **Python Flask API** for front-end interaction.  
- **Email/SMS integration** for real-time engagement.  

---

## 📌 Part 3: Data Warehouse & Analytics  

### **🔹 ETL Pipeline**
- Extracts data from **MySQL, MongoDB, and DynamoDB**.  
- Transforms data using **PySpark**.  
- Loads into **MySQL Star Schema Data Warehouse**.  

### **🔹 Star Schema Design**
| Fact Table  | Dimension Tables |
|-------------|-----------------|
| `fact_activity` | `users`, `activities`, `fitness_goals`, `time` |

### **🔹 Insights for Decision-Making**
📊 **Key Business Insights:**
1. **User Activity Trends by Location**  
   - Identifies **high engagement regions** for targeted marketing.  
2. **Seasonal Fitness Trends**  
   - Helps in **planning product launches** and promotional events.  
3. **User Segmentation for Product Recommendations**  
   - Groups users based on **shopping preferences & fitness goals**.  
4. **Age-based Engagement Analysis**  
   - Provides **personalized promotions** based on demographics.  
5. **Peak Workout Hours**  
   - Optimizes **push notifications & reminders** for higher engagement.  
![image](https://github.com/user-attachments/assets/48517b63-8616-498b-8727-b43ac905de27)


### **🔹 Challenges & Considerations**
- **Data Integration:** Ensuring real-time sync between structured & unstructured data.  
- **Scalability:** Handling millions of users during high-traffic events.  
- **Security & Compliance:** Protecting sensitive data (GDPR, CCPA).  

---

## 📌 Technologies Used  
- **Databases:** MySQL, MongoDB, DynamoDB, Hive  
- **Data Processing:** PySpark, Faker Library  
- **Backend:** Python Flask  
- **ETL & Analytics:** MySQL Star Schema, Pandas, Seaborn  
- **Deployment:** AWS RDS, Docker  

---




## 📌 Conclusion  
This project provides **Nike** with a **scalable** and **data-driven infrastructure** that enables:
- **Seamless data management** across multiple databases.  
- **A new business application** for enhancing customer engagement.  
- **Data-driven insights** to optimize marketing and product strategies.  

🚀 **Future Enhancements:**  
- Expand AI-driven recommendations for workout plans.  
- Real-time data streaming for instant activity tracking.  
- Integration with Nike’s existing apps (Nike Run Club, Training Club). 

