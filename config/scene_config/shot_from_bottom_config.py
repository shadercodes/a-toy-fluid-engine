from config.default_config.basic_config import m_dt as dt
from config.default_config.basic_config import m_res as res
import taichi as ti
import numpy as np

m_fluid_color = ti.Vector(list(np.random.rand(3) * 0.7 + 0.3))
m_f_strength = 10000.0
m_dye_decay = 0.99

m_force_radius = res[0] / 3.0
m_inv_force_radius = 1.0 / m_force_radius
m_inv_dye_denom = 4.0 / (res[0] / 15.0)**2
m_f_strength_dt = m_f_strength * dt

m_f_gravity = ti.static(9.8)
m_fluid_shot_direction = ti.Vector([0.0, 1.0])
m_direct_X_force = m_f_strength * m_fluid_shot_direction
m_source_x = ti.static(res[0] / 2)
m_source_y = ti.static(0)