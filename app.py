from tensorflow import keras
import pandas as pd

model_loaded = keras.models.load_model(r"model")
collumns={
"Плотность, кг/м3: " :0,
"модуль упругости, ГПа: ":0,
"Количество отвердителя, м.%: ":0,
"Содержание эпоксидных групп,%_2: ":0,
"Температура вспышки, С_2: ":0,
"Поверхностная плотность, г/м2: ":0,
"Модуль упругости при растяжении, ГПа: ":0,
"Прочность при растяжении, МПа: ":0,
"Потребление смолы, г/м2	999.0: ":0,
"Угол нашивки, град: ":0,
"Шаг нашивки: ":0,
"Плотность нашивки: ":0,
}

print("Модель прогноза 'Соотношение матрица-наполнитель'")
for collumn_name in collumns:
    while True:
        try:
            param_val = input(collumn_name)
            param_value=float(param_val)
        except:
            print("ОШИБКА введите числовое значение")
            continue
        break
    collumns[collumn_name] = param_value
    
df= pd.DataFrame([collumns])
test_predictions = model_loaded.predict(df).flatten()
print(" Прогнозное значение 'Соотношение матрица-наполнитель':",str(test_predictions)[1:-1])

