# SmartPrint: Simulation + Analytics for 3D Printing Efficiency (GigEfx Laboratories)

**Live demo (Streamlit):** https://smartprint-simulation-8bznxcpjkrofu4vp9sc52p.streamlit.app/

## What this is
SmartPrint is an end-to-end analytics + decision-support project built for **GigEfx Laboratories** (via a Riipen industry partnership).  
The goal was to quantify and reduce **time, cost, and throughput losses** from failed/inefficient 3D prints by combining:

- **An interactive Streamlit simulation model** (scenario + sensitivity testing)
- **A Tableau dashboard** (sub-issue analytics & executive visuals)
- **A written business case** (problem framing, value hypothesis, and recommendations)
- **A final presentation** (stakeholder-ready narrative)

> Recruiter-friendly takeaway: this repo shows how we translated a messy operations problem into a data product (dashboard + model) and a business recommendation.

---

## Problem (business framing)
3D printing workflows can suffer from:
- print failures and rework
- long print cycles with low effective throughput
- material waste and avoidable labor time
- uncertainty around whether simulation tools are worth adopting (ROI, break-even, payback)

**GigEfx asked:** *“If we adopt simulation-driven process improvements, what is the expected impact on failures, time-to-part, and cost? And where are the biggest inefficiency drivers?”*

---

## Solution (what we built)

### 1) Streamlit simulation model
A web app that lets stakeholders test scenarios (e.g., changing failure rates, cycle times, costs) and see estimated outcomes such as:
- expected time saved
- expected cost savings
- ROI / payback logic (where applicable)
- sensitivity to key assumptions

**Demo:** https://smartprint-simulation-8bznxcpjkrofu4vp9sc52p.streamlit.app/

> Add screenshots in `/assets/streamlit/` and they’ll render here:
>
> ![Streamlit Screenshot](assets/streamlit/streamlit_overview.png)

### 2) Tableau dashboard (sub-issue analytics)
An executive-friendly set of visuals to explore the major “sub-issues” behind inefficiency (failure-related time loss, cost drivers, adoption trade-offs, etc.).

> Add screenshots in `/assets/tableau/`:
>
> ![Tableau Screenshot](assets/tableau/dashboard_overview.png)

### 3) Business case + presentation
A stakeholder narrative connecting the analytics to a recommendation:
- problem context
- options considered
- economic logic & assumptions
- implementation roadmap and risks

---

## Tech stack
- **Python:** pandas, numpy
- **App:** Streamlit
- **Analytics/BI:** Tableau
- **Documentation:** Markdown (GitHub), PDF/Slides, screenshots

---

## Repo structure (recommended)
```
.
├── README.md
├── docs/
│   ├── Case_Study.md
│   ├── Model_Methodology.md
│   ├── Dashboard.md
│   └── How_to_Run.md
├── app/                      # (optional) Streamlit source, if you include it
│   ├── streamlit_app.py
│   └── requirements.txt
├── assets/
│   ├── streamlit/
│   └── tableau/
└── deliverables/
    ├── SmartPrint_Presentation.pdf
    ├── Business_Case.docx
    └── SmartPrint_Tableau_Dashboard.twbx
```

---

## How to run locally (if you include the app code)
1) Create an environment
```bash
python -m venv .venv
source .venv/bin/activate  # (Windows) .venv\Scripts\activate
```

2) Install dependencies
```bash
pip install -r app/requirements.txt
```

3) Run Streamlit
```bash
streamlit run app/streamlit_app.py
```

---

## Results (how to present this on a resume)
Use outcome language even if numbers are scenario-based:

- Built an interactive simulation app to quantify how operational changes impact **3D print failures, throughput, and cost**
- Designed a Tableau dashboard to visualize **root causes and drivers of inefficiency** across key sub-issues
- Delivered a stakeholder-ready business case and presentation with **implementation roadmap and ROI framing**

See: **docs/Case_Study.md**

---

## Screenshots (fast instructions)
- Put Streamlit screenshots in: `assets/streamlit/`
- Put Tableau screenshots in: `assets/tableau/`
- Keep file names consistent with the README image links.

See: **assets/README.md**

---

## Acknowledgements
Developed as part of a Riipen industry project in partnership with **GigEfx Laboratories**.
