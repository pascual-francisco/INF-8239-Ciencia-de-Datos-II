from datetime import datetime, timezone
from pathlib import Path

text = f"""# Incident simulation

- detected_at: {datetime.now(timezone.utc).isoformat()}
- signal: recall gap exceeded
- containment: REVIEW and safe baseline
- evidence: preserved report and model version
- communication: Product Owner, ML Engineer and Institutional Owner notified
- corrective actions, owners and dates:
  - Review fairness metrics | Owner: Data Scientist | Due: Next review cycle
  - Validate governance gates | Owner: ML Engineer | Due: Next review cycle
  - Update documentation and approval record | Owner: Product Owner | Due: Next review cycle
"""

path = Path("reports/lab13/INCIDENT_POSTMORTEM.md")
path.parent.mkdir(parents=True, exist_ok=True)

path.write_text(
    text,
    encoding="utf-8"
)

print(path)