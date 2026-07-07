import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
from sgp4.api import Satrec, jday
from astropy import units as u
from astropy.coordinates import GCRS, ITRS, TEME
from astropy.time import Time

tle_line1 = (
    "1 44204U 19023A   26132.76772565 -.00000227  00000-0  00000-0 0  9990"
)
tle_line2 = (
    "2 44204  58.6468  38.0171 0023856 234.3090 349.8662  1.00250503  6851"
)

satellite = Satrec.twoline2rv(tle_line1, tle_line2)

df = pd.read_csv(
    "only1sat.csv",
    header=None,
    names=["timestamp", "code", "x_ref", "y_ref", "z_ref", "id"],
)

df["timestamp"] = pd.to_datetime(df["timestamp"])

sgp4_x, sgp4_y, sgp4_z = [], [], []

for ts in df["timestamp"]:
    jd, fr = jday(ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second)
    e, r, v = satellite.sgp4(jd, fr)

    if e == 0:
        pos_teme = TEME(
            x=r[0] * u.km,
            y=r[1] * u.km,
            z=r[2] * u.km,
            obstime=Time(ts, scale="utc"),
        )

        pos_ecef = pos_teme.transform_to(ITRS(obstime=Time(ts, scale="utc")))

        sgp4_x.append(pos_ecef.x.value)
        sgp4_y.append(pos_ecef.y.value)
        sgp4_z.append(pos_ecef.z.value)
    else:
        sgp4_x.append(np.nan)
        sgp4_y.append(np.nan)
        sgp4_z.append(np.nan)

df["x_sgp4"] = sgp4_x
df["y_sgp4"] = sgp4_y
df["z_sgp4"] = sgp4_z


df["error_3d"] = np.sqrt(
    (df["x_ref"] - df["x_sgp4"]) ** 2
    + (df["y_ref"] - df["y_sgp4"]) ** 2
    + (df["z_ref"] - df["z_sgp4"]) ** 2
)


fig, axes = plt.subplots(4, 1, figsize=(12, 16), sharex=True)

# X
axes[0].plot(
    df["timestamp"], df["x_ref"], label="Dataset (Referencyjne)", color="black"
)
axes[0].plot(
    df["timestamp"],
    df["x_sgp4"],
    label="SGP4 (Wyliczone)",
    linestyle="--",
    color="red",
)
axes[0].set_ylabel("Pozycja X [km]")
axes[0].legend()
axes[0].grid(True)
axes[0].set_title("Porównanie pozycji na osi X")

# Y
axes[1].plot(df["timestamp"], df["y_ref"], color="black")
axes[1].plot(df["timestamp"], df["y_sgp4"], linestyle="--", color="green")
axes[1].set_ylabel("Pozycja Y [km]")
axes[1].grid(True)
axes[1].set_title("Porównanie pozycji na osi Y")

# Z
axes[2].plot(df["timestamp"], df["z_ref"], color="black")
axes[2].plot(df["timestamp"], df["z_zgp4" if "z_zgp4" in df else "z_sgp4"], linestyle="--", color="blue")
axes[2].set_ylabel("Pozycja Z [km]")
axes[2].grid(True)
axes[2].set_title("Porównanie pozycji na osi Z")


axes[3].plot(
    df["timestamp"], df["error_3d"], color="purple", label="Błąd całkowity 3D"
)
axes[3].set_ylabel("Różnica pozycji [km]")
axes[3].set_xlabel("Data i czas [UTC]")
axes[3].grid(True)
axes[3].set_title("Całkowity błąd odległości 3D (Ref vs SGP4)")

plt.tight_layout()
plt.show()