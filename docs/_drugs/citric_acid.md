---
layout: default
title: Citric Acid
parent: Evidencia Moderada (L3-L4)
nav_order: 160
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-14
description: "Citric Acid: nueva indicación predicha, Enfermedad del estómago (stomach disease) (nivel de evidencia L4). Indicación original: Electrolitos combinaciones"
monitor_inn: "citric acid"
predicted_indications: ["stomach disease", "pharyngitis", "acute laryngopharyngitis", "postgastrectomy syndrome", "nasal cavity disease", "papillary conjunctivitis", "blepharoconjunctivitis", "rhinitis"]
---

# Citric Acid
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

# Ácido cítrico: De Combinaciones de Electrolitos a Enfermedad del Estómago

## Resumen en Una Frase

El ácido cítrico (comercializado en Colombia como HIDRALITOS) se utilizó originalmente como parte de combinaciones de electrolitos en solución oral.
El modelo TxGNN predice que podría ser efectivo para **enfermedad del estómago**,
pero **no hay ensayos clínicos registrados** y la literatura disponible (20 publicaciones) es indirecta, por lo que la predicción es solo una hipótesis computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Electrolitos combinaciones |
| Nueva Indicación Predicha | Enfermedad del estómago (stomach disease) |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido cítrico es un componente de soluciones de rehidratación y electrolitos orales, y su uso como regulador de acidez y fuente de citrato en ese contexto está establecido. Mecanísticamente, podría relacionarse con el entorno ácido gástrico, pero esto es una inferencia y no un hallazgo comprobado.

La literatura recuperada muestra que el ácido cítrico se ha estudiado como comida de prueba para mejorar la precisión de la prueba de aliento con urea-13C para detectar *Helicobacter pylori*. Es un uso **diagnóstico**, no terapéutico. Se sabe que acidifica el ambiente gástrico y retrasa el vaciado gástrico, lo que podría explicar ese papel diagnóstico.

No existe un vínculo terapéutico establecido con la enfermedad del estómago. El puntaje de 0.997 es únicamente una predicción computacional y no debe interpretarse como evidencia de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Las publicaciones son en su mayoría revisiones, estudios observacionales o preclínicos, sin ensayos terapéuticos. Se listan las más relevantes:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Estudio diagnóstico clínico | Gut and Liver | Comentario sobre si una comida con ácido cítrico mejora la precisión de la prueba de aliento con urea-13C en poblaciones asiáticas (uso diagnóstico) |
| [30970440](https://pubmed.ncbi.nlm.nih.gov/30970440/) | 2019 | Estudio diagnóstico | Gut and Liver | Efecto del ácido cítrico en la precisión de la prueba de aliento tras la erradicación de *H. pylori* en una región con alta prevalencia de gastritis atrófica |
| [15854177](https://pubmed.ncbi.nlm.nih.gov/15854177/) | 2005 | Estudio mecanístico | Aliment Pharmacol Ther | Efecto de distintos ácidos orgánicos (cítrico, málico, ascórbico) sobre la actividad de la ureasa intragástrica |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Revisión | Med Clin North Am | Dieta y nutrición en la enfermedad ulcerosa; no se requieren dietas restrictivas |
| [9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/) | 1998 | Revisión | Adv Microb Physiol | Fisiología y metabolismo de *H. pylori* |
| [39539553](https://pubmed.ncbi.nlm.nih.gov/39539553/) | 2024 | Revisión | Front Immunol | Papel de la cuproptosis en el cáncer gástrico |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Observacional/metabolómica | Metabolomics | Niveles séricos altos de L-carnitina y ácido cítrico antes del inicio del cáncer gástrico en coreanos (biomarcador) |
| [7106518](https://pubmed.ncbi.nlm.nih.gov/7106518/) | 1982 | Observacional | Gastroenterology | Secreción salival en esofagitis por reflujo |
| [40987977](https://pubmed.ncbi.nlm.nih.gov/40987977/) | 2025 | Preclínico | Inflammopharmacol | Extracto de hojas de *Spondias purpurea* acelera la cicatrización de úlceras en roedores (sin relación directa con ácido cítrico) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19978751 (cancelado) | HIDRALITOS | Solución oral | Electrolitos combinaciones |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento asocia el fármaco con enfermedades como hipertensión, enfermedad renal, anuria, función renal deteriorada, enfermedad hepática, insuficiencia cardíaca congestiva, insuficiencia suprarrenal (incluida la enfermedad de Addison e hiperplasia suprarrenal congénita), úlcera péptica, gota, hipercalcemia, nefrocalcinosis, trombocitopenia, hemofilia, anemia y diarrea crónica, entre otras. Estas relaciones deben verificarse con fuentes regulatorias.
- **Interacciones farmacológicas** (15 registradas):
  - **Mayor**: hidróxido de aluminio.
  - **Moderada**: quinolonas y fármacos relacionados (cinoxacino, ciprofloxacino, enoxacino, gatifloxacino, gemifloxacino, levofloxacino, lomefloxacino, moxifloxacino, ácido nalidíxico, norfloxacino, ofloxacino, trovafloxacino, grepafloxacino, esparfloxacino).

No se dispone de advertencias ni contraindicaciones del prospecto del INVIMA; consultar el prospecto cuando esté disponible.

---

## Otras Indicaciones Predichas (Referencia)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| Faringitis | 99.68% | L4 | Hold |
| Laringofaringitis aguda | 99.59% | L5 | Hold |
| Síndrome postgastrectomía | 99.58% | L5 | Hold |
| Enfermedad de la cavidad nasal | 99.52% | L5 | Hold |
| Conjuntivitis papilar | 99.24% | L5 | Hold |
| Blefaroconjuntivitis | 99.14% | L5 | Hold |
| Rinitis | 99.07% | L4 | Hold |

En faringitis y rinitis, el ácido cítrico aparece sobre todo como agente que induce tos en modelos experimentales, o como excipiente, y no como tratamiento. En rinitis/rinosinusitis hay datos preclínicos de una preparación de ácido cítrico con surfactante zwitteriónico contra biopelículas, cuyo efecto no puede separarse del surfactante.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura es indirecta (uso diagnóstico, estudios de biomarcadores y modelos preclínicos), sin respaldo terapéutico para la enfermedad del estómago. Además, el único registro sanitario en Colombia está cancelado y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), un vacío que bloquea la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir una hipótesis terapéutica concreta (por ejemplo, un efecto sobre el pH gástrico o la erradicación de *H. pylori*) y probarla en estudios preclínicos o piloto.
- Verificar las contraindicaciones del grafo de conocimiento frente a fuentes regulatorias, en especial las renales, cardíacas y suprarrenales.
- Revisar la viabilidad regulatoria, dado que no hay registros vigentes en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

