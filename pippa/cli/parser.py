from argparse import ArgumentParser
from pippa.workers.extract_worker import ExtractWorker
from pippa.workers.load_worker import LoadWorker
from pippa.workers.transform_worker import TransformWorker


def run_extract_worker(args):
    worker = ExtractWorker()
    worker.run()


def run_transform_worker(args):
    worker = TransformWorker()
    worker.run()


def run_load_worker(args):
    worker = LoadWorker()
    worker.run()


def get_parser():
    parser = ArgumentParser()
    sub = parser.add_subparsers(help='sub-command help')
    sub.required = True

    ht = 'Usage: extract_worker'
    status_cmd = sub.add_parser('extract_worker', help=ht)
    status_cmd.set_defaults(func=run_extract_worker)

    ht = 'Usage: transform_worker'
    status_cmd = sub.add_parser('transform_worker', help=ht)
    status_cmd.set_defaults(func=run_transform_worker)

    ht = 'Usage: load_worker'
    status_cmd = sub.add_parser('load_worker', help=ht)
    status_cmd.set_defaults(func=run_load_worker)

    return parser
