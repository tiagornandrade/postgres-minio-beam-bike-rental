import argparse
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run():
    options = PipelineOptions()

    with beam.Pipeline(options=options) as p:
        lines = p | 'ReadLines' >> beam.io.ReadFromText('input.txt')
        upper_lines = lines | 'UpperLines' >> beam.Map(lambda x: x.upper())
        upper_lines | 'WriteLines' >> beam.io.WriteToText('output.txt')
        
        print('Done')


if __name__ == '__main__':
    run()
