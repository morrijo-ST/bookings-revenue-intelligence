from core import load_data,summary

def test_summary():
    d=load_data()
    s=summary(d)
    assert s['closed_won']>0
    assert s['weighted_pipeline']>=s['closed_won']
