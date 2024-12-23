import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, render_template

app = Flask(__name__)

# Загружаем модель один раз при запуске приложения
model_path = "C:\\Users\\Julia\\Desktop\\Kompozitnye\\App\\s_model\\k_m"
model = keras.models.load_model(model_path)

# Функция для прогнозирования
def set_params(params):
    # Преобразуем список параметров в массив NumPy
    params_array = np.array([params])
    prediction = model.predict(params_array)
    print("Model prediction:", prediction)  # Отладочное сообщение
    return prediction[0][0]

@app.route('/', methods=['POST', 'GET'])
def app_calculation():
    message = ''
    if request.method == 'POST':
        param_lst = []
        # Получаем данные из формы и добавляем их в список
        for i in range(1, 13):
            param = request.form.get(f'param{i}')
            if param:
                try:
                    param_lst.append(float(param))
                except ValueError:
                    return render_template("index.html", message="Ошибка: Введите числовые значения.")
        
        # Проверяем, что все 12 параметров заполнены
        if len(param_lst) == 12:
            print("Received parameters:", param_lst)  # Отладочное сообщение
            message = set_params(param_lst)
        else:
            message = "Ошибка: Все 12 параметров должны быть заполнены."
    
    # Отображаем шаблон
    return render_template("index.html", message=message)

# Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True)