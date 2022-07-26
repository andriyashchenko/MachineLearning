
# y = 2*x1 + 3*x2 + 4*x3


from random import randint
from sklearn.linear_model import LinearRegression

# Создание тренировочного набора данных
train_set_limit = 1000
train_set_count = 100

train_input = list()
train_output =list()
for i in range(train_set_count):
    a = randint(0, train_set_limit)
    b = randint(0, train_set_limit)
    c = randint(0, train_set_limit)
    op = 2*a + (3*b) + (4*c)
    train_input.append([a, b, c])
    train_output.append(op)

for i in range(20):
    print(train_input[i], train_output[i])
    
# Тренировка
predictor = LinearRegression()
predictor.fit(X=train_input, y=train_output)

# Прогнозирование
x_test = [[30, 40, 50]]
outcome = predictor.predict(X=x_test)
coefficients = predictor.coef_

print('Outcome : ', outcome)
print('Coefficients : ', coefficients)
