up:
	docker-compose up -d

down:
	docker-compose down

install:
	pip install --no-cache-dir -r requirements.txt

run-load-raw:
	python pipeline_beam/landing_to_raw.py

run-load-trusted:
	python pipeline_beam/raw_to_trusted.py

run-load-refined:
	python pipeline_beam/trusted_to_refined.py

export-python-path:
	export PYTHONPATH="$${PYTHONPATH}:$$(pwd)"