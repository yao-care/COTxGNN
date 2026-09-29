---
layout: default
title: Pantoprazole
parent: Solo Predicción del Modelo (L5)
nav_order: 317
evidence_level: L5
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Pantoprazol: De Indicación Original No Especificada a Enfermedad Ulcerosa Péptica Activa

## Resumen en Una Frase

Pantoprazol es un inhibidor de la bomba de protones (IBP) comercializado en Colombia. Los registros sanitarios solo repiten el nombre del principio activo y no detallan la indicación original.
El modelo TxGNN predice que podría ser efectivo para **enfermedad ulcerosa péptica activa**, con **3 ensayos clínicos** y **19 publicaciones** asociados a esta predicción.
Se trata en la práctica de un uso ya establecido para esta clase de fármacos, no de un hallazgo de reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PANTOPRAZOL (el texto del registro solo repite el nombre del fármaco, sin indicación explícita) |
| Nueva Indicación Predicha | Enfermedad ulcerosa péptica activa |
| Puntaje de Predicción TxGNN | 99.69% |
| Nivel de Evidencia | L2 (el pack de evidencia indica L1, ver nota en la conclusión) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. Según la información conocida, pantoprazol es un inhibidor de la bomba de protones. Bloquea de forma irreversible la enzima H+/K+ ATPasa de la célula parietal gástrica, lo que reduce la secreción de ácido.

Las úlceras pépticas dependen en gran medida de la exposición de la mucosa al ácido. Al reducirla, la mucosa puede cicatrizar, y por eso los IBP también se usan dentro de los esquemas de erradicación de *Helicobacter pylori*. La coherencia entre el mecanismo y la indicación explica el puntaje tan alto del modelo.

Como la indicación original no está documentada en los datos recibidos, no se puede afirmar que esta indicación esté o no en el prospecto colombiano. Debe verificarse por separado. Es probable que la predicción refleje un uso clínico ya establecido para la clase.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Fase 3 | Completado | 323 | Ensayo aleatorizado, doble ciego, con control activo. Compara terapia triple de 7 días con ilaprazol frente a pantoprazol para erradicar *H. pylori* en pacientes con úlcera gástrica o duodenal. El título está truncado y conviene confirmarlo en el registro. |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | No aplica | Completado | 316 | Estudio prospectivo para definir criterios de selección de quién necesita una segunda endoscopia tras una úlcera sangrante. Trata una estrategia de manejo, no la eficacia de pantoprazol. |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Fase 4 | Completado | 320 | Efecto de estatinas e IBP sobre la acción antiplaquetaria de clopidogrel en pacientes con stent coronario. Es una pregunta de interacción farmacodinámica, no de tratamiento de úlceras. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | ECA | Digestion | Compara infusión intermitente frente a continua de pantoprazol para prevenir el resangrado de úlcera péptica tras terapia endoscópica. |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | ECA | Aliment Pharmacol Ther | Compara tres terapias triples basadas en pantoprazol para erradicar *H. pylori* y cicatrizar la úlcera gástrica. |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | ECA | J Gastroenterol Hepatol | Evalúa la infusión de pantoprazol como coadyuvante de la terapia endoscópica en úlcera sangrante. |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisión sistemática y metaanálisis en red | Am J Gastroenterol | Compara bloqueadores ácidos competitivos de potasio (P-CAB) con IBP en esofagitis grado C/D. Es evidencia de clase, no específica de pantoprazol. |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | ECA | Gut Liver | Evalúa tegoprazán en úlceras artificiales tras resección endoscópica. Es indirecta, porque el fármaco estudiado no es pantoprazol. |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Revisión | Clin Drug Investig | Revisión de pantoprazol: unión irreversible a la bomba de protones y larga duración de acción. |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclínico (animal) | Inflammopharmacology | Pantoprazol combinado con células madre mesenquimales en úlcera gástrica inducida en ratas. Sugiere efectos sobre estrés oxidativo, inflamación y apoptosis. |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Estudio comparativo (diseño no confirmado) | Hepato-gastroenterology | Compara lansoprazol y pantoprazol en úlcera duodenal activa y erradicación de *H. pylori*. |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | Sin clasificar | Aliment Pharmacol Ther | Pantoprazol, amoxicilina y azitromicina o claritromicina para erradicar *H. pylori* en úlcera duodenal. |
| [10228801](https://pubmed.ncbi.nlm.nih.gov/10228801/) | 1999 | Sin clasificar | Hepato-gastroenterology | Terapia triple de 1 semana con pantoprazol, amoxicilina y metronidazol en úlcera duodenal con *H. pylori*. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20102044 | PANTOPRAZOL 40 MG (Laboratorios MK S.A.S.) | Tableta de liberación retardada | PANTOPRAZOL (sin indicación detallada en el registro) |

El pack contiene 20 registros en total, pero las cinco entradas recibidas son idénticas y corresponden al mismo registro sanitario. Por eso se muestra una sola fila.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 3 completado (n=323) y varios ECA publicados que respaldan el uso de pantoprazol en úlcera péptica, además de un mecanismo plausible. Sin embargo, esta indicación es un uso establecido de la clase, no un reposicionamiento novedoso. Faltan además datos regulatorios y de seguridad locales.

**Nota sobre el nivel de evidencia:** el pack asigna L1, pero entre los ensayos listados para esta indicación solo hay un Fase 3 completado (NCT02084420), lo que corresponde a L2 con la regla aplicada. El L1 se sostendría con los Fase 3 adicionales listados para "úlcera duodenal" (por ejemplo NCT00261300), que conviene confirmar.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para confirmar indicaciones, advertencias y contraindicaciones (brecha bloqueante).
- Confirmar en el registro de ClinicalTrials.gov el detalle de NCT02084420, cuyo título está truncado.
- Obtener el mecanismo de acción y la información de interacciones desde DrugBank.
- Verificar si la úlcera péptica ya figura como indicación aprobada en Colombia, para decidir si hay algo que reposicionar.

Las otras indicaciones predichas tienen menos respaldo. La úlcera gastroyeyunal y la perforación de úlcera péptica quedan como preguntas de investigación. El reflujo duodenogástrico y la obstrucción duodenal quedan en Hold, y esta última sin vínculo mecanístico creíble.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

