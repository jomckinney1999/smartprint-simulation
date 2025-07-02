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
        "ROI (%)": f"{roi:.2%}",
        "ROI (numeric)": roi,
        "Net Savings (numeric)": savings
    }

st.set_page_config(page_title="SmartPrint Simulation Model", layout="centered")

st.title("📊 3D Printing Simulation Efficiency Model")
st.caption("Real-time simulation of the ROI potential from adopting quantum/AI-based simulation tools like SmartPrint.")

# Sidebar Inputs
st.sidebar.header("🛠️ Simulation Parameters")
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

# Results Display
st.markdown("## 📈 Simulation Results Summary")
st.markdown("---")

st.markdown("### 🔧 Operational Metrics")
st.markdown(f"🖨️ **Total Print Jobs/Month:** `{results['Total Print Jobs/Month']}`")
st.markdown(f"📉 **Failure Rate (Before):** `{results['Failure Rate (Before)']}`")
st.markdown(f"📈 **Failure Rate (After):** `{results['Failure Rate (After)']}`")

st.markdown("### ⏱️ Time Lost to Failures")
st.markdown(f"⛔ **Labor Hours Lost (Before):** `{results['Labor Hours Lost (Before)']}`")
st.markdown(f"✅ **Labor Hours Lost (After):** `{results['Labor Hours Lost (After)']}`")

st.markdown("### 💸 Cost Breakdown")
st.markdown(f"🧱 **Material Cost Lost (Before):** `{results['Material Cost Lost (Before)']}`")
st.markdown(f"🪙 **Material Cost Lost (After):** `{results['Material Cost Lost (After)']}`")
st.markdown(f"💰 **Total Monthly Cost (Before):** `{results['Total Monthly Cost (Before)']}`")
st.markdown(f"💵 **Total Monthly Cost (After):** `{results['Total Monthly Cost (After)']}`")

st.markdown("### 📊 ROI & Savings")
st.markdown(f"🧠 **Simulation Tool Cost:** `{results['Simulation Tool Cost']}`")

# Emphasize Net Savings
savings_numeric = results["Net Savings (numeric)"]
roi_numeric = results["ROI (numeric)"]

if savings_numeric > 100000:
    st.markdown(f"🟢 **Net Savings:** <span style='color:limegreen;font-weight:bold;font-size:20px'>{results['Net Savings']}</span>", unsafe_allow_html=True)
else:
    st.markdown(f"**Net Savings:** {results['Net Savings']}")

if roi_numeric > 5:
    st.markdown(f"🚀 **ROI:** <span style='color:gold;font-weight:bold;font-size:20px'>{results['ROI (%)']}</span>", unsafe_allow_html=True)
else:
    st.markdown(f"**ROI:** {results['ROI (%)']}")

# Description
st.markdown("---")
st.markdown("## 🧠 What This Model Does")
st.markdown("""
This tool simulates inefficiencies in 3D printing — including labor and material losses from failed prints — and estimates the improvements from using simulation tools like SmartPrint.

✅ Adjust print volume, failure rates, labor costs, and simulation effectiveness  
📊 See projected cost reductions and ROI in real time  
💡 Use insights to support investment or research proposals
""")

# Takeaway
st.markdown("## 🔍 Key Takeaway")
if roi_numeric > 5:
    st.success("This model shows exceptionally high ROI. Quantum/AI simulation tools could significantly reduce costs and improve throughput.")
elif roi_numeric > 1:
    st.info("Strong case for adoption. The numbers show real operational gains with a solid return.")
elif roi_numeric > 0:
    st.warning("There's some efficiency gain, but ROI is modest. Consider improving simulation effectiveness or scaling scope.")
else:
    st.error("This scenario does not show a return. Recheck your inputs or test with different assumptions.")

# Chart
before_labor = float(results["Labor Hours Lost (Before)"]) * hourly_labor_cost
after_labor = float(results["Labor Hours Lost (After)"]) * hourly_labor_cost
before_material = float(results["Material Cost Lost (Before)"].replace('$','').replace(',',''))
after_material = float(results["Material Cost Lost (After)"].replace('$','').replace(',',''))

labels = ['Labor Cost', 'Material Cost']
before_costs = [before_labor, before_material]
after_costs = [after_labor, after_material]
x = range(len(labels))

fig, ax = plt.subplots()
ax.bar(x, before_costs, width=0.4, label='Before', align='center', color='tomato')
ax.bar([i + 0.4 for i in x], after_costs, width=0.4, label='After', align='center', color='mediumseagreen')
ax.set_xticks([i + 0.2 for i in x])
ax.set_xticklabels(labels)
ax.set_ylabel("Cost ($)")
ax.set_title("📉 Monthly Cost Comparison: Before vs After Simulation")
ax.legend()

st.pyplot(fig)
