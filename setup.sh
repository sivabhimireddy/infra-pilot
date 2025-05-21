#!/bin/bash

echo "🔧 Setting up Infra Pilot MCP environment..."

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
echo "📦 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Instructions for user
echo ""
echo " Setup complete!"
echo " To activate your environment, run:"
echo "   source .venv/bin/activate"
echo ""
echo " Run embedding:"
echo "   python embed_terraform.py"
echo ""
echo " Start FastAPI backend:"
echo "   uvicorn app.main:app --reload"
echo ""
echo " Start Streamlit UI:"
echo "   streamlit run app/ui/app.py"
