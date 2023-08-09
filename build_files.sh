echo "BUILD_START"
python3.11 -m pip install -r requirements.txt
python3.11 -m manage.py collectstatic --noinput --clear

echo "BUILD_END"