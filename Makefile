create-virtual-env:
	python -m venv .env

install-requirements:
	pip install -r requirements.txt

run:
	python main.py