up:
	docker-compose up -d

down:
	docker-compose down

install:
	pip install --no-cache-dir -r requirements.txt

run:
	python apache-bean/landing_to_raw.py  --sample_size 10

export-python-path:
	export PYTHONPATH="${PYTHONPATH}:postgres-minio-bean-bike-rental"