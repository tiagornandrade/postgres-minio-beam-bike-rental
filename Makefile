up:
	docker-compose up -d

down:
	docker-compose down

install:
	pip install --no-cache-dir -r requirements.txt

run-load-raw:
	python pipeline_beam/landing_to_raw.py --sample_size 10

run-load-trusted:
	python pipeline_beam/raw_to_trusted.py

export-python-path:
	export PYTHONPATH="$${PYTHONPATH}:$$(pwd)"