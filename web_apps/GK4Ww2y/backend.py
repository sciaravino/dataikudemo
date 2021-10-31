import dataiku
import pandas as pd
from flask import request

# Call the dataset from the Flow
mydataset = dataiku.Dataset("website_topn")

# Load dataframe
df = mydataset.get_dataframe()

# Group df by ip_country, aggregated by sum of pages visited and average of prediction
df = df.groupby("education").reset_index()

# Print statement available in the "Log" tab
print(df)

@app.route('/send_data')
def send_data():
    # Pandas dataframes are not directly JSON serializable, use to_json()
    data = df.to_json(orient="records")
    return json.dumps({"status": "ok", "dataset": data})
