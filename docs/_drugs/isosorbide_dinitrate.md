---
layout: default
title: Isosorbide Dinitrate
parent: Solo Predicción del Modelo (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Isosorbide Dinitrate: nueva indicación predicha, Alopecia (nivel de evidencia L5). Indicación original: Dinitrato de isosorbida"
---

# Isosorbide Dinitrate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Dinitrato de isosorbida: De Indicación Cardiovascular Registrada a Alopecia

## Resumen en Una Frase

El dinitrato de isosorbida es un vasodilatador (donador de óxido nítrico). Está registrado en Colombia como tableta sublingual (Isocord®), pero el registro no detalla la indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **alopecia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dinitrato de isosorbida (el registro sanitario no especifica la indicación) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, el dinitrato de isosorbida es un nitrato orgánico que libera óxido nítrico (NO), activa la guanilato ciclasa y eleva el GMP cíclico, lo que relaja el músculo liso vascular. Su eficacia como vasodilatador en enfermedad cardiovascular está establecida, y mecanísticamente podría ser aplicable a la alopecia solo de forma hipotética.

La hipótesis plausible, pero no demostrada, es que la vasodilatación podría mejorar la microcirculación del cuero cabelludo alrededor de los folículos pilosos. No hay ensayos ni literatura que respalden esta idea. El puntaje alto del modelo podría reflejar también cercanía en la red de conocimiento con otras enfermedades del cabello, más que una relación biológica real.

---

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 37246 (cancelado) | ISOCORD® SUBLINGUAL | Tableta sublingual | Dinitrato de isosorbida |

El único registro es de Laboratorios Bagó de Colombia S.A.S. y está cancelado, por lo que actualmente no hay producto vigente con este registro.

---

## Consideraciones de Seguridad

Los datos del prospecto (advertencias y contraindicaciones) no estaban disponibles. Consultar el prospecto para esa información.

- **Contraindicaciones o condiciones de precaución según el grafo de conocimiento (TxGNN/PrimeKG, no texto de prospecto)**: hipotensión, miocardiopatía hipertrófica, acetilación lenta, enfermedad arterial coronaria, accidente cerebrovascular y trastornos cerebrovasculares, infarto cerebral, infarto de miocardio, trombosis coronaria, hemoglobinopatía, anemia (incluida la macrocítica), hipertiroidismo, enfermedad de Graves, tirotoxicosis, pseudotumor cerebral, hipertensión intracraneal, hemorragia intracerebral y síndrome de Rowell.
- **Interacciones farmacológicas**: se identificaron 141 interacciones. Entre las principales (nivel moderado) están bupropión, morfina, opio, dronabinol, nabilona, sapropterina, rosiglitazona y los inhibidores SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina). El omeprazol figura como interacción menor.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para alopecia es de nivel L5: no hay ensayos clínicos ni literatura que la respalden. Además, el único registro sanitario en Colombia está cancelado y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Realizar estudios preclínicos o piloto sobre microcirculación folicular que sustenten la hipótesis.
- Evaluar la viabilidad de una vía tópica o local, ya que la forma disponible (sublingual) no es adecuada para esta indicación, y considerar el riesgo de hipotensión sistémica.
- Priorizar otras predicciones del modelo con más respaldo:
  - **Hipertensión pulmonar** (L3): 20 publicaciones, principalmente estudios hemodinámicos pequeños, sin ensayos registrados.
  - **Enfermedad vascular** (L2): incluye un ensayo de Fase 3 completado con aerosol de dinitrato de isosorbida en úlceras de pie diabético (NCT02789033, n=68), cuyos resultados no estaban disponibles.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

