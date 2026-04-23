import streamlit as st
import pandas as pd 
st.title("Business perfomance report")
revenues=[]
profits=[]
costs=[]
margins=[]
days=st.number_input("how many days?",min_value=1,step=1)
for i in range(days):
    st.subheader(f"Day {i+1}")
    
    revenue=st.number_input(f"enter revenue {i+1}",key=f"rev{i}")
    cost=st.number_input(f"enter cost {i+1}",key=f"cost{i}")
    profit=revenue-cost
    profits.append(profit)
    revenues.append(revenue)
    costs.append(cost)
    if revenue > 0:
        margin=(profit/revenue)*100
        margins.append(margin)
    else:
        margins.append(0)

if st.button("calculate report"):
    if len(profits)>0:
        st.write("---Business performance report---")

        total_profit= sum(profits)
        total_revenue= sum(revenues)
        total_cost= sum(costs)
        
        st.write("total profit",total_profit)
        st.write("total revenue",total_revenue)
        st.write("total cost",total_cost)

        max_profit=max(profits)
        min_profit=min(profits)
        st.write("best day profit:",max_profit)
        st.write("worst day profit:",min_profit)


        average_margin=sum(margins)/len(margins)
        st.write("Average margin(%):",round(average_margin,2))

        average_profit=total_profit/len(profits)
        above_count=0
        for profit in profits:
            if profit > average_profit:
                above_count += 1

        st.write("average profit:",round(average_profit,2))
        st.write("days above average:",above_count)

        days_list=[]
        for i in range(len(profits)):
            days_list.append(f"Day {i+1}")


        data=pd.DataFrame({
            "Day":days_list,
            "Revenue":revenues,
            "Cost":costs,
            "Profit":profits,
            "Margin":margins
        })

        st.subheader("Business Data")
        st.dataframe(data)

        st.subheader("Revemue,Cost and Profit")
        st.line_chart(data.set_index("Day")[["Revenue","Cost","Profit"]])

        st.subheader("Profit Margin")
        st.bar_chart(data.set_index("Day")[["Margin"]])
