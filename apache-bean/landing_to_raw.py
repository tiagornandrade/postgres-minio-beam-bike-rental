import argparse
import apache_beam as beam
from utils.postgres.generate import FakerEvents
from utils.minio.landing_to_raw import process_etl
from apache_beam.options.pipeline_options import PipelineOptions


class GenerateData(beam.DoFn):
    def process(self, element: int):
        db_uri = "postgresql://postgres:postgres@localhost:5432/postgres"
        faker_events = FakerEvents(db_uri)
        faker_events.create_stations(element)
        faker_events.create_status(element)
        faker_events.create_trips(element)
        yield f'Data generated and inserted into PostgreSQL for {element} records'


class ProcessRaw(beam.DoFn):
    def process(self, element: str):
        process_etl()
        yield f'Data loaded into MinIO for {element} records'


def run(sample_size):
    options = PipelineOptions()

    with beam.Pipeline(options=options) as p:
        _ = (
            p
            | 'GenerateData' >> beam.Create([sample_size])
            | 'ProcessData' >> beam.ParDo(GenerateData())
            | 'WriteResult' >> beam.ParDo(ProcessRaw())
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample_size', dest='sample_size', type=int, default=10,
                        help='Sample size for data generation')
    known_args, pipeline_args = parser.parse_known_args()

    run(known_args.sample_size)
