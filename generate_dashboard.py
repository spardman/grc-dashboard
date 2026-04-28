import plotly.graph_objects as go
import pandas as pd

# Mock GRC Maturity Data
data = {
    'Control': ['Access Control', 'Audit/Log', 'IR Plan', 'Risk Assessment', 'MFA'],
    'Status': [85, 40, 95, 60, 100]
}
df = pd.DataFrame(data)

# Build the chart
fig = go.Figure(go.Bar(
    x=df['Control'], 
    y=df['Status'],
    marker_color=['green', 'red', 'green', 'orange', 'green']
))

fig.update_layout(title="Company X: Compliance Maturity Score (%)", template="plotly_dark")

# Save the file
fig.write_html("index.html")
print("--- Dashboard Generated Successfully! ---")
