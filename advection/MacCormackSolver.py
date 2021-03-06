import taichi as ti
from enum import Enum
from .AbstractAdvectionSolver import AdvectionSolver
from .SemiLagrangianSolver import SemiLagrangeSolver

@ti.data_oriented
class MacCormackSolver(AdvectionSolver):

    def __init__(self, cfg, grid):
        super().__init__(cfg)
        self.RK = cfg.semi_order
        self.grid = grid
        self.subsolver = SemiLagrangeSolver(cfg, grid)

    @ti.func
    def advect_func(self,
                    vec_field: ti.template(),
                    q_cur: ti.template(),
                    q_nxt: ti.template(),
                    dt: ti.template()):

        for I in ti.grouped(vec_field):
            pos = (I + 0.5) * self.cfg.dx
            p_mid = self.subsolver.backtrace(vec_field, pos, dt)
            q_mid = self.grid.interpolate_value(q_cur, p_mid)

            p_fin = self.subsolver.backtrace(vec_field, p_mid, -dt)
            q_fin = self.grid.interpolate_value(q_cur, p_fin)

            q_nxt[I] = q_mid + 0.5 * (q_fin - q_cur[I])
            # clipping to prevent overshooting
            if (ti.static(self.cfg.macCormack_clipping)):
                # ref: advection.py from class 4
                min_val, max_val = self.grid.sample_minmax(q_cur, p_mid)
                cond = min_val < q_nxt[I] < max_val
                for k in ti.static(range(cond.n)):
                    if not cond[k]:
                        q_nxt[I][k] = q_mid[k]


    @ti.kernel
    def advect(self,
               vec_field: ti.template(),
               q_cur: ti.template(),
               q_nxt: ti.template(),
               dt: ti.template()):
        self.advect_func(vec_field, q_cur, q_nxt, dt)


