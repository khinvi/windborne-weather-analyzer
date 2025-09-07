#!/usr/bin/env python3
"""
WindBorne Systems - Software Engineering Intern Application Submission
Author: Arnav Khinvasara
"""

import json
import requests
import time
from datetime import datetime

CONFIG = {
    "name": "Arnav Khinvasara",
    "email": "arnav707@gmail.com",
    "role": "Software Engineering Intern Product",
    "submission_url": "https://windborne-weather-analyzer.vercel.app/",
    "portfolio_url": "https://khinvi.github.io/",
    "resume_url": "https://github.com/khinvi/windborne-weather-analyzer/blob/main/docs/Arnav%20Khinvasara%20Resum%C3%A9%20-%20AUGUST%202025.pdf", 
    "notes": """M.S. Computer Science student at UCSD specializing in AI/ML and Computer Systems. Currently building clipshot.ai, a domain-specific sports LLM for professional sports teams. Strong background in data systems, ML pipelines, and cloud infrastructure (AWS Certified). Previous internships at Glooko and Malwarebytes working on scalable systems and data ingestion.

Some things that I wanted to showcase in the Weather Pattern ML Analyzer:
- Interactive map visualization with all ASOS stations
- Real-time data fetching (proper rate limiting and error handling)
- ML-powered insights including trend analysis, anomaly detection, and correlation analysis
- Clean, modern UI (responsive design)
- Robust data corruption handling as mentioned in the requirements

The application uses TensorFlow.js for client-side ML processing, ensuring fast performance without backend dependencies. I implemented statistical methods for anomaly detection and Pearson correlation for parameter relationships."""
}

def validate_urls():
    """
    Validate that all URLs are accessible
    """
    print("🔍 Validating URLs...")
    print("-" * 30)
    
    urls_to_check = {
        "Portfolio": CONFIG["portfolio_url"],
        "Submission": CONFIG["submission_url"],
        "Resume": CONFIG["resume_url"]
    }
    
    all_valid = True
    for name, url in urls_to_check.items():
        if url and not url.startswith("YOUR_"):
            try:
                response = requests.head(url, timeout=5, allow_redirects=True)
                if response.status_code < 400:
                    print(f"✅ {name}: {url} - OK")
                else:
                    print(f"❌ {name}: {url} - Status {response.status_code}")
                    all_valid = False
            except Exception as e:
                print(f"❌ {name}: {url} - Error: {str(e)}")
                all_valid = False
        else:
            print(f"⚠️  {name}: Not configured yet")
            all_valid = False
    
    return all_valid

def submit_application():
    """
    Submit the application to WindBorne Systems
    """
    print("\n📮 SUBMITTING APPLICATION")
    print("=" * 50)
    
    # Check if URLs are configured
    if "YOUR_" in CONFIG["submission_url"] or "YOUR_" in CONFIG["resume_url"]:
        print("❌ ERROR: Please update the CONFIG section with your actual URLs")
        print("   - submission_url: Your deployed Vercel/Netlify app URL")
        print("   - resume_url: Your resume URL from GitHub or Google Drive")
        return False
    
    # Prepare the application data
    application_data = {
        "career_application": {
            "name": CONFIG["name"],
            "email": CONFIG["email"],
            "role": CONFIG["role"],
            "submission_url": CONFIG["submission_url"],
            "portfolio_url": CONFIG["portfolio_url"],
            "resume_url": CONFIG["resume_url"],
            "notes": CONFIG["notes"]
        }
    }
    
    print("📝 Application Details:")
    print(json.dumps(application_data, indent=2))
    print()
    
    # Confirm before sending
    confirm = input("Ready to submit? (yes/no): ").lower().strip()
    if confirm != "yes":
        print("❌ Application not submitted.")
        return False
    
    # Submit the application
    try:
        print("\n🚀 Sending application...")
        response = requests.post(
            "https://windbornesystems.com/career_applications.json",
            json=application_data,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if response.status_code == 200 or response.status_code == 201:
            print("✅ SUCCESS! Application submitted successfully!")
            print(f"   Response: {response.text}")
            print(f"   Timestamp: {datetime.now().isoformat()}")
            
            # Save confirmation
            with open("application_confirmation.json", "w") as f:
                json.dump({
                    "submitted": True,
                    "timestamp": datetime.now().isoformat(),
                    "response": response.text,
                    "status_code": response.status_code,
                    "application": application_data
                }, f, indent=2)
            print("   Confirmation saved to: application_confirmation.json")
            return True
        else:
            print(f"❌ ERROR: Server returned status code {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: Failed to submit application")
        print(f"   Error: {str(e)}")
        return False

def main():
    """
    Main execution flow
    """
    print("🌟 WindBorne Systems - Application Submission Tool")
    print("=" * 50)
    print()
    
    print("📋 CURRENT CONFIGURATION")
    print("-" * 30)
    print(f"Name: {CONFIG['name']}")
    print(f"Email: {CONFIG['email']}")
    print(f"Role: {CONFIG['role']}")
    print(f"Portfolio: {CONFIG['portfolio_url']}")
    print(f"Submission URL: {CONFIG['submission_url']}")
    print(f"Resume URL: {CONFIG['resume_url']}")
    print()
    
    # Step 3: Validate URLs
    if not validate_urls():
        print("\n⚠️  WARNING: Some URLs are not accessible or not configured.")
        print("Please ensure all URLs are working before submitting.")
        print()
    
    # Step 4: Submit application
    print("\n" + "=" * 50)
    print("FINAL CHECKLIST:")
    print("☐ Weather ML Analyzer deployed and accessible")
    print("☐ Resume uploaded and URL is public")
    print("☐ All URLs validated and working")
    print("☐ Application details reviewed")
    print("=" * 50)
    print()
    
    submit_application()

if __name__ == "__main__":
    main()