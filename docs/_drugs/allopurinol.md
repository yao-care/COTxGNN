---
layout: default
title: Allopurinol
parent: Evidencia Moderada (L3-L4)
nav_order: 38
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Allopurinol: nueva indicación predicha, Porfiria hepática (nivel de evidencia L4). Indicación original: Alopurinol"
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
---

# Allopurinol
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

# Alopurinol: De Alopurinol (indicación registrada sin detalle) a Porfiria Hepática

## Resumen en Una Frase

Alopurinol es un inhibidor de la xantina oxidasa que se usa principalmente para la hiperuricemia y la gota crónica; en los registros sanitarios de Colombia solo figura con el texto "alopurinol", sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática**, pero no hay ensayos clínicos y solo **2 publicaciones** de relevancia indirecta (una hipótesis y un estudio preclínico en ratas sobre otro fármaco).
La predicción es, por ahora, una señal del modelo sin respaldo clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Alopurinol (el registro no detalla la indicación; el uso conocido es hiperuricemia y gota crónica) |
| Nueva Indicación Predicha | Porfiria hepática |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el alopurinol inhibe la xantina deshidrogenasa/oxidasa (gen XDH), la enzima que produce ácido úrico, y su eficacia en hiperuricemia y gota crónica está comprobada.

El vínculo con la porfiria hepática es **indirecto y especulativo**. Un artículo de hipótesis de 2019 (PMID 31443750) propone actuar sobre la 5-aminolevulinato sintasa (ALAS1), enzima limitante de la síntesis del hemo, mediante triptófano e inhibidores del uso de hemo por la triptófano 2,3-dioxigenasa. El alopurinol no es un modulador establecido de ALAS1. El segundo artículo (PMID 1567472) trata sobre carbamazepina en hígado de rata, no sobre alopurinol.

Además, hay literatura antigua que sugiere que el alopurinol podría ser porfirinogénico o afectar el hemo oxigenasa y el citocromo P450 en modelos animales, lo que plantea una posible preocupación de seguridad en esta enfermedad. El puntaje alto de TxGNN refleja una predicción de red, no evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Revisión/Hipótesis | Medical Hypotheses | Propone reducir la actividad de ALAS1 hepática con triptófano o inhibiendo el uso de hemo por la triptófano 2,3-dioxigenasa como terapia de porfirias hepáticas agudas. No evalúa alopurinol. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclínico (rata) | Biochemical Pharmacology | La carbamazepina a dosis muy bajas agrava el metabolismo del hemo en hígado de rata y se comporta como exacerbante de porfirias. No involucra alopurinol. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11415 | ALOPURINOL 300 MG (Memphis Products S.A.) | Tableta | Alopurinol (estado: cancelado) |
| 18777 | UROCUAD® Tabletas 100 mg (Teofarma S.R.L.) | Tableta | Alopurinol (estado: cancelado) |
| 19966240 | ALLO Tableta (Laboratorios Neo Ltda.) | Tableta | Alopurinol (estado: cancelado) |

---

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de precaución (grafo de conocimiento, no texto del prospecto):** enfermedad hepática, enfermedad de la vesícula biliar, función renal alterada, vasculitis por hipersensibilidad, angeítis leucocitoclástica cutánea, vasculitis cutánea alérgica y enfermedad por anticuerpos antimembrana basal glomerular.
- **Interacciones y diana farmacológica:** el alopurinol actúa sobre la xantina deshidrogenasa (XDH, humana). No se dispone de otras interacciones farmacológicas con nivel de gravedad.
- **Señales relevantes para la indicación predicha:** existen reportes antiguos de posible efecto porfirinogénico en modelos animales, y la enfermedad hepática figura entre las condiciones de precaución. Esto exige cautela especial en porfiria hepática.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura disponible no estudia el alopurinol en porfiria; el puntaje alto de TxGNN refleja una predicción de red. Además, existe una posible señal de seguridad (efecto porfirinogénico en animales) y todos los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre alopurinol y porfirias (seguridad porfirinogénica, hemo oxigenasa, citocromo P450).
- Estudios preclínicos que evalúen directamente el efecto del alopurinol sobre ALAS1 y el metabolismo del hemo.
- Datos de mecanismo de acción detallados (por ejemplo, desde DrugBank).
- Obtener y analizar advertencias y contraindicaciones del prospecto en el sitio de INVIMA.
- Aclarar la situación regulatoria, dado que no hay registros vigentes en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

