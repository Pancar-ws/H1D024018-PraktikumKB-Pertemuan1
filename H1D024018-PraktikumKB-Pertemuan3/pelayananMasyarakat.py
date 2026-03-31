import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt # Kunci biar grafik muncul

info = ctrl.Antecedent(np.arange(0, 101), 'kejelasan_informasi')
persyaratan = ctrl.Antecedent(np.arange(0, 101), 'kejelasan_persyaratan')
petugas = ctrl.Antecedent(np.arange(0, 101), 'kemampuan_petugas')
sarpras = ctrl.Antecedent(np.arange(0, 101), 'ketersediaan_sarpras')
kepuasan = ctrl.Consequent(np.arange(0, 401), 'kepuasan_pelayanan')

def define_input_mf(var):
    var['Tidak memuaskan'] = fuzz.trapmf(var.universe, [0, 0, 60, 75])
    var['Cukup memuaskan'] = fuzz.trimf(var.universe, [60, 75, 90])
    var['memuaskan'] = fuzz.trapmf(var.universe, [75, 90, 100, 100])

define_input_mf(info)
define_input_mf(persyaratan)
define_input_mf(petugas)
define_input_mf(sarpras)

# kepuasan pelayanan [0-400]
kepuasan['Tidak memuaskan'] = fuzz.trapmf(kepuasan.universe, [0, 0, 50, 100])
kepuasan['Kurang memuaskan'] = fuzz.trimf(kepuasan.universe, [50, 100, 175])
kepuasan['Cukup memuaskan'] = fuzz.trimf(kepuasan.universe, [150, 225, 275])
kepuasan['Memuaskan'] = fuzz.trimf(kepuasan.universe, [250, 300, 350]) 
kepuasan['Sangat memuaskan'] = fuzz.trapmf(kepuasan.universe, [325, 375, 400, 400])

# RULES
ruleKe1 = ctrl.Rule(info['Tidak memuaskan'] & persyaratan['Tidak memuaskan'] & petugas['Tidak memuaskan'] & sarpras['Tidak memuaskan'], kepuasan['Tidak memuaskan'])
ruleKe2 = ctrl.Rule(info['Tidak memuaskan'] & persyaratan['Tidak memuaskan'] & petugas['Tidak memuaskan'] & sarpras['Cukup memuaskan'], kepuasan['Tidak memuaskan'])
ruleKe3 = ctrl.Rule(info['Tidak memuaskan'] & persyaratan['Tidak memuaskan'] & petugas['Tidak memuaskan'] & sarpras['Memuaskan'], kepuasan['Tidak memuaskan'])
ruleKe4 = ctrl.Rule(info['Tidak memuaskan'] & persyaratan['Tidak memuaskan'] & petugas['Cukup memuaskan'] & sarpras['Tidak memuaskan'], kepuasan['Tidak memuaskan'])
ruleKe5 = ctrl.Rule(info['Tidak memuaskan'] & persyaratan['Tidak memuaskan'] & petugas['Cukup memuaskan'] & sarpras['Cukup memuaskan'], kepuasan['Tidak memuaskan'])
ruleKe6 = ctrl.Rule(info['Tidak memuaskan'] & persyaratan['Tidak memuaskan'] & petugas['Cukup memuaskan'] & sarpras['Memuaskan'], kepuasan['Cukup memuaskan'])
ruleKe7 = ctrl.Rule(info['Tidak memuaskan'] & persyaratan['Tidak memuaskan'] & petugas['Memuaskan'] & sarpras['Tidak memuaskan'], kepuasan['Tidak memuaskan'])
ruleKe8 = ctrl.Rule(info['Tidak memuaskan'] & persyaratan['Tidak memuaskan'] & petugas['Memuaskan'] & sarpras['Cukup memuaskan'], kepuasan['Cukup memuaskan'])
ruleKe9 = ctrl.Rule(info['Tidak memuaskan'] & persyaratan['Tidak memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], kepuasan['Cukup memuaskan'])
ruleKe10 = ctrl.Rule(info['Cukup memuaskan'] & persyaratan['Cukup memuaskan'] & petugas['Cukup memuaskan'] & sarpras['Memuaskan'], kepuasan['Memuaskan'])
ruleKe11 = ctrl.Rule(info['Cukup memuaskan'] & persyaratan['Cukup memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], kepuasan['Memuaskan'])
ruleKe12 = ctrl.Rule(info['Cukup memuaskan'] & persyaratan['Memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], kepuasan['Sangat memuaskan'])
ruleKe13 = ctrl.Rule(info['Memuaskan'] & persyaratan['Memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], kepuasan['Sangat memuaskan'])

kepuasan_ctrl = ctrl.ControlSystem([ruleKe1, ruleKe2, ruleKe3, ruleKe4, ruleKe5, ruleKe6, ruleKe7, ruleKe8, ruleKe9, ruleKe10, ruleKe11, ruleKe12, ruleKe13])
kepuasan_sim = ctrl.ControlSystemSimulation(kepuasan_ctrl)

kepuasan_sim.input['kejelasan_informasi'] = 80
kepuasan_sim.input['kejelasan_persyaratan'] = 60
kepuasan_sim.input['kemampuan_petugas'] = 50
kepuasan_sim.input['ketersediaan_sarpras'] = 90

kepuasan_sim.compute()

print("Nilai Tingkat Kepuasan Pelayanan =", round(kepuasan_sim.output['kepuasan_pelayanan'], 2))
kepuasan.view(sim=kepuasan_sim)
plt.show()