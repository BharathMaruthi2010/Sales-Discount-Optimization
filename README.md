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

<img width="1288" height="622" alt="Screenshot 2025-11-10 123409" src="https://github.com/user-attachments/assets/cbea80f4-8ec4-4b99-a05f-9df03efee2fe" />


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




