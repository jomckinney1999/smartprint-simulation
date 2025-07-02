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

# Streamlit layout
st.set_page_config(page_title="SmartPrint Simulation Model", layout="centered")
st.title("📊 3D Printing Simulation Efficiency Model")
st.caption("Explore how simulation tools can reduce failures, save costs, and improve ROI in real-world 3D printing workflows.")

# --- Preset Use Cases ---
st.sidebar.markdown("### 🧭 Use Case Presets")
preset = st.sidebar.selectbox("Choose a realistic use case to explore:", [
    "Customize your own inputs", 
    "University Lab (Standard Usage)", 
    "Manufacturing Facility (High Volume)", 
    "Startup R&D Team (Small-Scale Pilot)"
])

defaults = {
    "printer_count": 10,
    "jobs_per_printer_per_week": 20,
    "failure_rate": 0.15,
    "time_lost_per_failure": 2.0,
    "hourly_labor_cost": 30,
    "material_waste_cost": 15,
    "simulation_effectiveness": 0.5,
    "simulation_tool_cost": 1000
}

if preset == "University Lab (Standard Usage)":
    defaults.update({
        "printer_count": 5,
        "jobs_per_printer_per_week": 25,
        "failure_rate": 0.18,
        "time_lost_per_failure": 1.5,
        "hourly_labor_cost": 40,
        "material_waste_cost": 12,
        "simulation_effectiveness": 0.4,
        "simulation_tool_cost": 500
    })
elif preset == "Manufacturing Facility (High Volume)":
    defaults.update({
        "printer_count": 25,
        "jobs_per_printer_per_week": 60,
        "failure_rate": 0.12,
        "time_lost_per_failure": 3.0,
        "hourly_labor_cost": 35,
        "material_waste_cost": 20,
        "simulation_effectiveness": 0.6,
        "simulation_tool_cost": 5000
    })
elif preset == "Startup R&D Team (Small-Scale Pilot)":
    defaults.update({
        "printer_count": 2,
        "jobs_per_printer_per_week": 10,
        "failure_rate": 0.25,
        "time_lost_per_failure": 1.0,
        "hourly_labor_cost": 25,
        "material_waste_cost": 10,
        "simulation_effectiveness": 0.3,
        "simulation_tool_cost": 300
    })

# --- Simulation Sliders ---
st.sidebar.header("🎛️ Fine-tune Parameters")
printer_count = st.sidebar.slider("Number of Printers", 1, 50, defaults["printer_count"])
jobs_per_printer_per_week = st.sidebar.slider("Jobs per Printer per Week", 1, 100, defaults["jobs_per_printer_per_week"])
failure_rate = st.sidebar.slider("Failure Rate (%)", 0.0, 1.0, defaults["failure_rate"])
time_lost_per_failure = st.sidebar.slider("Time Lost per Failure (hrs)", 0.0, 10.0, defaults["time_lost_per_failure"])
hourly_labor_cost = st.sidebar.slider("Hourly Labor Cost ($)", 10, 200, defaults["hourly_labor_cost"])
material_waste_cost = st.sidebar.slider("Material Cost per Failure ($)", 1, 100, defaults["material_waste_cost"])
simulation_effectiveness = st.sidebar.slider("Simulation Effectiveness (%)", 0.0, 1.0, defaults["simulation_effectiveness"])
simulation_tool_cost = st.sidebar.slider("Monthly Simulation Tool Cost ($)", 0, 10000, defaults["simulation_tool_cost"])

# --- Run Simulation ---
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

# --- Display Results ---
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

if results["Net Savings (numeric)"] > 100000:
    st.markdown(f"🟢 **Net Savings:** <span style='color:limegreen;font-weight:bold;font-size:20px'>{results['Net Savings']}</span>", unsafe_allow_html=True)
else:
    st.markdown(f"**Net Savings:** {results['Net Savings']}")

if results["ROI (numeric)"] > 5:
    st.markdown(f"🚀 **ROI:** <span style='color:gold;font-weight:bold;font-size:20px'>{results['ROI (%)']}</span>", unsafe_allow_html=True)
else:
    st.markdown(f"**ROI:** {results['ROI (%)']}")

# --- Description ---
st.markdown("---")
st.markdown("## 🧠 What This Model Does")
st.markdown("""
This simulation estimates the time, cost, and resource impact of failed 3D print jobs in real-world workflows.  
It models how simulation tools like SmartPrint can reduce these inefficiencies — giving you real-time insights on ROI, labor savings, and material waste reduction.
""")

# --- Takeaway ---
st.markdown("## 🔍 Key Takeaway")
roi_numeric = results["ROI (numeric)"]
if roi_numeric > 5:
    st.success("✅ Simulation tools offer massive cost and time savings — a strong business case for adoption.")
elif roi_numeric > 1:
    st.info("📈 This shows a promising return on investment. Worth piloting or scaling.")
elif roi_numeric > 0:
    st.warning("⚠️ Limited efficiency gains. Consider adjusting parameters or simulation scope.")
else:
    st.error("❌ This configuration doesn’t show value. Try a different scenario or input.")

# --- Bar Chart: Labor & Material Cost Before/After ---
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
ax.bar([i +]()
