import streamlit as st
import plotly.express as px
from core import load_data,summary

st.set_page_config(page_title="Bookings Revenue Intelligence",layout="wide")
st.title("Bookings & Revenue Intelligence")
st.caption("Synthetic executive analytics for bookings, forecast stages, renewals, revenue and variance.")
df=load_data()
regs=st.sidebar.multiselect("Region",sorted(df.region.unique()),default=sorted(df.region.unique()))
f=df[df.region.isin(regs)]
s=summary(f)
c=st.columns(4)
c[0].metric("Closed Won",f"${s['closed_won']/1e6:,.1f}M")
c[1].metric("Weighted Pipeline",f"${s['weighted_pipeline']/1e6:,.1f}M")
c[2].metric("Recognized Revenue",f"${s['revenue']/1e6:,.1f}M")
c[3].metric("Renewal Value",f"${s['renewals']/1e6:,.1f}M")
stage=f.groupby("stage",as_index=False)["booking_value"].sum()
st.plotly_chart(px.bar(stage,x="stage",y="booking_value",title="Bookings by forecast stage"),use_container_width=True)
weekly=f.groupby("week",as_index=False)[["booking_value","weighted_pipeline","recognized_revenue"]].sum()
st.plotly_chart(px.line(weekly,x="week",y=["booking_value","weighted_pipeline"],title="Weekly bookings and weighted pipeline"),use_container_width=True)
reg=f.groupby("region",as_index=False)[["booking_value","recognized_revenue"]].sum()
st.plotly_chart(px.bar(reg,x="region",y=["booking_value","recognized_revenue"],barmode="group",title="Regional performance"),use_container_width=True)
st.dataframe(f.sort_values("week",ascending=False),use_container_width=True)
