import logging
from os import makedirs
import numpy as np
import random
import torch

def setup_logger():
    makedirs('logs', exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler('./logs/debug.log')])
    
def fix_seed(random_seed):
    torch.manual_seed(random_seed)
    torch.cuda.manual_seed(random_seed)
    torch.cuda.manual_seed_all(random_seed) # if use multi-GPU
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(random_seed)
    random.seed(random_seed)