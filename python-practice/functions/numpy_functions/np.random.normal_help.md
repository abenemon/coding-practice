# Understanding np.random.normal: Drawing Random Numbers from a Normal Distribution

The function `np.random.normal()` in NumPy is used when you want to generate random numbers that follow a normal (Gaussian or "bell curve") distribution. This is one of the most common distributions in statistics and data science, where most values are clustered around a mean, with decreasing likelihood as you move further from the mean.

## Parameters Explained

- **loc**: This sets the mean ("center") of your distribution. If you want your random numbers centered around 5, set `loc=5`.
- **scale**: This is the standard deviation, which controls how spread out the numbers are. A larger `scale` means numbers will be spread further from the mean. (Must be positive.)
- **size**: This controls how many random numbers you want, and in what shape. For a single number, you can skip this. For 100 numbers, use `size=100`. For a 2D array, use something like `size=(3, 4)`.

## How to Use

Here are some practical examples:

    import numpy as np

    # Just one random number (mean 0, std 1)
    x = np.random.normal()

    # 10 random numbers, mean=5, std=2
    arr = np.random.normal(loc=5, scale=2, size=10)

    # A 2x3 array of random numbers, mean=0, std=1
    mat = np.random.normal(0, 1, size=(2, 3))

## How the Output Looks

The function returns either a single number or a NumPy array of the shape you requested, filled with random numbers that follow your specified mean and standard deviation.

## Visual Example

You can quickly see how these numbers are distributed by plotting a histogram:

    import matplotlib.pyplot as plt
    data = np.random.normal(10, 3, 1000)
    plt.hist(data, bins=30, density=True)
    plt.title('Random samples from N(10, 3^2)')
    plt.show()

## In Summary

If you want random numbers with a certain average and spread, just use:

    np.random.normal(loc, scale, size)

where `loc` is the mean, `scale` is the standard deviation, and `size` controls the shape and number of values. This is one of the fastest ways to get random data for simulations, tests, or examples in Python.

## Note

If you're starting a new project, NumPy recommends using the newer random number Generator API:

    rng = np.random.default_rng()
    rng.normal(loc, scale, size)
