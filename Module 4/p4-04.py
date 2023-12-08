# import rpy2.robjects as robjects

# # Load the RData file
# robjects.r['load']('c50_model.RData')

# # Access the C5.0 model in Python
# c50fit = robjects.r['c50fit']


# # Assuming 'dat' is a pandas DataFrame loaded with your data
# # Replace column indices with the appropriate column indices in your dataset
# x = dat.iloc[:, [1, 5, 8, 9, 15, 16, 17, 18, 19]]
# y = dat['income']

# # Fit C5.0 model
# c50fit = C50()
# c50fit.fit(x, y)

# # Print summary
# print(c50fit)

# ---------------------------------------------------------------------
# import pandas as pd
# from c50 import C50Classifier

# # Assuming 'dat' is a pandas DataFrame
# # Replace the column names accordingly
# x_cols = ['col2', 'col6', 'col9', 'col10', 'col16', 'col17', 'col18', 'col19', 'col20']
# x = dat[x_cols]
# y = dat['Sincome']

# # Create and fit the C5.0 model
# c50_fit = C50Classifier()
# c50_fit.fit(x, y)

# # Display model summary
# print(c50_fit)