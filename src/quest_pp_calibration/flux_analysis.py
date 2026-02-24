import numpy as np
from scipy.optimize import curve_fit

class FluxDecayModel:
    """
    透過流束の減衰過程を解析解に基づき計算・最適化するクラス。
    """
    def __init__(self, kd, ji, jf=1, L=2e-5):
        self.kd = kd
        self.ji = ji
        self.jf = jf
        self.L = L
        self.log_ku_opt = None

    def flux_function(self, t, log10_ku):
        """
        流束衰退の理論式 (解析解)
        ※ curve_fit用。第一引数に独立変数、第二引数に最適化対象のパラメータをとる。
        """
        ku = 10.0**log10_ku
        
        # タイムコンスタント（時定数）の計算
        time_constant = (2 * (ku + self.kd) * np.sqrt(self.jf)) / (np.sqrt(self.kd) * self.L)
        
        # 中間変数 A の計算
        term = np.sqrt(self.ji / self.jf)
        A_prefix = (1 + term) / (1 - term)
        A = A_prefix * np.exp(time_constant * t)
        
        return self.jf * ((A - 1) / (A + 1))**2

    def fit_ku(self, t_data, y_data, p0_log10_ku=-31):
        """
        実験データに対して ku を最適化し、推定された ku を返す。
        """
        popt, _ = curve_fit(self.flux_function, t_data, y_data, p0=[p0_log10_ku])
        self.log_ku_opt = popt[0]
        return self.log_ku_opt
    
    @property
    def ku_opt(self):
        """10のべき乗に変換した本来の ku 値"""
        return 10**self.log_ku_opt if self.log_ku_opt is not None else None
    
    @property
    def ku_details(self):
        """仮数部、指数部、オーダーを辞書形式で返す"""
        if self.ku_opt is None:
            return {}
        
        # 指数表記文字列から分解
        mantissa_str, exponent_str = f"{self.ku_opt:e}".split('e')
        
        return {
            "mantissa": float(mantissa_str),
            "exponent": int(exponent_str),
            "order": 10**int(exponent_str)
        }