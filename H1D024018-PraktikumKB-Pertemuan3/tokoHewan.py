import numpy as np
import skfuzzy as fuzz 
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

barang = ctrl.Antecedent(np.arange(0, 101), 'barang_terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301), 'permintaan')
harga = ctrl.Antecedent(np.arange(0, 100001), 'harga_per_item')
profit = ctrl.Antecedent(np.arange(0, 4000001), 'profit')
stok = ctrl.Consequent(np.arange(0, 1001), 'stok_makanan')

# barang terjual [0-100]
barang['rendah'] = fuzz.trapmf(barang.universe, [0, 0, 20, 50])
barang['sedang'] = fuzz.trimf(barang.universe, [20, 50, 80])
barang['tinggi'] = fuzz.trapmf(barang.universe, [50, 80, 100, 100])

# permintaan [0-300]
permintaan['rendah'] = fuzz.trapmf(permintaan.universe, [0, 0, 75, 150])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [75, 150, 225])
permintaan['tinggi'] = fuzz.trapmf(permintaan.universe, [150, 225, 300, 300])

# harga per item [0-100000]
harga['murah'] = fuzz.trapmf(harga.universe, [0, 0, 25000, 50000])
harga['sedang'] = fuzz.trimf(harga.universe, [25000, 50000, 75000])
harga['mahal'] = fuzz.trapmf(harga.universe, [50000, 75000, 100000, 100000])

# profit [0-4000000]
profit['rendah'] = fuzz.trapmf(profit.universe, [0, 0, 1000000, 2000000])
profit['sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 3000000])
profit['tinggi'] = fuzz.trapmf(profit.universe, [2000000, 3000000, 4000000, 4000000])

# stok makanan [0-1000]
stok['sedang'] = fuzz.trapmf(stok.universe, [0, 0, 400, 600])
stok['banyak'] = fuzz.trapmf(stok.universe, [400, 600, 1000, 1000])

# rules
rule1 = ctrl.Rule(barang['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
rule2 = ctrl.Rule(barang['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule3 = ctrl.Rule(barang['tinggi'] & permintaan['sedang'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule4 = ctrl.Rule(barang['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule5 = ctrl.Rule(barang['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
rule6 = ctrl.Rule(barang['rendah'] & permintaan['rendah'] & harga['sedang'] & profit['sedang'], stok['sedang'])

stok_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
stok_sim = ctrl.ControlSystemSimulation(stok_ctrl)

# input soal
stok_sim.input['barang_terjual'] = 80
stok_sim.input['permintaan'] = 255
stok_sim.input['harga_per_item'] = 25000
stok_sim.input['profit'] = 3500000

stok_sim.compute()
print("Jumlah Persediaan Stok Makanan =", round(stok_sim.output['stok_makanan'], 2), "unit")

stok.view(sim=stok_sim)
plt.show()