import apache_beam as beam
from utils.postgres.generate import FakerEvents
from utils.minio.raw_to_trusted import promotion_to_trusted
from apache_beam.options.pipeline_options import PipelineOptions


class ProcessTrusted(beam.DoFn):
    def process(self, element: str):
        promotion_to_trusted()
        yield f"Data loaded into MinIO for {element} records"


def run():
    options = PipelineOptions()

    with beam.Pipeline(options=options) as p:
        _ = (
            p
            | "GenerateData" >> beam.Create(["dummy_element"])
            | "WriteResult" >> beam.ParDo(ProcessTrusted())
        )


if __name__ == "__main__":
    run()
