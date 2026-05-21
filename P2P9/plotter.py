import matplotlib.pyplot as plt
from collections import deque


class LivePlotter:
    def __init__(self, max_len=50):
        self.max_len = max_len

        self.temp_data = deque(maxlen=max_len)
        self.hum_data = deque(maxlen=max_len)
        self.time_data = deque(maxlen=max_len)

        self.fig, self.ax = plt.subplots(
            2,
            1,
            figsize=(10, 6)
        )

        self.fig.suptitle(
            'Lecturas en tiempo real del DHT11'
        )

    def update(
        self,
        timestamp,
        temperature,
        humidity
    ):
        self.time_data.append(timestamp)
        self.temp_data.append(temperature)
        self.hum_data.append(humidity)

        self.ax[0].cla()
        self.ax[1].cla()

        self.ax[0].plot(
            self.time_data,
            self.temp_data,
            'r-',
            label='Temperatura (°C)'
        )

        self.ax[1].plot(
            self.time_data,
            self.hum_data,
            'b-',
            label='Humedad (%)'
        )

        self.ax[0].set_ylabel(
            'Temperatura (°C)'
        )

        self.ax[1].set_ylabel(
            'Humedad (%)'
        )

        self.ax[1].set_xlabel(
            'Tiempo (s)'
        )

        for axis in self.ax:
            axis.grid(True)
            axis.legend(loc='upper left')

        plt.pause(0.1)
