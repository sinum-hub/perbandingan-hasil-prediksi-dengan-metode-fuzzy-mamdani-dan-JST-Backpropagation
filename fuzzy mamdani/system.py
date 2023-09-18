from aggregation import *
from fuzzyset import fuzzySet
import numpy as np
from helpers import *

class FuzzyInferenceSystem:

    def __init__(self, rules):
        self.rules = rules
        self.antecedents = []
        self.precedents = []

        for r in rules:
            self.antecedents.append(r[:-1])
            self.precedents.append(r[-1])

    def singleton_params(self, inputs):
        params = []
        for antc in self.antecedents:
            minimum = 10000000000000000000
            for s,i in zip(antc, inputs):
                minimum = min(minimum, s.func(i))
            params.append(minimum)
        return params

    def _common(f:fuzzySet,s:fuzzySet):
        left, right = join([f.domain, s.domain])
        maximum = -10000000000000000000
        for x in np.arange(left, sup + 1, 0.1):
            maximum = max(maximum, min(f.func(x), s.func(x)))
        return maximum
    
    def fuzzy_params(self, inputs):
        params = []
        for antc in self.antecedents:
            maxs = []
            for f,i in zip(antc, inputs):
                maxs.append(_common(f,i))
            params.append(min(maxs))
        return params

    def call_aggregation(self, inputs, method = 'mamdani', typ = 'singleton'):
        if typ == 'singleton':
            params = self.singleton_params(inputs)
        elif type == 'fuzzy':
            params = self.fuzzy_params(inputs)
        else:
            return TypeError('Type not found')

        #TODO finish set of params or degrees

        if method == 'mamdani':
            func = lambda z: max (mamdani(param, prec, z) for param, prec in zip(params, self.precedents))
        elif method == 'larsen':
            func = lambda z: max (larsen(param, prec, z) for param, prec in zip(params, self.precedents))
        else:
            return TypeError('Method not found')

        domain = join([prec.domain for prec in self.precedents])
        return fuzzySet(func, domain)

