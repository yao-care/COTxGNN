---
layout: default
title: Posaconazole
parent: Solo Predicción del Modelo (L5)
nav_order: 524
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Posaconazole: nueva indicación predicha, Neumocistosis (nivel de evidencia L4). Indicación original: No especificada en detalle"
monitor_inn: "posaconazole"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Posaconazol: De Posaconazol (indicación no detallada en el registro) a Neumocistosis
{: .text-alpha }

## Resumen en Una Frase

Posaconazol es un antifúngico triazólico, registrado en Colombia en tabletas de liberación retardada, cuyo texto de indicación en el registro sanitario solo indica el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero la evidencia real es muy limitada: **1 ensayo clínico** (que evalúa otro fármaco, rezafungina) y **5 publicaciones** de carácter general (guías, revisiones y un estudio de cohorte), ninguna de las cuales demuestra eficacia de posaconazol en esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en detalle (el registro solo indica "Posaconazol"); clase antifúngica triazólica |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, posaconazol es un antifúngico triazólico que inhibe la lanosterol 14-alfa-desmetilasa (CYP51), bloqueando la síntesis de ergosterol en la membrana fúngica.

Sin embargo, la plausibilidad mecanística para neumocistosis es débil. *Pneumocystis jirovecii* carece de ergosterol en su membrana y utiliza colesterol y otros esteroles, por lo que el mecanismo de los azoles no tiene una diana clara en este organismo. El puntaje tan alto de TxGNN (0.9977) probablemente refleja la cercanía en la red de conocimiento con otros antifúngicos y enfermedades fúngicas invasivas, más que una verdadera afinidad mecanística.

Como referencia, el tratamiento de primera línea de la neumocistosis es trimetoprima-sulfametoxazol. Las equinocandinas (por ejemplo, rezafungina) se han investigado como posible complemento porque inhiben la beta-1,3-glucano sintasa de la forma quística de *Pneumocystis*; este mecanismo es distinto al de posaconazol.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Fase 3 | Completado | 602 | Rezafungina intravenosa frente al régimen antimicrobiano estándar para prevenir enfermedades fúngicas invasivas en adultos sometidos a trasplante alogénico de sangre y médula ósea (estudio ReSPECT). No evalúa posaconazol para neumocistosis; relevancia baja. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guía/Revisión | The Lancet. Infectious Diseases | Recomendaciones de la Sociedad Británica de Micología Médica (actualización 2025) para el diagnóstico de enfermedades fúngicas graves; no aborda eficacia de posaconazol en neumocistosis |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guía/Revisión | Zhonghua Jie He He Hu Xi Za Zhi | Guía china 2025 para el diagnóstico y manejo de enfermedades fúngicas pulmonares invasivas |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Revisión | Swiss Medical Weekly | Panorama de candidiasis invasiva, aspergilosis, criptococosis y neumonía por *Pneumocystis*; menciona que la profilaxis con posaconazol (activo frente a mohos) redujo infecciones fúngicas invasivas en pacientes hemato-oncológicos de alto riesgo |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisión | Clinical Pharmacokinetics | Penetración de antiinfecciosos (incluidos antifúngicos) en el líquido de revestimiento epitelial pulmonar |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohorte | Transplant Infectious Disease | Complicaciones infecciosas en la enfermedad injerto contra huésped aguda tras trasplante hepático |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20064520 (cancelado) | NOXAFIL® Tabletas Recubiertas de Liberación Retardada (Merck Sharp & Dohme LLC) | Tableta de liberación retardada | Posaconazol (sin detalle de indicación) |
| 20195133 (cancelado) | Posaconazol 100 mg Tabletas Gastrorresistentes (Sandoz GmbH) | Tableta de liberación retardada | Posaconazol (sin detalle de indicación) |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 269 interacciones en total. Entre las de nivel **mayor** figuran loperamida, triamcinolona y budesonida. Entre las de nivel **moderado** figuran famotidina, ranitidina, rabeprazol, omeprazol, cimetidina, hidrocortisona, dexametasona, betametasona, aprepitant, claritromicina, bisacodilo, ácido picosulfúrico, polietilenglicol 3350 con electrolitos y saxagliptina.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es muy alta, pero no hay estudios que evalúen posaconazol en neumocistosis y el mecanismo azólico carece de una diana clara en *Pneumocystis*. Además, el fármaco no tiene registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos de mecanismo de acción verificados en fuentes primarias (por ejemplo, DrugBank)
- Estudios preclínicos o clínicos que evalúen directamente posaconazol frente a *Pneumocystis*, comparado con trimetoprima-sulfametoxazol
- Prospecto del INVIMA con advertencias y contraindicaciones para completar el tamizaje de seguridad
- Aclarar la situación regulatoria (registros cancelados) y la indicación aprobada originalmente
- Análisis de compatibilidad de vías de administración y similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

