from beir import util, LoggingHandler
from beir.datasets.data_loader import GenericDataLoader
from beir.generation import QueryGenerator as QGen
from beir.generation.models import BART

import pathlib, os
import logging

#### Just some code to print debug information to stdout
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    handlers=[LoggingHandler()])
#### /print debug information to stdout

#### Download nfcorpus.zip dataset and unzip the dataset
dataset = "nfcorpus.zip"
url = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{}".format(dataset)
out_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "datasets")
data_path = util.download_and_unzip(url, out_dir)

#### Provide the data_path where nfcorpus has been downloaded and unzipped
corpus, _, _ = GenericDataLoader(data_path).load(split="test")

#### Model Loading 
model_path = "/home/ukp/srivastava/projects/generation-train/output/msmarco/t5-small-1-epoch/checkpoint-66500"
generator = QGen(model=BART(model_path))

#### Generation
ques_per_passage = 5
batch_size = 2

generator.generate(corpus, data_path, ques_per_passage, "test")