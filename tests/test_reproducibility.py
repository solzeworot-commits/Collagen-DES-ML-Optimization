import pandas as pd
def test_r2_is_987():
df = pd.read_excel("../results/Приложение_4_финальное_с_выходом_150_DES.xlsx")
assert abs(df['Предсказанный выход коллагена MLP, %'].corr(df['Экспериментальный выход, %'])**2 - 1) - 0.987) < 0.005
def test_best_composition():
df = pd.read_excel("../results/Приложение_4_ДВА_ЛУЧШИХ_СОСТАВА_жирным_красным.xlsx")
assert "ChCl–ZnCl₂" in df['DES'].iloc[0]
