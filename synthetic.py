import numpy as np
import pandas as pd

def generate_bookings_data(seed=42):
    rng=np.random.default_rng(seed)
    dates=pd.date_range("2026-01-05","2026-12-28",freq="W-MON")
    stages=["Closed Won","Commit","Best Case","Pipeline"]
    regions=["North America","Europe","Asia Pacific","Middle East & Africa"]
    rows=[]
    for d in dates:
        for reg in regions:
            for stage in stages:
                base={"Closed Won":1.5e6,"Commit":1.0e6,"Best Case":.7e6,"Pipeline":.55e6}[stage]
                amount=base*rng.uniform(.65,1.35)*{"North America":1.3,"Europe":.95,"Asia Pacific":.8,"Middle East & Africa":.5}[reg]
                probability={"Closed Won":1,"Commit":.8,"Best Case":.5,"Pipeline":.2}[stage]
                revenue=amount*rng.uniform(.22,.42) if stage=="Closed Won" else 0
                renewal=amount*rng.uniform(.35,.75)
                rows.append([d,reg,stage,amount,probability,revenue,renewal])
    return pd.DataFrame(rows,columns=["week","region","stage","booking_value","probability","recognized_revenue","renewal_value"])
