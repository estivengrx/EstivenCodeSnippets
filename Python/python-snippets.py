# The best way to get the path of a file in Python is to use the pathlib library, 
# which provides an easy and efficient way to handle file paths.
# Path.resolve.parents is used to go up in the directory structure, 
# and you can specify how many levels to go up 
# by replacing "NUMBER OF FOLDERS TO GO UP" with the appropriate number.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents["NUMBER OF FOLDERS TO GO UP"]
labels_path = BASE_DIR / "other_folder" / "file.txt"  # path to the labels file


# __________________ SEPARATION BETWEEN CODE SNIPPETS __________________


# This is how to call a python module from another folder, 
# that is following this structure:
# project/
# ├── src/
# |   ├── python/
# │     ├── main.py
# ├── tests/
# │   ├── module.py
# In this case, you can import the main.py in module.py like this:

import sys, os
# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import using the full module path from the root
from src.python import main


# __________________ SEPARATION BETWEEN CODE SNIPPETS __________________

# Code to perform a random sampling acceptance-rejection algorithm in Python
import numpy as np
import tqdm

def random_sampling_acceptance_rejection(function: callable, x_min: float, x_max: float, n_samples: int, *args, **kwargs) -> np.ndarray:
    """
    Perform random sampling using the acceptance-rejection method.
    Uses vectorized batches for performance and tqdm for progress tracking.

    Parameters
    ----------
    function : callable
        The function to sample from.
    x_min : float
        Minimum value of x to sample.
    x_max : float
        Maximum value of x to sample.
    n_samples : int
        The number of accepted samples to generate.

    Returns
    -------
    np.ndarray
        Accepted normalized electron energy samples.
    """
    y_values = function(np.linspace(x_min, x_max, n_samples), *args, **kwargs)
    min_rate, max_rate = np.min(y_values), np.max(y_values)

    batch_size = 500_000  # candidates generated per iteration
    accepted = []
    n_accepted = 0

    # tqdm tracks accepted samples, total = n_samples is the finish line
    with tqdm(total=n_samples,
            desc="Sampling",
            unit="events",
            colour="blue",
            dynamic_ncols=True) as pbar:

        while n_accepted < n_samples:
            x_rand = np.random.uniform(x_min, x_max, batch_size)
            y_rand = np.random.uniform(min_rate, max_rate, batch_size)
            mask = y_rand <= function(x_rand, *args, **kwargs)

            batch_accepted = x_rand[mask]
            accepted.append(batch_accepted)

            new = len(batch_accepted)
            n_accepted += new
            pbar.update(new)   # advance bar by however many were accepted
