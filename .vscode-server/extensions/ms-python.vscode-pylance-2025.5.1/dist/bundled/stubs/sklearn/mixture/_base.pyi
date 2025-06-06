import warnings
from abc import ABCMeta, abstractmethod as abstractmethod
from numbers import Integral as Integral, Real as Real
from time import time as time
from typing import Any, ClassVar
from typing_extensions import Self

import numpy as np
from numpy import ndarray
from numpy.random.mtrand import RandomState
from scipy.special import logsumexp as logsumexp

from .. import cluster as cluster
from .._typing import Float, Int, MatrixLike
from ..base import BaseEstimator, DensityMixin
from ..cluster import kmeans_plusplus as kmeans_plusplus
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_random_state as check_random_state
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.validation import check_is_fitted as check_is_fitted

# Author: Wei Xue <xuewei4d@gmail.com>
# Modified by Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

class BaseMixture(DensityMixin, BaseEstimator, metaclass=ABCMeta):
    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: int,
        tol: float,
        reg_covar: float,
        max_iter: int,
        n_init: int,
        init_params: str,
        random_state: None | RandomState | int,
        warm_start: bool,
        verbose: int,
        verbose_interval: int,
    ) -> None: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...
    def fit_predict(self, X: MatrixLike, y: Any = None) -> ndarray: ...
    def score_samples(self, X: MatrixLike) -> ndarray: ...
    def score(self, X: MatrixLike, y: Any = None) -> Float: ...
    def predict(self, X: MatrixLike) -> ndarray: ...
    def predict_proba(self, X: MatrixLike) -> ndarray: ...
    def sample(self, n_samples: Int = 1) -> tuple[ndarray, ndarray]: ...
