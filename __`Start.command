cd "$(dirname "$0")"

source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

osascript -e "tell application \"Safari\"
    make new document
    set URL of document 1 to \"http://localhost:8080\"
    activate
end tell"

python3 main.py