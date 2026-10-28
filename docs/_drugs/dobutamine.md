---
layout: default
title: Dobutamine
parent: Solo Predicción del Modelo (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Dobutamine: nueva indicación predicha, Alopecia (nivel de evidencia L5). Indicación original: DOBUTAMINA"
monitor_inn: "dobutamine"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "headache disorder", "hypertrichosis (disease)", "migraine disorder"]
---

# Dobutamine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Dobutamina: De Dobutamina (indicación registrada) a Alopecia
{: .text-alpha }

## Resumen en Una Frase

La dobutamina es un agonista adrenérgico beta-1 de uso intravenoso, registrado en Colombia bajo la indicación genérica "dobutamina" (sin texto de indicación detallado).
El modelo TxGNN predice que podría ser efectiva para **alopecia**, pero no hay ensayos clínicos y solo existe **1 publicación** (un reporte veterinario de intoxicación por minoxidil en un gato), que no respalda esta dirección.
La predicción se considera un artefacto del modelo TxGNN (aprendizaje profundo), no una hipótesis farmacológica creíble.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DOBUTAMINA (el registro no detalla el texto de la indicación) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 0.9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, la dobutamina es un inotrópico agonista beta-1 adrenérgico que se administra por infusión intravenosa y se usa en el soporte hemodinámico de la insuficiencia cardíaca aguda.

El análisis de los datos compilados **no encuentra un vínculo mecanístico creíble** entre la dobutamina y la alopecia. La dobutamina no tiene efecto conocido sobre la biología del folículo piloso. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

La única publicación recuperada describe insuficiencia cardíaca por intoxicación con minoxidil en un gato, en la que se usó dobutamina para tratar la hipotensión. Es un reporte de toxicidad veterinaria y no constituye evidencia de eficacia de la dobutamina en alopecia.

Otras predicciones del modelo (hipotricosis, alopecia areata difusa, glaucoma, enfermedad de Raynaud, cefalea, migraña, hipertricosis) tampoco cuentan con respaldo mecanístico ni clínico; la mayoría se limita a predicción del modelo (L5) o a evidencia indirecta preclínica (L4).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Reporte de caso (veterinario) | Journal of Veterinary Cardiology | Gato de 13 meses con insuficiencia cardíaca congestiva por intoxicación con minoxidil; se usó dobutamina por hipotensión. No evalúa la dobutamina como tratamiento de alopecia. |

---

## Información de Mercado en Colombia

El medicamento está comercializado y cuenta con 3 registros sanitarios vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20068276 | AUTOBOD (Laboratorio Blaskov SAS) | Solución inyectable | DOBUTAMINA |
| 20096467 | DOCARIP® 1 MG/ML (ADS Pharma S.A.S.) | Solución inyectable | DOBUTAMINA |
| 19941379 | DOBUTAMINA 250 MG/20 ML INYECTABLE (Laboratorios Ryan de Colombia S.A.S.) | Solución inyectable | DOBUTAMINA |

---

## Consideraciones de Seguridad

- **Enfermedades con contraindicación señalada en el grafo de conocimiento** (no proviene del texto del prospecto): hipertensión, deficiencia de potasio, fibrilación auricular, estenosis aórtica (incluida la valvular y la supravalvular), enfermedad de la válvula aórtica, infarto de miocardio, trombosis coronaria, hemoglobinopatía y miocardiopatía hipertrófica (incluida la familiar).
- **Interacciones farmacológicas**: se identificaron 101 interacciones, las 20 mostradas son de nivel moderado. Incluyen antidiabéticos (acarbosa, metformina, pioglitazona, repaglinida, clorpropamida), inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), inhibidores de DPP-4 (alogliptina, linagliptina), agonistas de GLP-1 (albiglutida, dulaglutida, liraglutida, semaglutida), insulinas (aspart, degludec), anorexígenos (dietilpropión, fentermina), cimetidina y vancomicina.
- Se debe consultar el prospecto para advertencias y contraindicaciones formales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para alopecia se basa solo en el puntaje del modelo (L5), sin ensayos clínicos, sin literatura que respalde la eficacia y sin mecanismo plausible. Además, el producto no tiene registros vigentes en Colombia y es de uso exclusivamente intravenoso hospitalario, lo que lo hace poco compatible con una indicación dermatológica.

**Para avanzar se necesita:**
- Obtener el texto de advertencias y contraindicaciones del prospecto INVIMA.
- Completar los datos del mecanismo de acción desde DrugBank.
- Demostrar un vínculo mecanístico creíble con la biología del folículo piloso mediante estudios preclínicos.
- Evaluar la compatibilidad de la vía de administración con la nueva indicación.
- Considerar priorizar otras candidatas del modelo con mayor plausibilidad biológica, o descartar la hipótesis de reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

