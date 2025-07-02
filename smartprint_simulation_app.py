
# smartprint_simulation_app.py
import streamlit as st

def run_simulation(
    printer_count, 
    jobs_per_printer_per_week, 
    failure_rate, 
    time_lost_per_failure,
    hourly_labor_cost,
    material_waste_cost,
    simulation_effectiveness,
    simulation_tool_cost
):
    weeks_per_month = 4
    total_jobs = printer_count * jobs_per_printer_per_week * weeks_per_month
    failed_jobs = total_jobs * failure_rate
    labor_hours_lost = failed_jobs * time_lost_per_failure
    labor_cost_lost = labor_hours_lost * hourly_labor_cost
    material_cost_lost = failed_jobs * material_waste_cost
    total_cost_lost = labor_cost_lost + material_cost_lost

    new_failure_rate = failure_rate * (1 - simulation_effectiveness)
    new_failed_jobs = total_jobs * new_failure_rate
    new_labor_hours = new_failed_jobs * time_lost_per_failure
    new_labor_cost = new_labor_hours * hourly_labor_cost
    new_material_cost = new_failed_jobs * material_waste_cost
    new_total_cost = new_labor_cost + new_material_cost + simulation_tool_cost

    savings = total_cost_lost - new_total_cost
    roi = (savings - simulation_tool_cost) / simulation_tool_cost if simulation_tool_cost else 0

    return {
        "Total Print Jobs/Month": total_jobs,
        "Failure Rate (Before)": f"{failure_rate:.0%}",
        "Failure Rate (After)": f"{new_failure_rate:.0%}",
        "Labor Hours Lost (Before)": labor_hours_lost,
        "Labor Hours Lost (After)": new_labor_hours,
        "Material Cost Lost (Before)": f"${material_cost_lost:,.2f}",
        "Material Cost Lost (After)": f"${new_material_cost:,.2f}",
        "Total Monthly Cost (Before)": f"${total_cost_lost:,.2f}",
        "Total Monthly Cost (After)": f"${new_total_cost:,.2f}",
        "Simulation Tool Cost": f"${simulation_tool_cost:,.2f}",
        "Net Savings": f"${savings:,.2f}",
        "ROI (%)": f"{roi:.2%}"
    }

st.title("3D Printing Simulation Efficiency Model")

st.sidebar.header("Simulation Parameters")
printer_count = st.sidebar.slider("Number of Printers", 1, 50, 10)
jobs_per_printer_per_week = st.sidebar.slider("Jobs per Printer per Week", 1, 100, 20)
failure_rate = st.sidebar.slider("Failure Rate (%)", 0.0, 1.0, 0.15)
time_lost_per_failure = st.sidebar.slider("Time Lost per Failure (hrs)", 0.0, 10.0, 2.0)
hourly_labor_cost = st.sidebar.slider("Hourly Labor Cost ($)", 10, 200, 30)
material_waste_cost = st.sidebar.slider("Material Cost per Failure ($)", 1, 100, 15)
simulation_effectiveness = st.sidebar.slider("Simulation Effectiveness (%)", 0.0, 1.0, 0.5)
simulation_tool_cost = st.sidebar.slider("Monthly Simulation Tool Cost ($)", 0, 10000, 1000)

results = run_simulation(
    printer_count,
    jobs_per_printer_per_week,
    failure_rate,
    time_lost_per_failure,
    hourly_labor_cost,
    material_waste_cost,
    simulation_effectiveness,
    simulation_tool_cost
)

st.subheader("Simulation Results")
for k, v in results.items():
    st.markdown(f"**{k}:** {v}")
