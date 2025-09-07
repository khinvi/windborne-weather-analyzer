#!/bin/bash

# ==================================
# DEPLOYMENT SCRIPT FOR VERCEL
# ==================================

echo "🚀 Weather Pattern ML Analyzer - Deployment Script"
echo "=================================================="

# Step 1: Create project directory
echo "📁 Creating project directory..."
mkdir -p weather-ml-analyzer
cd weather-ml-analyzer

# Step 2: Save the HTML file
echo "💾 Creating index.html..."
# Copy the HTML content from the artifact above into index.html

# Step 3: Create package.json for Vercel
echo "📦 Creating package.json..."
cat > package.json << 'EOF'
{
  "name": "weather-ml-analyzer",
  "version": "1.0.0",
  "description": "Weather Pattern ML Analyzer for WindBorne Systems",
  "scripts": {
    "start": "python -m http.server 8000"
  },
  "author": "Arnav Khinvasara"
}
EOF

# Step 4: Create vercel.json configuration
echo "⚙️ Creating Vercel configuration..."
cat > vercel.json << 'EOF'
{
  "version": 2,
  "builds": [
    {
      "src": "index.html",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
EOF

# Step 5: Install Vercel CLI (if not installed)
echo "📥 Checking Vercel CLI..."
if ! command -v vercel &> /dev/null; then
    echo "Installing Vercel CLI..."
    npm i -g vercel
fi

# Step 6: Deploy to Vercel
echo "🌐 Deploying to Vercel..."
echo "Please follow the prompts to deploy your application."
echo "When asked:"
echo "  - Set up and deploy: Y"
echo "  - Which scope: Select your account"
echo "  - Link to existing project: N"
echo "  - Project name: weather-ml-analyzer-arnav"
echo "  - Directory: ./"
echo "  - Want to override settings: N"

vercel --prod

echo "✅ Deployment complete! Your app URL will be shown above."
echo ""
echo "=================================================="
echo "ALTERNATIVE DEPLOYMENT OPTIONS"
echo "=================================================="

echo "Option 2: Deploy to Netlify"
echo "---------------------------"
echo "1. Go to https://app.netlify.com"
echo "2. Drag and drop the project folder"
echo "3. Your site will be live immediately"

echo ""
echo "Option 3: Deploy to GitHub Pages"
echo "--------------------------------"
echo "1. Create a new GitHub repository"
echo "2. Push the index.html file"
echo "3. Go to Settings > Pages"
echo "4. Select 'Deploy from branch' and choose main"
echo "5. Your site will be available at https://[username].github.io/[repo-name]"

echo ""
echo "=================================================="
echo "MANUAL TESTING INSTRUCTIONS"
echo "=================================================="
echo "To test locally before deploying:"
echo "1. Open index.html in your browser"
echo "2. Or run: python -m http.server 8000"
echo "3. Visit: http://localhost:8000"