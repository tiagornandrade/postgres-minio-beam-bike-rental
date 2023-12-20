import argparse
import apache_beam as beam
from utils.postgres.generate import FakerEvents
from utils.minio.raw_to_trusted import promotion_to_trusted
from apache_beam.options.pipeline_options import PipelineOptions


class ProcessTrusted(beam.DoFn):
    def process(self, element: str):
        promotion_to_trusted()
        yield f'Data loaded into MinIO for {element} records'


def run(sample_size):
    options = PipelineOptions()

    with beam.Pipeline(options=options) as p:
        _ = (
            p
            | 'GenerateData' >> beam.Create([sample_size])
            | 'WriteResult' >> beam.ParDo(ProcessTrusted())
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample_size', dest='sample_size', type=int, default=10,
                        help='Sample size for data generation')
    known_args, pipeline_args = parser.parse_known_args()

    run(known_args.sample_size)
