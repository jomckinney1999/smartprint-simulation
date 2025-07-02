import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

# --- Model Function ---
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
        "Net Savings (numeric)": savings,
        "Labor Savings (numeric)": labor_cost_lost - new_labor_cost,
        "Material Savings (numeric)": material_cost_lost - new_material_cost
    }

# --- Page Setup ---
st.set_page_config(page_title="SmartPrint Simulation Model", layout="centered")
st.title("📊 3D Printing Simulation Efficiency Model")

# --- Overview Section ---
st.markdown("## 🧠 What This Model Does")
st.markdown("""
This simulation helps stakeholders understand how quantum or AI-driven simulation tools (like SmartPrint) could improve the efficiency of 3D printing operations.

It calculates:
- How much time and money are lost from failed print jobs
- How simulation tools can reduce those losses
- The resulting monthly cost savings and return on investment (ROI)

You can either **choose a preset scenario** (like a university lab or a manufacturing facility) or **customize the inputs** using the sliders on the left.
""")

# --- Use Case Presets ---
st.sidebar.markdown("### 🧭 Use Case Presets")
preset = st.sidebar.selectbox("Choose a use case:", [
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

# --- Input Sliders ---
st.sidebar.header("🎛️ Adjust Parameters")
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

# --- Output Summary ---
st.markdown("## 📈 Key Results")
st.write(f"🖨️ **Total Print Jobs/Month:** `{results['Total Print Jobs/Month']}`")
st.write(f"📉 **Failure Rate Before Simulation:** `{results['Failure Rate (Before)']}` → 📈 After: `{results['Failure Rate (After)']}`")
st.write(f"⏱️ **Labor Hours Lost:** `{results['Labor Hours Lost (Before)']}` → `{results['Labor Hours Lost (After)']}`")
st.write(f"🧱 **Material Cost Lost:** `{results['Material Cost Lost (Before)']}` → `{results['Material Cost Lost (After)']}`")
st.write(f"💰 **Monthly Cost Before Simulation:** `{results['Total Monthly Cost (Before)']}`")
st.write(f"💵 **Monthly Cost After Simulation:** `{results['Total Monthly Cost (After)']}`")
st.write(f"🧠 **Simulation Tool Cost:** `{results['Simulation Tool Cost']}`")

# --- ROI Highlights ---
roi_numeric = results["ROI (numeric)"]
savings_numeric = results["Net Savings (numeric)"]

if roi_numeric > 5:
    st.markdown(f"🚀 **ROI:** <span style='color:gold;font-weight:bold;font-size:22px'>{results['ROI (%)']}</span>", unsafe_allow_html=True)
else:
    st.write(f"ROI: {results['ROI (%)']}")

if savings_numeric > 100000:
    st.markdown(f"🟢 **Net Savings:** <span style='color:limegreen;font-weight:bold;font-size:22px'>{results['Net Savings']}</span>", unsafe_allow_html=True)
else:
    st.write(f"Net Savings: {results['Net Savings']}")

# --- Takeaway Message ---
st.markdown("## 🔍 Takeaway")
if roi_numeric > 5:
    st.success("✅ This scenario demonstrates exceptional ROI. Simulation is likely to deliver major cost and time savings.")
elif roi_numeric > 1:
    st.info("📈 There is a strong case for adopting simulation tools based on efficiency and ROI.")
elif roi_numeric > 0:
    st.warning("⚠️ Modest ROI. Consider increasing simulation effectiveness or reducing tool cost.")
else:
    st.error("❌ No return on investment. Reassess your parameters or test with a smaller pilot first.")

# --- Visuals: ROI Trend Line ---
st.markdown("## 📊 Visual Insights")
st.markdown("### ROI Growth vs. Simulation Effectiveness")
eff_levels = np.linspace(0.1, 0.9, 5)
roi_vals = [round((0.2 + eff * 2), 2) for eff in eff_levels]
fig1, ax1 = plt.subplots()
ax1.plot(eff_levels, roi_vals, marker='o', color='mediumblue')
ax1.set_xlabel("Simulation Effectiveness")
ax1.set_ylabel("Estimated ROI")
ax1.set_title("ROI Growth vs. Simulation Effectiveness")
ax1.grid(True)
buf1 = BytesIO()
fig1.savefig(buf1, format="png")
buf1.seek(0)
st.image(buf1)

# --- Visuals: Savings Breakdown Pie ---
st.markdown("### Savings Breakdown (Labor vs Material)")
fig2, ax2 = plt.subplots()
savings_data = [results["Labor Savings (numeric)"], results["Material Savings (numeric)"]]
labels = ['Labor Savings', 'Material Savings']
colors = ['lightgreen', 'lightskyblue']
ax2.pie(savings_data, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
ax2.axis('equal')
ax2.set_title("Savings Distribution")
buf2 = BytesIO()
fig2.savefig(buf2, format="png")
buf2.seek(0)
st.image(buf2)

st.markdown("---")
st.caption("🔎 *Note: All results are based on approximated input values and simulation logic. They are intended for exploratory and illustrative purposes only.*")

