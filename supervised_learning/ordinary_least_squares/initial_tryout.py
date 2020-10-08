# In [ ]
from sklearn import linear_model

# In [ ]
# Taken straight from the example
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
reg.coef_

# In [ ]
# Taken straight from the example
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 3, 8])
reg.coef_

# In [ ]
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [3, 3], [4, 4]], [0, 3, 4])
reg.coef_

# <markdown>
# Interseting that the coefficients are affected by the prediction values
# Let's see if it's one feature...

# In [ ]
#
one_reg = linear_model.LinearRegression()
one_reg.fit([[0], [1], [2]], [0, 1, 2])
one_reg.coef_
# One for one (i.e. y=mx+c is literally y=x)

# In [ ]
print("Predict with value 3:", one_reg.predict([[3]]))
print("Predict with value 4:", one_reg.predict([[4]]))
print("Predict with value 5:", one_reg.predict([[5]]))

# <markdown>
Basically, from few values, the linear model is predicting beyond the examples
since the x values will always match y values.
