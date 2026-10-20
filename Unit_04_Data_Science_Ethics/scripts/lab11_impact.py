import json
from pathlib import Path

import pandas as pd
import yaml

from inf8239_u04.impact import validate_impact, score_risks

# -----------------------------------------------------------------------------
# Crear carpeta de salida
# -----------------------------------------------------------------------------
out = Path("reports/lab11")
out.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# Cargar y validar evaluación de impacto
# -----------------------------------------------------------------------------
impact = yaml.safe_load(
    Path("student_inputs/lab11_impact.yml").read_text(
        encoding="utf-8"
    )
)

validate_impact(impact)

# -----------------------------------------------------------------------------
# Cargar y validar stakeholders
# -----------------------------------------------------------------------------
stake = pd.read_csv("student_inputs/stakeholders.csv")

if stake.astype(str).apply(
    lambda s: s.str.contains("REPLACE")
).any().any():
    raise ValueError("Complete stakeholders.csv")

# -----------------------------------------------------------------------------
# Cargar, validar y puntuar riesgos
# -----------------------------------------------------------------------------
risks = score_risks(
    pd.read_csv("student_inputs/risk_register.csv")
)

# -----------------------------------------------------------------------------
# Guardar evidencia
# -----------------------------------------------------------------------------
risks.to_csv(
    out / "risk_register_scored.csv",
    index=False
)

stake.to_csv(
    out / "stakeholders.csv",
    index=False
)

(out / "rmf_summary.json").write_text(
    json.dumps(
        {
            "GOVERN": "owner and policy",
            "MAP": f"{len(risks)} documented risks",
            "MEASURE": "LAB12 pending",
            "MANAGE": "withdrawal and appeal documented"
        },
        indent=2
    ),
    encoding="utf-8"
)

# -----------------------------------------------------------------------------
# Crear plantilla para el registro de decisión
# -----------------------------------------------------------------------------
(out / "DECISION_RECORD.md").write_text(
    """# Decision record

REPLACE with evidence, uncertainty, owner and GO/REVIEW/STOP.
""",
    encoding="utf-8"
)

# -----------------------------------------------------------------------------
# Mostrar riesgos prioritarios
# -----------------------------------------------------------------------------
print("\nTop 3 riesgos prioritarios:\n")

print(
    risks[
        ["id", "priority", "owner"]
    ]
    .sort_values(
        by="priority",
        ascending=False
    )
    .head(3)
    .to_string(index=False)
)