class PulseShape:
    def __init__(self, name, pulse_shape):
        self._name = name
        self._pulse_shape = pulse_shape

    @property
    def name(self):
        return self._name
    
    def __call__(self, samples_per_symbol):
        return self._pulse_shape(samples_per_symbol)