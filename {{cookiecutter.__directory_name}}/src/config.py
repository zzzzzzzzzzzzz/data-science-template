import os
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))

__version__ = "0.0.1"
class Config:
    DATA_ROOT = Path(f'{basedir}/data')
    MODEL_ROOT = Path(f'{basedir}/models')

    # Debug setting
    DEBUG = True