import numpy as np

s_U = 1 * 15 #V

#скрещенные поляроиды
U_skr_l_0 = np.array([35, 33, 32, 34]) * 15 #V
U_skr_l2_0 = np.array([66, 66, 65, 64]) * 15 #V

U_skr_l = sum(U_skr_l_0) / len(U_skr_l_0)
U_skr_l2 = sum(U_skr_l2_0) / len(U_skr_l2_0)

delta_U_skr_l = np.array(U_skr_l_0) - U_skr_l
delta_U_skr_l2 = np.array(U_skr_l2_0) - U_skr_l2

sigma_U_skr_l = ((1/len(U_skr_l_0)) * sum(np.array(delta_U_skr_l)**2))**0.5
sigma_U_skr_l2 = ((1/len(U_skr_l2_0)) * sum(np.array(delta_U_skr_l2)**2))**0.5

error_U_skr_l = (s_U**2 + sigma_U_skr_l**2)**0.5
error_U_skr_l2 = (s_U**2 + sigma_U_skr_l2**2)**0.5

print(f' U_skr_l = {U_skr_l} ± {error_U_skr_l} V')
print(f' U_skr_l2 = {U_skr_l2} ± {error_U_skr_l2} V')



#параллельные поляроиды
U_p_l_0 = np.array([34, 34, 33, 34, 32]) * 15 #V
U_p_l2_0 = np.array([66, 64, 65, 66, 64]) * 15 #V

U_p_l = sum(U_p_l_0) / len(U_p_l_0)
U_p_l2 = sum(U_p_l2_0) / len(U_p_l2_0)

delta_U_p_l = np.array(U_p_l_0) - U_p_l
delta_U_p_l2 = np.array(U_p_l2_0) - U_p_l2

sigma_U_p_l = ((1/len(U_p_l_0)) * sum(np.array(delta_U_p_l)**2))**0.5
sigma_U_p_l2 = ((1/len(U_p_l2_0)) * sum(np.array(delta_U_p_l2)**2))**0.5

error_U_p_l = (s_U**2 + sigma_U_p_l**2)**0.5
error_U_p_l2 = (s_U**2 + sigma_U_p_l2**2)**0.5

print(f' U_p_l = {U_p_l} ± {error_U_p_l} V')
print(f' U_p_l2 = {U_p_l2} ± {error_U_p_l2} V')

#фотодиод
U_ph_min = np.array([28, 28, 30, 27]) * 15 #V
U_ph_max = np.array([57, 56, 56, 57]) * 15 #V

U_ph_l = np.array(U_ph_max) - np.array(U_ph_min)

# Вычисление среднего значения и стандартного отклонения
mean_U_ph_l = np.mean(U_ph_l)
std_dev_U_ph_l = np.std(U_ph_l, ddof=1)  # Используем ddof=1 для выборки

# Полная погрешность
total_error = np.sqrt(s_U**2 + std_dev_U_ph_l**2)

# Результаты
print(f"U_ph_l: {U_ph_l}")
print(f"Среднее значение U_ph_l: {mean_U_ph_l:.2f} V")
print(f"Стандартное отклонение U_ph_l: {std_dev_U_ph_l:.2f} V")
print(f"Полная погрешность: {total_error:.2f} V")
