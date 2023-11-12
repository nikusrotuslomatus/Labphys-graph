import matplotlib.pyplot as plt
import numpy as np
# Data from the image
wavelengths_nm = [404.7, 407.8, 433.9, 434.7, 435.8, 491.6, 496.2, 512, 546.1, 567.6, 572.0, 579.0, 607.3, 612.3, 623.6, 671.6, 690.7]
angles_m = [604, 668, 1150, 1156, 1162, 1816, 1858, 1948, 2236, 2366, 2414, 2418, 2572, 2638, 2776, 3052, 3214]
angles_m2 = [1450, 1512, 1614, 1756, 1960, 2228, 2390, 2438, 2472, 2580, 2664, 2744]



# Fit a polynomial regression model
degree = 4  # you can change this to adjust the fit
coefficients = np.polyfit(angles_m, wavelengths_nm, degree)
poly = np.poly1d(coefficients)

# Predict the wavelengths for the new angles
predicted_wavelengths = poly(angles_m2)
print(predicted_wavelengths)
# Plot
plt.figure(figsize=(10, 6))
plt.plot(wavelengths_nm, angles_m, 'o-', color='blue', label="Known Data")
plt.plot(predicted_wavelengths, angles_m2, 'o', color='red', label="Predicted Wavelengths")
plt.title("Graph from Data")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Angle (m°)")
plt.legend()
plt.grid(True)
plt.show()
'''[457.1742095  462.95994373 473.0827529  488.3846656  512.64091909
 547.89202552 570.53672039 577.36895549 582.2310317  597.74672577
 609.81969534 621.24918713]'''