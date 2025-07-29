>>> help(pd.DataFrame.index)
Help on AxisProperty:

    The index (row labels) of the DataFrame.

    The index of a DataFrame is a series of labels that identify each row.
    The labels can be integers, strings, or any other hashable type. The index
    is used for label-based access and alignment, and can be accessed or
    modified using this attribute.

    Returns
    -------
    pandas.Index
        The index labels of the DataFrame.

    See Also
    --------
    DataFrame.columns : The column labels of the DataFrame.
    DataFrame.to_numpy : Convert the DataFrame to a NumPy array.

    Examples
    --------
    >>> df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Aritra'],
    ...                    'Age': [25, 30, 35],
    ...                    'Location': ['Seattle', 'New York', 'Kona']},
    ...                   index=([10, 20, 30]))
    >>> df.index
    Index([10, 20, 30], dtype='int64')

    In this example, we create a DataFrame with 3 rows and 3 columns,
    including Name, Age, and Location information. We set the index labels to
    be the integers 10, 20, and 30. We then access the `index` attribute of the
    DataFrame, which returns an `Index` object containing the index labels.

    >>> df.index = [100, 200, 300]
    >>> df
        Name  Age Location
    100  Alice   25  Seattle
    200    Bob   30 New York
    300  Aritra  35    Kona

    In this example, we modify the index labels of the DataFrame by assigning
    a new list of labels to the `index` attribute. The DataFrame is then
    updated with the new labels, and the output shows the modified DataFrame
