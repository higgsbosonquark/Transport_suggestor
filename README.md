🚆 Transport Suggestor
Transport Suggestor is a Python-based command-line tool designed to assist users in selecting the most suitable mode of transportation—cab, train, or flight—between two locations. It evaluates options based on cost, duration, and availability using preloaded datasets.

📁 Project Structure
bash
Copy
Edit
.
├── main.py             # Main application script
├── requirements.txt    # List of Python dependencies
├── cab_data.csv        # Dataset containing cab fare information
├── train_data.csv      # Dataset containing train fare information
└── flight_data.csv     # Dataset containing flight fare information
⚙️ Features
Multi-Modal Comparison: Analyze and compare transportation options across cabs, trains, and flights.

Cost & Time Evaluation: Determine the most economical or fastest travel option based on user preference.

Data-Driven Insights: Utilize structured datasets to provide informed suggestions.

🛠️ Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/higgsbosonquark/Transport_suggestor.git
cd Transport_suggestor
Install Dependencies:

Ensure you have Python installed. Then, install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
Run the application using:

bash
Copy
Edit
python main.py
Follow the on-screen prompts to input your source and destination. The tool will then present you with the best transportation options based on your criteria.

📊 Datasets
The application relies on three CSV files:

cab_data.csv: Contains cab fare details between various locations.

train_data.csv: Contains train fare and duration details.

flight_data.csv: Contains flight fare and duration details.

Ensure these files are present in the project directory for the application to function correctly.

🛣️ Future Enhancements
Real-Time Data Integration: Incorporate live data from transportation APIs for up-to-date suggestions.

User Preferences: Allow users to set preferences like maximum budget, preferred travel time, etc.

Graphical User Interface (GUI): Develop a user-friendly interface for easier interaction.

🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

📄 License
This project is open-source and available under the MIT License.
