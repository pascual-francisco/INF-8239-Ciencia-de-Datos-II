# INF-8239 · Unidad 04 · Gobernanza y DSS responsable

## LAB11 – Evaluación de Impacto Ético
## LAB12 – Auditoría de Equidad con Fairlearn

**Autor:** Francisco Pascual  
**Asignatura:** INF-8239 Ciencia de Datos II  
**Unidad:** 04 – Ética y Roles en Ciencia de Datos

---

# Introducción

La creciente adopción de sistemas de apoyo a decisiones basados en datos requiere mecanismos de evaluación que permitan validar no solo el desempeño técnico de los modelos, sino también sus implicaciones éticas, de gobernanza y de equidad.

Durante los laboratorios LAB11 y LAB12 se realizó una evaluación integral de un sistema de apoyo a decisiones utilizando un enfoque alineado con principios de gestión de riesgos, auditoría de equidad y gobernanza de inteligencia artificial. El trabajo incluyó la identificación de riesgos, el análisis de partes interesadas, la documentación de controles y la evaluación comparativa de modelos predictivos considerando desempeño, equidad y costo computacional.

---

# LAB11 – Evaluación de Impacto Ético

## Propósito del Sistema

El sistema tiene como finalidad apoyar la priorización de territorios para intervenciones preventivas y asignación eficiente de recursos, proporcionando recomendaciones basadas en información histórica.

## Partes Interesadas

| Actor | Beneficio | Riesgo Potencial |
|---------|---------|---------|
| Personas afectadas | Mejor asignación de recursos | Clasificación incorrecta |
| Operadores | Mayor eficiencia en decisiones | Dependencia excesiva del sistema |
| Propietario institucional | Mejor planificación | Riesgo reputacional y regulatorio |
| Equipo de datos | Mejora continua del modelo | Responsabilidad por sesgos o errores |

## Riesgos Identificados

Se documentaron ocho riesgos principales:

1. Sesgo sistemático en la clasificación de territorios.
2. Clasificación incorrecta de territorios prioritarios.
3. Uso de datos desactualizados.
4. Acceso no autorizado a información sensible.
5. Interpretación incorrecta de resultados.
6. Uso fuera del propósito autorizado.
7. Dependencia excesiva de recomendaciones automatizadas.
8. Incumplimiento regulatorio.

## Riesgos Prioritarios

### R02 – Clasificación incorrecta de territorios prioritarios

Este riesgo obtuvo la prioridad más alta debido al impacto potencial sobre la asignación de recursos y la atención de necesidades críticas.

### R01 – Sesgo sistemático en la clasificación de territorios

La presencia de sesgos podría afectar la distribución equitativa de recursos y generar desigualdades entre grupos o territorios.

### R07 – Dependencia excesiva de recomendaciones automatizadas

Existe el riesgo de disminuir la supervisión humana y confiar excesivamente en las recomendaciones del sistema.

## Alternativa No Predictiva

Como alternativa se documentó el uso de criterios definidos por expertos y revisiones periódicas sin modelos predictivos.

## Mecanismo de Apelación

Las decisiones derivadas del sistema pueden ser revisadas mediante un proceso formal de revisión humana.

## Condición de Retiro

El sistema deberá retirarse si:

- Se detectan sesgos significativos.
- Existen incumplimientos regulatorios.
- El desempeño se degrada de forma sostenida.
- Se identifica daño relevante asociado al uso del sistema.

---

# Registro de Riesgos y NIST AI RMF

La evaluación incorporó elementos alineados con NIST AI RMF:

- **GOVERN:** Definición de propietario y responsabilidades.
- **MAP:** Identificación de riesgos y grupos afectados.
- **MEASURE:** Evaluación mediante métricas y auditorías.
- **MANAGE:** Controles, monitoreo y criterios de retiro.

Los riesgos fueron documentados con:

- Escenario.
- Persona o grupo afectado.
- Probabilidad.
- Impacto.
- Control.
- Responsable.
- Evidencia.
- Riesgo residual.

---

# LAB12 – Auditoría de Equidad con Fairlearn

## Comprensión del Dataset

### Distribución de la Variable Objetivo

La variable objetivo presenta una distribución relativamente balanceada:

- Positivos: 55.2 %
- Negativos: 44.8 %

Aunque existe balance entre clases, el accuracy por sí solo puede ocultar diferencias importantes entre grupos.

### Tamaño por Grupo

- G1: 396 observaciones
- G2: 244 observaciones

Ambos grupos poseen suficiente representación para comparaciones generales.

### Corte Temporal

El entrenamiento finaliza el 24/09/2026 y la prueba inicia el 25/09/2026.

Este enfoque evita utilizar información futura para evaluar eventos pasados y reduce la posibilidad de fuga de información (data leakage).

### Variables Excluidas

Se excluyeron:

- case_id
- received_date
- protected_group
- target

Aunque el atributo sensible no participa en el entrenamiento, esto no elimina automáticamente la posibilidad de sesgos indirectos.

---

# Resultados del Modelo Logistic Regression

## Métricas Globales

| Métrica | Valor |
|----------|----------|
| Accuracy | 0.719 |
| Recall | 0.717 |
| Precision | 0.776 |
| FPR | 0.279 |
| Selection Rate | 0.531 |

## Métricas por Grupo

### Grupo G1

- Count: 101
- Accuracy: 0.703
- Recall: 0.653
- FPR: 0.250
- Selection Rate: 0.446

### Grupo G2

- Count: 59
- Accuracy: 0.746
- Recall: 0.791
- FPR: 0.375
- Selection Rate: 0.678

## Interpretación

Se observan diferencias entre grupos en métricas relevantes como recall y tasa de selección. El grupo G2 presenta mayor recall, pero también una tasa de falsos positivos más elevada.

Estas diferencias requieren análisis adicional antes del despliegue, pero no constituyen evidencia suficiente para afirmar discriminación causal.

---

# Análisis Interseccional

Se identificaron grupos con bajo soporte:

- G2 | 45-59 → 8 observaciones
- G2 | 18-29 → 11 observaciones
- G2 | 30-44 → 14 observaciones

Debido al número reducido de observaciones, las métricas obtenidas para estos grupos pueden ser inestables.

Por este motivo, cualquier diferencia observada debe interpretarse con cautela y validarse mediante datos adicionales.

---

# Comparación de Modelos

## Logistic Regression

- Accuracy global: 0.719
- Tiempo de entrenamiento: 0.044 s
- Tamaño del modelo: 3.56 KB

## Decision Tree

- Accuracy global similar
- Tiempo de entrenamiento: 0.040 s
- Tamaño del modelo: 7.90 KB

## Trade-off Observado

El árbol de decisión mostró mejoras limitadas en algunas métricas, pero incrementó:

- La complejidad del modelo.
- El tamaño serializado.
- Algunas tasas de falsos positivos.

La mejora observada no compensa claramente el aumento de complejidad.

---

# Green AI

Desde una perspectiva de Green AI, Logistic Regression representa la opción más eficiente debido a:

- Menor tamaño del modelo.
- Menor complejidad.
- Desempeño comparable o superior.
- Menor costo de mantenimiento.

Por estas razones se considera la alternativa más adecuada para un despliegue inicial.

---

# Brechas Observadas y Discriminación Causal

Las diferencias observadas entre grupos constituyen indicadores que requieren investigación adicional.

Sin embargo, una brecha en métricas como recall, tasa de selección o falsos positivos no demuestra por sí sola la existencia de discriminación causal.

Las diferencias pueden estar influenciadas por:

- Distribución desigual de datos.
- Calidad de la información disponible.
- Variables correlacionadas.
- Tamaño de muestra reducido.

Por esta razón, las métricas de equidad deben utilizarse como herramientas de monitoreo y evaluación, no como evidencia concluyente de discriminación.

---

# Obligación Legal, Marco Voluntario y Recomendación Ética

## Obligación Legal

Cumplir con los requisitos aplicables de privacidad, protección de datos y trazabilidad de decisiones.

## Marco Voluntario

Aplicar las recomendaciones del NIST AI RMF para gobernanza, evaluación y gestión de riesgos.

## Recomendación Ética

Mantener supervisión humana, mecanismos de apelación, monitoreo de equidad y auditorías periódicas del sistema.

---

# Decisión Final

## DESPLEGAR CON CONTROLES Y MONITOREO

Se recomienda utilizar Logistic Regression como modelo base debido a que ofrece el mejor equilibrio entre:

- Desempeño.
- Equidad observada.
- Simplicidad.
- Transparencia.
- Eficiencia computacional.

El despliegue debe mantenerse sujeto a:

- Revisión humana obligatoria.
- Monitoreo continuo.
- Auditorías periódicas.
- Condiciones de retiro previamente documentadas.

---

# Reproducción del Proyecto y Evidencias

**Repositorio público:**

https://github.com/pascual-francisco/INF-8239-Ciencia-de-Datos-II

## Preparación del Entorno

### 1. Clonar repositorio

```bash
git clone https://github.com/pascual-francisco/INF-8239-Ciencia-de-Datos-II.git
```

### 2. Abrir Google Colab

### 3. Navegar hasta:

```text
INF-8239-Ciencia-de-Datos-II/
└── Unit_04_Data_Science_Ethics
```

### 4. Ejecutar las celdas del notebook en el orden documentado.

---

## Secuencia de Ejecución

### LAB11

```bash
uv run python scripts/lab11_impact.py
uv run pytest -q tests/test_impact.py tests/test_privacy.py
```

### LAB12

```bash
uv run python scripts/describe_dataset.py

uv run python scripts/lab12_audit.py --model logistic

uv run python scripts/lab12_audit.py --model tree

uv run python scripts/validate_lab12_decision.py

uv run pytest -q tests/test_fairness.py tests/test_model.py
```

---

## Evidencias Incluidas

- Archivos YAML completados.
- Registro de riesgos.
- Stakeholders documentados.
- Auditoría de equidad.
- Comparación de modelos.
- Resultados de pruebas automatizadas.
- Evidencia de gobernanza y NIST AI RMF.
- Artefactos editables generados durante los laboratorios.

---

# Declaración de Uso de Inteligencia Artificial

Se utilizaron herramientas de inteligencia artificial generativa como apoyo para comprender instrucciones, estructurar la documentación técnica, revisar consistencia de resultados y mejorar la redacción del informe.

Todas las decisiones, interpretaciones, análisis de riesgos, verificaciones de resultados, selección de controles, comparación de modelos y conclusiones finales fueron revisadas y validadas manualmente por el estudiante antes de la entrega.

Ninguna evidencia experimental, métrica, resultado o conclusión fue inventada ni utilizada sin verificación previa.

Sí. Te recomiendo integrarlo en ese mismo documento en lugar de tener otro informe separado. Solo añadiría las secciones de LAB13 después de "Decisión Final" y antes de "Reproducción del Proyecto y Evidencias".

LAB13 – Gobernanza y DSS Responsable
Matriz RACI

Como parte de la gobernanza del DSS se definieron responsabilidades mediante una matriz RACI para asegurar la trazabilidad de las decisiones y la separación entre ejecución técnica y aprobación organizacional.

La calidad de los datos quedó bajo responsabilidad del Data Engineer, mientras que la aprobación final corresponde al Product Owner. La validación del modelo quedó asignada al Data Scientist con aprobación del Product Owner. El despliegue es responsabilidad del ML Engineer, manteniendo al Product Owner como responsable final de la liberación.

La respuesta ante incidentes quedó bajo la ejecución del ML Engineer y la responsabilidad final del Institutional Owner. Esta estructura garantiza que cada actividad cuente con exactamente un responsable final (Accountable) y al menos un ejecutor directo (Responsible).

Política de Gobernanza

El sistema fue configurado mediante una política formal de gobernanza que establece límites de uso, controles de privacidad y puertas de calidad para el despliegue.

Los usos prohibidos incluyen intervenciones automáticas, decisiones de elegibilidad y declaraciones de emergencia. Asimismo, el sistema reconoce como atributos sensibles las variables protected_group y age_band, utilizadas únicamente para auditoría de equidad.

Se definieron umbrales mínimos para desempeño y equidad, incluyendo un recall mínimo de 0.68, una brecha máxima de recall de 0.16, una brecha máxima de FPR de 0.16, una latencia máxima de 500 ms y un tamaño máximo de modelo de 1024 KB.

Estas condiciones constituyen las puertas de gobernanza que deben superarse antes de autorizar cualquier despliegue.

Resultado de la Evaluación de Gobernanza

Se ejecutó el pipeline de gobernanza para validar desempeño, equidad, latencia y eficiencia computacional utilizando las puertas definidas en la política del sistema.

El resultado final fue GO, indicando que todas las verificaciones fueron aprobadas satisfactoriamente. El modelo cumplió con el recall mínimo requerido, mantuvo las brechas de equidad dentro de los límites permitidos y permaneció muy por debajo del tamaño máximo autorizado.

No se registraron verificaciones fallidas durante la evaluación. Sin embargo, la gobernanza mantiene la necesidad de una revisión humana final antes de cualquier despliegue operativo.

Arquitectura del DSS Gobernado

La arquitectura implementada se compone de seis capas principales.

La capa de datos es responsable de validar contratos de datos, procedencia, exclusión de identificadores directos y control del corte temporal. La capa de modelo proporciona predicciones reproducibles mediante Logistic Regression como alternativa seleccionada.

La capa de equidad evalúa métricas desagregadas por grupos protegidos e intersecciones utilizando Fairlearn. Para los grupos con soporte reducido se documentaron advertencias específicas para evitar interpretaciones incorrectas.

La capa Green AI justifica la elección del modelo mediante una comparación entre calidad predictiva, complejidad computacional, tiempo de entrenamiento y tamaño serializado.

La capa DSS transforma las predicciones en recomendaciones explicables para revisión humana, proporcionando evidencia, métricas y criterios de decisión.

Finalmente, la capa de gobernanza integra responsables, monitoreo, auditorías, mecanismos de apelación, respuesta a incidentes y procedimientos de despliegue controlado.

Simulacro de Incidente

Se ejecutó un simulacro de incidente para validar la capacidad de respuesta del DSS ante una desviación de equidad.

El escenario simulado correspondió a una brecha de recall superior al límite permitido. La condición fue detectada mediante los mecanismos de monitoreo y generó una recomendación de tipo REVIEW manteniendo disponible un baseline seguro.

Como parte de la contención se preservaron reportes, métricas y versiones del modelo para permitir la investigación posterior. La comunicación fue dirigida al Product Owner, ML Engineer e Institutional Owner siguiendo la matriz RACI definida para el proyecto.

Posteriormente se documentaron acciones correctivas orientadas a revisar métricas de equidad, revalidar las puertas de gobernanza y actualizar la documentación asociada. El simulacro confirmó la disponibilidad de procedimientos formales para detección, contención, preservación de evidencia, comunicación, rollback y análisis posterior.

Model Card y Runbook

Se elaboró un Model Card para documentar el propósito del modelo, usuarios previstos, métricas de desempeño, resultados de equidad, riesgos identificados, limitaciones conocidas y mecanismos de supervisión humana.

Adicionalmente se desarrolló un Runbook que describe los procedimientos de respuesta ante incidentes, incluyendo clasificación, comunicación, contención, recuperación, rollback y postmortem. Ambos documentos constituyen artefactos de gobernanza necesarios para auditorías y revisiones posteriores.

Validación Final del DSS

Como etapa final se ejecutó la batería completa de pruebas del proyecto.

Las pruebas incluyeron validaciones de contratos de datos, privacidad, equidad, gobernanza, DSS y funcionamiento de Streamlit sin navegador.

El resultado obtenido fue:

10 passed in 6.69s


Este resultado confirma que el sistema cumple los requisitos técnicos y de gobernanza definidos para la Unidad 04.

Decisión Final Integrada

Considerando los resultados obtenidos en LAB11, LAB12 y LAB13, se recomienda desplegar el DSS con controles y monitoreo continuo.

La evaluación de impacto identificó riesgos gestionables mediante controles documentados. La auditoría de equidad mostró un desempeño global aceptable y diferencias entre grupos que deben mantenerse bajo monitoreo. Las puertas de gobernanza fueron aprobadas satisfactoriamente y el simulacro de incidente validó la capacidad de respuesta del sistema.

El DSS mantiene explícitamente la supervisión humana obligatoria, el monitoreo continuo de métricas, auditorías periódicas y mecanismos documentados para respuesta ante incidentes. Estas condiciones permiten un uso responsable del sistema dentro del alcance definido para el proyecto.




