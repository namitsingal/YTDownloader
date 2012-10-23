setup:
	virtualenv ./venv
	./venv/bin/pip install -r requirements.txt

run:
	export PYTHONPATH='/home/namit/repo/ytdownloader/venv/lib/python2.7/site-packages'
	gunicorn main:app
