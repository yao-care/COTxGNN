---
layout: default
title: Ampicillin
parent: Evidencia Moderada (L3-L4)
nav_order: 49
evidence_level: L4
indication_count: 10
---

# Ampicillin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Ampicilina: De «Ampicilina e Inhibidor Enzimático» a Laringitis

## Resumen en Una Frase

La ampicilina es un antibiótico betalactámico. En Colombia, el texto del registro sanitario solo dice «ampicilina e inhibidor enzimático», sin detallar la indicación.
El modelo TxGNN predice que podría ser efectiva para **laringitis**.
Solo hay **1 ensayo clínico**, sobre otro fármaco (amoxicilina/clavulanato), y **20 publicaciones**, casi todas reportes de caso y revisiones que no evalúan la ampicilina directamente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ampicilina e inhibidor enzimático (texto del registro; no describe una indicación clínica específica) |
| Nueva Indicación Predicha | Laringitis |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según el conocimiento general, la ampicilina es un betalactámico que inhibe las proteínas fijadoras de penicilina de la bacteria y bloquea así la síntesis de su pared celular. Su eficacia contra infecciones bacterianas sensibles es conocida desde hace décadas.

El vínculo con la laringitis existe, pero es limitado. Las infecciones bacterianas de la laringe y la región supraglótica, como la epiglotitis o el absceso laríngeo, podrían ser sensibles a un betalactámico. Sin embargo, la mayoría de las laringitis son virales, y contra ellas un antibiótico no tiene efecto esperable. La predicción solo sería plausible para un subgrupo bacteriano.

El puntaje alto de TxGNN refleja la asociación en el grafo de conocimiento entre antibióticos e infecciones de vías respiratorias altas. No demuestra eficacia de la ampicilina en laringitis.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | Completado | 363 | Vigilancia posterior a la comercialización de CLAVAMOX® (amoxicilina/clavulanato) en jarabe pediátrico, en Japón. Cubre infecciones de piel, faringitis, laringitis, amigdalitis, bronquitis, cistitis y pielonefritis (excepto otitis media). |

**Nota:** este estudio es de otro fármaco y no es un ensayo de eficacia. No confirma que la laringitis sea la condición estudiada (relevancia: C). No aporta evidencia directa para la ampicilina.

---

## Evidencia de Literatura

No se encontró ningún ECA. Los estudios están ordenados por tipo (revisiones antes que reportes de caso) y fecha.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Reporte de caso y revisión | Ann Otol Rhinol Laryngol | Los abscesos laríngeos son raros en la era antibiótica. Se presenta un caso en un paciente con diabetes no controlada y una revisión de casos modernos. |
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Evaluación de guías (AGREE II) | CoDAS | Evalúa la calidad metodológica de las guías clínicas para laringitis y faringitis. |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Revisión | Anaesth Intensive Care | 161 niños con epiglotitis aguda: 45 complicaciones y 5 muertes. Recomienda intubación nasotraqueal como manejo de la vía aérea. |
| [5314768](https://pubmed.ncbi.nlm.nih.gov/5314768/) | 1971 | Revisión | Br Med J | Epiglotitis en adultos (sin resumen disponible). |
| [5046782](https://pubmed.ncbi.nlm.nih.gov/5046782/) | 1972 | Revisión | Arch Dis Child | Manejo del crup agudo (sin resumen disponible). |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | Reporte de caso | Auris Nasus Larynx | Actinomicosis laríngea en una adolescente de 14 años tras un trasplante de médula ósea. |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | Reporte de caso y revisión | Auris Nasus Larynx | Epiglotitis aguda probablemente causada por COVID-19, con lesiones laríngeas erosivas. |
| [6465636](https://pubmed.ncbi.nlm.nih.gov/6465636/) | 1984 | Serie de casos | Ann Emerg Med | Tres adultos con epiglotitis; el diagnóstico suele pasar inadvertido y puede haber obstrucción de la vía aérea. |
| [3347186](https://pubmed.ncbi.nlm.nih.gov/3347186/) | 1988 | Serie de casos | Med J Aust | Tres casos de epiglotitis del adulto, con énfasis en la variabilidad clínica y la dificultad diagnóstica. |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Estudio observacional | Otolaryngol Head Neck Surg | Relaciona el antibiótico perioperatorio elegido en laringectomía con infección de herida, dehiscencia y complicaciones por antibióticos. |

**Nota:** ninguna de estas publicaciones muestra que la ampicilina sea eficaz en laringitis. Son en su mayoría descripciones de la enfermedad o de infecciones laríngeas específicas.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20166599 | AUROPENNZ 1.5 G | Polvo estéril para reconstituir a solución inyectable | Ampicilina e inhibidor enzimático |

El paquete de evidencia informa 12 registros en total, pero solo detalla uno (20166599), repetido cinco veces con datos idénticos. Aquí se muestra una sola vez. El fabricante es Eugia Pharma Specialities Limited. La forma farmacéutica es inyectable.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Hay solo un ensayo sobre otro fármaco y sin relación de eficacia confirmada. La literatura es descriptiva (reportes de caso y revisiones) y no evalúa la ampicilina en laringitis. Además, la mayoría de las laringitis son virales, por lo que un antibiótico solo tendría sentido en casos bacterianos específicos como la epiglotitis. Con esta base, la evidencia corresponde a un nivel L4.

**Para avanzar se necesita:**
- Obtener del sitio de INVIMA el prospecto con advertencias y contraindicaciones, para completar el tamizaje de seguridad.
- Aclarar la indicación aprobada real de los productos con ampicilina y su inhibidor enzimático.
- Definir el subgrupo de interés, por ejemplo laringitis o epiglotitis bacteriana confirmada, y buscar estudios que usen específicamente ampicilina.
- Consultar la base de datos de DrugBank para completar los datos del mecanismo de acción.
- Considerar otras predicciones del mismo modelo antes de invertir en esta. Por ejemplo, la uretritis gonocócica tiene evidencia histórica más directa (varios ensayos comparativos con ampicilina), aunque hoy está limitada por la resistencia bacteriana.

*Este informe es solo para fines de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

