import apache_beam as beam
from utils.postgres.generate import FakerEvents
from utils.minio.trusted_to_refined import promotion_to_refined
from apache_beam.options.pipeline_options import PipelineOptions


class ProcessRefined(beam.DoFn):
    def process(self, element: str):
        promotion_to_refined()
        yield f"Data loaded into MinIO for {element} records"


def run():
    options = PipelineOptions()

    with beam.Pipeline(options=options) as p:
        _ = (
            p
            | "GenerateData" >> beam.Create(["dummy_element"])
            | "WriteResult" >> beam.ParDo(ProcessRefined())
        )


if __name__ == "__main__":
    run()
