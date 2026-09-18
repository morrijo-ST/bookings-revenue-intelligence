from pathlib import Path
import numpy as np
from streamlit.testing.v1 import AppTest

APP=Path(__file__).resolve().parents[1]/'app.py'
def app():
    at=AppTest.from_file(str(APP),default_timeout=30).run()
    assert not at.exception
    return at

def test_open_pipeline_excludes_closed_won():
    at=app()
    detail=at.dataframe[0].value
    expected=detail.loc[detail.stage!='Closed Won','weighted_pipeline'].sum()
    assert at.metric[1].value==f'${expected/1e6:,.2f}M'
    assert expected<detail.weighted_pipeline.sum()
