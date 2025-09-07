# 🌦️ WindBorne Weather Analyzer

An interactive Weather Pattern ML Analyzer for ASOS stations, built as part of the WindBorne Systems Software Engineering Intern application.

## 🎯 Features

- **Interactive Map**: Visualize all ASOS weather stations across the US
- **Real-time Data**: Fetch historical weather data with proper rate limiting
- **ML Analysis**: 
  - Temperature trend prediction
  - Anomaly detection
  - Correlation analysis between weather parameters
- **Modern UI**: Responsive design with smooth animations
- **Error Handling**: Robust handling of corrupted data

## 🚀 Live Demo

[View Live Application](https://windborne-weather-analyzer.vercel.app)

## 💻 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Mapping**: Leaflet.js
- **Visualization**: Chart.js
- **ML**: TensorFlow.js
- **Deployment**: Vercel

## 🏃‍♂️ Running Locally

```bash
# Clone the repository
git clone https://github.com/khinvi/windborne-weather-analyzer.git

# Navigate to directory
cd windborne-weather-analyzer

# Start local server
python3 -m http.server 8000

# Open in browser
open http://localhost:8000
```

## 📊 API Usage

The application uses the WindBorne Systems ASOS API:
- Endpoint: `https://sfc.windbornesystems.com`
- Rate limit: 20 requests per minute
- Implements automatic rate limiting and error handling
