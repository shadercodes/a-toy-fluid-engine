from .class_cfg import SceneEnum, VisualizeEnum, SchemeType
from utils import set_attribute_from_cfg
import sys
import config.scene_config.mouse_drag_config as scene_cfg
import config.default_config as default_cfg

debug = True

FILTER_TYPE = 'm_'
set_attribute_from_cfg(default_cfg, sys.modules[__name__], FILTER_TYPE)
set_attribute_from_cfg(scene_cfg, sys.modules[__name__], FILTER_TYPE)
SceneType = SceneEnum.MouseDragDye
VisualType = VisualizeEnum.Density
## run Scheme
run_scheme = SchemeType.Advection_Reflection

from advection import SemiLagrangeOrder, SemiLagrangeSolver, MacCormackSolver
advection_solver = MacCormackSolver

from projection import JacobiProjectionSolver ,RedBlackGaussSedialProjectionSolver
projection_solver = JacobiProjectionSolver
p_jacobi_iters = 30
dye_decay = 0.99

# save to video(gif)
bool_save = False
