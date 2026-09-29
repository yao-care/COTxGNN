---
layout: default
title: Epinephrine
parent: Evidencia Alta (L1-L2)
nav_order: 181
evidence_level: L1
indication_count: 4
---

# Epinephrine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **4** 
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

# Epinefrina: De Uso Original No Especificado a Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

La epinefrina (adrenalina) es un agonista adrenérgico de uso amplio. En Colombia está registrada como solución inyectable, y el registro sanitario no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **enfermedad pulmonar obstructiva**, con **50 ensayos clínicos registrados** y **20 publicaciones** relacionados con esta dirección. Solo tres de esos ensayos son de Fase 3 completados y evalúan directamente epinefrina, y en bronquiolitis la evidencia es mixta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro sanitario solo indica "EPINEFRINA", sin texto de indicación) |
| Nueva Indicación Predicha | Enfermedad pulmonar obstructiva |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, la epinefrina es un agonista adrenérgico no selectivo. La estimulación de los receptores beta-2 relaja el músculo liso bronquial, y la de los alfa-1 reduce el edema de la mucosa. Ambos efectos pueden aliviar la obstrucción de la vía aérea, lo que es coherente con el puntaje alto del modelo.

Además, la epinefrina inhalada ya es un broncodilatador establecido para el asma en algunos mercados. Por eso esta predicción se acerca más a confirmar un uso conocido que a un reposicionamiento realmente novedoso.

Hay varias salvedades:
- En bronquiolitis, el foco principal de la literatura, la evidencia es mixta y las revisiones Cochrane muestran beneficio limitado o inconsistente.
- Los títulos de varios ensayos están truncados, por lo que la población de pacientes y el comparador no están verificados.
- La evidencia más sólida usa una formulación en aerosol inhalado, mientras que los registros en Colombia son de solución inyectable.

---

## Evidencia de Ensayos Clínicos

Se listan los ensayos más relevantes de los 50 registrados. Los demás son en su mayoría estudios sobre otros fármacos (corticoides, omalizumab, etc.) o sin relación con epinefrina.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Fase 3 | Completado | 70 | Aerosol inhalado de epinefrina (E004) vs placebo en niños de 4 a 11 años con asma; estudio aleatorizado, doble ciego, de 4 semanas |
| [NCT03567473](https://clinicaltrials.gov/study/NCT03567473) | Fase 3 | Completado | 864 | Epinefrina inhalada más dexametasona oral vs placebo en lactantes con bronquiolitis; criterio principal: hospitalizaciones a 7 días |
| [NCT00116584](https://clinicaltrials.gov/study/NCT00116584) | Fase 3 | Completado | 72 | Epinefrina racémica nebulizada con heliox vs aire-oxígeno en bronquiolitis moderada a grave |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Fase 4 | Completado | 120 | Estudio piloto aleatorizado de epinefrina, dexametasona y solución salina hipertónica en bronquiolitis pediátrica |
| [NCT02585531](https://clinicaltrials.gov/study/NCT02585531) | Fase 2 | Desconocido | 100 | Epinefrina, dexametasona y solución salina hipertónica en bronquiolitis (Hospital General Naval, México) |
| [NCT05363670](https://clinicaltrials.gov/study/NCT05363670) | Fase 2 | Completado | 18 | Estudio cruzado de epinefrina intranasal (ARS-1) vs albuterol en asma persistente, como alternativa sin aguja |
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Fase 1/2 | Completado | 24 | Farmacocinética y seguridad del aerosol de epinefrina (E004) en voluntarios sanos |
| [NCT01025648](https://clinicaltrials.gov/study/NCT01025648) | Fase 1/2 | Terminado | 9 | Búsqueda de dosis de epinefrina HFA-MDI (E004) vs placebo y epinefrina CFC-MDI en asma leve a moderada; terminado con solo 9 pacientes |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Fase 4 | Desconocido | 500 | Búsqueda del tratamiento inhalado óptimo en lactantes con bronquiolitis aguda (uso de epinefrina no confirmado en el texto disponible) |
| [NCT00435994](https://clinicaltrials.gov/study/NCT00435994) | N/A | Completado | 59 | Efecto de dos medicamentos en aerosol sobre la función de la vía aérea en lactantes con infecciones respiratorias bajas (medicamentos no confirmados en el texto disponible) |

---

## Evidencia de Literatura

No se identificaron ensayos controlados aleatorizados entre las publicaciones. Predominan revisiones y estudios secundarios.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Epinefrina para bronquiolitis; parte de la duda sobre la efectividad real de los broncodilatadores en esta enfermedad |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Versión anterior de la revisión sobre epinefrina en bronquiolitis; los broncodilatadores aportan un beneficio modesto a corto plazo en casos leves a moderados |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Revisión | Expert Rev Respir Med | Analiza el papel de la epinefrina racémica, los corticoides sistémicos, la solución salina hipertónica y el oxígeno de alto flujo en bronquiolitis |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | Análisis de costo-efectividad | Pediatrics | Costo-efectividad de epinefrina y dexametasona en lactantes con bronquiolitis, con datos del ensayo canadiense CBEST |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Revisión | Pediatr Clin North Am | Los corticoides mejoran el crup; la adrenalina nebulizada da alivio sintomático temporal. En bronquiolitis falta una definición diagnóstica clara |
| [19444115](https://pubmed.ncbi.nlm.nih.gov/19444115/) | 2009 | Revisión | Curr Opin Pediatr | Actualización sobre los usos de la epinefrina en urgencias pediátricas |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Revisión | BMJ Clin Evid | Resumen sobre bronquiolitis, la infección respiratoria baja más común en lactantes |
| [11339733](https://pubmed.ncbi.nlm.nih.gov/11339733/) | 2001 | Revisión sistemática | Prehosp Emerg Care | Uso prehospitalario de epinefrina subcutánea (asma y anafilaxia) en personas mayores |
| [4551435](https://pubmed.ncbi.nlm.nih.gov/4551435/) | 1972 | Revisión (sin resumen) | Ann Allergy | Broncodilatadores nebulizados en enfermedad pulmonar obstructiva; solo se dispone del título |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Revisión | J Allergy Clin Immunol | Define el asma infantil como enfermedad obstructiva de la vía aérea por espasmo muscular, exceso de moco e inflamación |

---

## Información de Mercado en Colombia

Hay 20 registros sanitarios en total. Los datos disponibles muestran el mismo registro repetido, por lo que se presenta una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20032463 | Epinefrina solución inyectable 1 mg/1 mL (Laboratorio Biosano S.A.) | Solución inyectable | Epinefrina (sin texto de indicación detallado) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay tres ensayos de Fase 3 completados que evalúan epinefrina en vías aéreas obstructivas (asma pediátrica y bronquiolitis), lo que sustenta el nivel L1. Sin embargo, la evidencia en bronquiolitis es inconsistente y la formulación estudiada (inhalada) no coincide con la registrada en Colombia (inyectable).

**Para avanzar se necesita:**
- Confirmar la población, el comparador y los resultados de los ensayos con títulos truncados, especialmente NCT01460511 y NCT03567473.
- Verificar la compatibilidad de vía y formulación: los ensayos usan aerosol inhalado o nebulizado, y el registro local es solo solución inyectable.
- Obtener el prospecto de INVIMA para advertencias y contraindicaciones, que no están disponibles.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir si el objetivo es enfermedad pulmonar obstructiva en general o un subgrupo concreto (asma, bronquiolitis, EPOC), dado que los resultados difieren según la población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

