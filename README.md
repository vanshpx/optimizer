🌍 Voyage – Trip Companion

Voyage is an AI-powered trip planning assistant that helps users create personalized travel itineraries based on their preferences, budget, and trip duration.
It simplifies the entire planning process by generating smart, structured, and easy-to-follow travel plans.

🚀 Problem Statement

Planning a trip is often:

Time-consuming

Confusing (multiple platforms for places, routes, budgets)

Not personalized

Users struggle to convert ideas like “3-day trip to Goa under ₹15k” into a clear day-wise plan.

💡 Our Solution

Voyage acts as a smart trip companion that:

Takes basic user inputs (destination, days, budget, preferences)

Uses AI to generate:

Day-wise itineraries

Place recommendations

Logical travel flow

Delivers everything in a single, clean response

✨ Key Features

🧠 AI-generated personalized itineraries

📅 Day-wise trip planning

📍 Smart place recommendations

💰 Budget-aware suggestions

⚡ Fast and easy to use

🛠️ Tech Stack

Backend: Python

AI / LLM: Large Language Model (LLM)

APIs: Google Places (for location data)

Data Handling: JSON-based storage

Version Control: Git & GitHub

🧩 Project Structure
Voyage-Trip-Companion/
│
├── backend/
│   ├── main.py
│   ├── llm.py
│   ├── itinerary_generator.py
│   ├── google_places_client.py
│   ├── place_provider.py
│   ├── schemas.py
│   └── config.py
│
├── data/
│   └── trip.store.json
│
├── requirements.txt
├── README.md
└── .gitignore

⚙️ How It Works

User provides trip details (destination, duration, preferences)

Backend processes input

AI generates a structured itinerary

Data is optionally stored for reuse or extension

▶️ How to Run Locally
# Clone the repository
git clone https://github.com/ShauryaSlayyZ/Voyage-Trip-Companion.git

# Navigate to the project
cd Voyage-Trip-Companion

# Install dependencies
pip install -r requirements.txt

# Run the backend
python backend/main.py


⚠️ Note: API keys should be stored in a .env file (not committed).

🌱 Future Scope

🌐 Frontend UI (web/mobile)

✈️ Flight & hotel integration

🗺️ Multi-city trip planning

👥 Group travel support

📶 Offline itinerary access

🏆 Hackathon Context

This project was built as part of a hackathon with a focus on:

Real-world usability

AI-driven personalization

Clean architecture and scalability

🙌 Team

Shaurya Agarwal
(and team members, if any)

📄 License

This project is open-source and intended for educational and hackathon use.
