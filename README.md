# chanOpt
The repository for the Sabancı University graduation project: Product Reccomendation & Channel Optimization for Service Industries


This project is based on Kaggle's Santander Product Recommendation challange. We simulated a real life scenario where a bank brought in their 
data to us, seeking a new channel optimization engine. We took their data and explored it in Power BI, cleaned/enriched it on T-SQL and
built an ML model to predict probabilities of success for each customer/product matching in the following period. We used XGBoost as our model of choice.

Then, we took constraints from an IT company which works in a similar field and used Simplex Integer Programming to solve the maximization
problem for the best customer-channel-product combinations to be marketed, given their probabilities of success.
Plus, we wrapped the engine on a prototyped GUI.
