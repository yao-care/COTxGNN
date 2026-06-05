---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 3
---

# Cobicistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# COBICISTAT: De Potenciador Farmacocinético (HIV) a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Cobicistat es un inhibidor de CYP3A utilizado exclusivamente como potenciador farmacocinético en combinaciones antirretrovirales para el tratamiento del VIH en humanos, sin actividad antiviral propia.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Inmunodeficiencia Adquirida Felina (FIV)**,
sin embargo, esta predicción cuenta con **0 ensayos clínicos** y **0 publicaciones** que la respalden, configurándose como una señal de baja confiabilidad generada por similitud estructural en el grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrado en Colombia (uso como booster PK en combinaciones anti-VIH) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información disponible en la rationale del modelo, cobicistat es un inhibidor potente de CYP3A que actúa como potenciador farmacocinético (*booster*) dentro de combinaciones antirretrovirales (por ejemplo, combinado con elvitegravir, darunavir o atazanavir). Su efecto no es antiviral directo, sino que incrementa la exposición plasmática de los fármacos co-administrados al inhibir su metabolismo hepático e intestinal.

La conexión propuesta por TxGNN entre cobicistat y el FIV descansa en que el virus de inmunodeficiencia felina (FIV) pertenece a la misma familia que el VIH (lentivirus, retroviridae), lo que genera alta similitud de nodos en el grafo de conocimiento. Si en un hipotético esquema de tratamiento felino se utilizaran antirretrovirales metabolizados por CYP3A, cobicistat podría actuar como booster de forma análoga a su uso en VIH humano.

Sin embargo, esta inferencia es indirecta y altamente especulativa: cobicistat carece de actividad antiviral intrínseca contra FIV, no existen datos farmacocinéticos en especies felinas, y la indicación corresponde a medicina veterinaria y no a una indicación humana. La puntuación elevada (99.92%) refleja muy probablemente un artefacto del grafo de conocimiento por compartir representaciones vectoriales con nodos de VIH, no una predicción clínicamente trasladable.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para cobicistat en ninguna de las tres indicaciones predichas.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para cobicistat en ninguna de las tres indicaciones predichas.

---

## Información de Mercado en Colombia

Cobicistat no cuenta con registro sanitario en Colombia. No se encontraron licencias aprobadas en la base de datos consultada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las tres indicaciones predichas por TxGNN para cobicistat son clasificadas como L5 (solo predicción del modelo, sin ningún estudio real de respaldo), y la indicación principal (síndrome de inmunodeficiencia adquirida felina) corresponde a una enfermedad veterinaria sin aplicabilidad directa en humanos. Adicionalmente, cobicistat no tiene registro en Colombia y carece de actividad antiviral propia, lo que reduce sustancialmente el valor traslacional de estas predicciones.

**Para reconsiderar la decisión se necesita:**
- Confirmar el mecanismo de acción completo (MOA) desde DrugBank para identificar posibles vías de reposicionamiento en humanos
- Consultar las indicaciones aprobadas globalmente (EMA, FDA) para enriquecer el contexto de uso real
- Evaluar si existen otras indicaciones predichas en el ranking completo de TxGNN con mayor plausibilidad biológica en humanos y al menos evidencia L3 o superior
- Obtener datos de seguridad (advertencias, contraindicaciones, interacciones) desde el prospecto TFDA o ficha técnica EMA antes de cualquier evaluación posterior
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

