# Sales-Discount-Optimization
A machine learning-based Sales Optimization system built with Streamlit that identifies new or returning customers, applies automated discounts, and saves every transaction for future analysis.

# 📈 Sales Optimization System (Machine Learning + Streamlit)

A smart Sales Optimization Application that helps businesses analyze customer behavior, apply dynamic discounts, and store transaction history.  
This system improves customer retention, boosts sales, and automates discount decisions using Machine Learning models.

---

## ✅ Features

✅ Detects new vs existing customers  
✅ New customers get 10% discount on their first purchase  
✅ Existing customers get dynamic ML-based discount  
✅ Customer segmentation using Clustering (K-Means)  
✅ Automatic transaction saving (no duplicates)  
✅ Clean, fast, Streamlit UI  
✅ Ready for deployment and future model retraining

---

## 🧠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| UI | Streamlit |
| Data | Pandas, NumPy |
| Machine Learning | Scikit-Learn, Joblib |
| Storage | CSV / Excel / DB |

---

## 🏗 Project Structure


📂 Sales-Optimization
├── 📁 data
│ ├── customers.csv
│ └── transactions.csv
├── 📁 models
│ └── clustering_model.joblib
├── 📁 src
│ ├── app.py # Streamlit app
│ ├── utils.py # Helper/logic functions
│ └── train_model.py # Model training script
├── requirements.txt
└── README.md

PREVIEW

<img width="1288" height="622" alt="Screenshot 2025-11-10 123409" src="https://github.com/user-attachments/assets/2f856d88-9e85-48ca-82e4-c6a00fc86206" />

<img width="1165" height="422" alt="Screenshot 2025-11-10 123518" src="https://github.com/user-attachments/assets/a40d5a0a-da8d-4f79-ab19-270202a4f69e" />

<img width="1112" height="472" alt="Screenshot 2025-11-10 123541" src="https://github.com/user-attachments/assets/2faa9baa-f29e-4aa2-a09b-efa081ac1466" />

<img width="999" height="620" alt="Screenshot 2025-11-10 123637" src="https://github.com/user-attachments/assets/731feddb-1907-4256-9053-ed5381e8c04a" />

<img width="944" height="616" alt="Screenshot 2025-11-10 123659" src="https://github.com/user-attachments/assets/7cbbca63-9989-41a4-8239-6f770b1e63d4" />

<img width="937" height="526" alt="Screenshot 2025-11-10 124441" src="https://github.com/user-attachments/assets/0593dc0e-57d6-4d68-8c52-3d3e5db9f36c" />




---

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/sales-optimization.git
cd sales-optimization

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run src/app.py


🚀 How It Works
User enters: Name, Phone Number, City, Amount, etc.

System checks if the customer is new or returning

Discounts:

🆕 New Customer → 10% first-time discount

🔁 Existing Customer → ML-based discount using clustering

Final bill with discount is displayed

Transaction is saved to database (CSV)

Data improves model accuracy over time

📊 Output
Discounted bill

Customer category (New / Returning / Cluster Group)

Updated transaction history

Can be exported for real business use

<img width="1288" height="622" alt="Screenshot 2025-11-10 123409" src="https://github.com/user-attachments/assets/2f856d88-9e85-48ca-82e4-c6a00fc86206" />

<img width="1165" height="422" alt="Screenshot 2025-11-10 123518" src="https://github.com/user-attachments/assets/a40d5a0a-da8d-4f79-ab19-270202a4f69e" />

<img width="1112" height="472" alt="Screenshot 2025-11-10 123541" src="https://github.com/user-attachments/assets/2faa9baa-f29e-4aa2-a09b-efa081ac1466" />

<img width="999" height="620" alt="Screenshot 2025-11-10 123637" src="https://github.com/user-attachments/assets/731feddb-1907-4256-9053-ed5381e8c04a" />

<img width="944" height="616" alt="Screenshot 2025-11-10 123659" src="https://github.com/user-attachments/assets/7cbbca63-9989-41a4-8239-6f770b1e63d4" />

<img width="937" height="526" alt="Screenshot 2025-11-10 124441" src="https://github.com/user-attachments/assets/0593dc0e-57d6-4d68-8c52-3d3e5db9f36c" />


🚀 Future Enhancements
✅ Customer dashboard with analytics
✅ SMS / Email invoice system
✅ Cloud deployment (AWS / Render / Azure)
✅ Product recommendation engine
✅ Multi-branch sales tracking


📌 Requirements
txt
Copy code
streamlit
pandas
numpy
scikit-learn
joblib

🧑‍💻 Author
Your Name
GitHub: https://github.com/bharathmaruthi2010
Email: bharathmaruthi2010@gmail.com

⭐ If this project helps you, please give it a star on GitHub!
yaml


---

✅ This version is professional, clean, and recruiter-friendly  
✅ You can paste it directly into `README.md` on GitHub  

If you share your **name, email, and GitHub username**, I will personalize the final section for you.




