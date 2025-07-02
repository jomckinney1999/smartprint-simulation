import streamlit as st
import matplotlib.pyplot as plt

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

# Streamlit UI
st.set_page_config(page_title="SmartPrint Simulation Model", layout="centered")

st.title("3D Printing Simulation Efficiency Model")
st.caption("An interactive model to showcase the ROI and operational impact of simulation technologies like SmartPrint.")

# Sidebar Inputs
st.sidebar.header("Simulation Parameters")
printer_count = st.sidebar.slider("Number of Printers", 1, 50, 10)
jobs_per_printer_per_week = st.sidebar.slider("Jobs per Printer per Week", 1, 100, 20)
failure_rate = st.sidebar.slider("Failure Rate (%)", 0.0, 1.0, 0.15)
time_lost_per_failure = st.sidebar.slider("Time Lost per Failure (hrs)", 0.0, 10.0, 2.0)
hourly_labor_cost = st.sidebar.slider("Hourly Labor Cost ($)", 10, 200, 30)
material_waste_cost = st.sidebar.slider("Material Cost per Failure ($)", 1, 100, 15)
simulation_effectiveness = st.sidebar.slider("Simulation Effectiveness (%)", 0.0, 1.0, 0.5)
simulation_tool_cost = st.sidebar.slider("Monthly Simulation Tool Cost ($)", 0, 10000, 1000)

# Run model
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

# Results Output
st.markdown("## Simulation Results Summary")
st.markdown("---")

st.markdown("### Operational Metrics")
st.write(f"Total Print Jobs/Month: {results['Total Print Jobs/Month']}")
st.write(f"Failure Rate (Before): {results['Failure Rate (Before)']}")
st.write(f"Failure Rate (After): {results['Failure Rate (After)']}")

st.markdown("### Time Lost to Failures")
st.write(f"Labor Hours Lost (Before): {results['Labor Hours Lost (Before)']}")
st.write(f"Labor Hours Lost (After): {results['Labor Hours Lost (After)']}")

st.markdown("### Material & Cost Impact")
st.write(f"Material Cost Lost (Before): {results['Material Cost Lost (Before)']}")
st.write(f"Material Cost Lost (After): {results['Material Cost Lost (After)']}")
st.write(f"Total Monthly Cost (Before): {results['Total Monthly Cost (Before)']}")
st.write(f"Total Monthly Cost (After): {results['Total Monthly Cost (After)']}")

st.markdown("### ROI Snapshot")
st.write(f"Simulation Tool Cost: {results['Simulation Tool Cost']}")
st.write(f"Net Savings: {results['Net Savings']}")
st.write(f"ROI: {results['ROI (%)']}")

# Description
st.markdown("---")
st.markdown("## 📘 What This Model Does")
st.markdown("""
This simulation estimates the time, cost, and resource impact of failed 3D print jobs in a typical additive manufacturing environment.
It then models how quantum or AI-driven simulation tools (like SmartPrint) could reduce these inefficiencies.
You can adjust key assumptions and immediately see the projected ROI and savings.
""")

# Takeaway
st.markdown("## 🧠 Key Takeaway")
roi_numeric = float(results["ROI (%)"].strip('%'))

if roi_numeric > 500:
    st.success("🚀 Simulation technology could drastically improve efficiency and cost savings. Strong ROI indicates high-value potential.")
elif roi_numeric > 100:
    st.info("✅ Simulation tools offer meaningful efficiency improvements and a promising investment opportunity.")
elif roi_numeric > 0:
    st.warning("⚠️ Some return on investment exists, but effectiveness or strategy may need refinement.")
else:
    st.error("🔴 No return under current conditions. Optimize assumptions or run a pilot test.")

# Bar Chart: Before vs After Costs
before_labor = float(results["Labor Hours Lost (Before)"]) * hourly_labor_cost
after_labor = float(results["Labor Hours Lost (After)"]) * hourly_labor_cost
before_material = float(results["Material Cost Lost (Before)"].replace('$','').replace(',',''))
after_material = float(results["Material Cost Lost (After)"].replace('$','').replace(',',''))

before_costs = [before_labor, before_material]
after_costs = [after_labor, after_material]

labels = ['Labor Cost', 'Material Cost']
x = range(len(labels))

fig, ax = plt.subplots()
ax.bar(x, before_costs, width=0.4, label='Before', align='center')
ax.bar([i + 0.4 for i in x], after_costs, width=0.4, label='After', align='center')
ax.set_xticks([i + 0.2 for i in x])
ax.set_xticklabels(labels)
ax.set_ylabel("Cost ($)")
ax.set_title("Monthly Labor & Material Costs: Before vs After Simulation")
ax.legend()

st.pyplot(fig)
