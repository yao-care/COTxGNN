---
layout: default
title: Pantoprazole
parent: Solo Predicción del Modelo (L5)
nav_order: 498
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Pantoprazol: nueva indicación predicha, obstrucción duodenal (nivel de evidencia L1). Indicación original: Pantoprazol"
monitor_inn: "Pantoprazole"
predicted_indications: ["duodenal obstruction"]
---

# Pantoprazole
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

## Pantoprazol: De Indicación Original (Pantoprazol) a obstrucción duodenal
{: .text-alpha }

## Resumen en Una Frase

Pantoprazol es un inhibidor de la bomba de protones (IBP) registrado en Colombia bajo la indicación genérica "pantoprazol" (tabletas de liberación retardada de 40 mg).
El modelo TxGNN predice que podría ser efectivo para **enfermedad ulcerosa péptica activa**, con **1 ensayo clínico** y **20 publicaciones** asociados directamente a esta predicción.
Se trata de una indicación dentro de la clase terapéutica ya establecida, por lo que la evidencia confirma un uso existente más que un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Pantoprazol (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Enfermedad ulcerosa péptica activa |
| Puntaje de Predicción TxGNN | 0.9921 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Pantoprazol inhibe de forma irreversible la H+/K+ ATPasa (bomba de protones) de la célula parietal gástrica. Esto reduce la secreción de ácido y permite la cicatrización de las úlceras. No se dispone de un campo de mecanismo de acción en los datos de fármaco compilados, pero este mecanismo está ampliamente descrito en la literatura recuperada.

La indicación original registrada ("pantoprazol") es genérica, pero la clase de los IBP se usa de forma establecida en enfermedades ácido-pépticas. Por ello, la predicción de úlcera péptica activa es coherente con el mecanismo y con el uso clínico conocido. Es una confirmación de uso dentro de la clase más que un hallazgo novedoso.

La evidencia directa incluye ensayos aleatorizados de pantoprazol frente a ranitidina y frente a omeprazol en úlcera duodenal aguda. Como salvaguardas se deben considerar el efecto del polimorfismo de CYP2C19 sobre la exposición al fármaco y los riesgos del uso prolongado de IBP (hipomagnesemia, fracturas, infecciones y carga de interacciones).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Fase 3 | Completado | 323 | Ensayo multicéntrico, aleatorizado, doble ciego y con control activo: erradicación de *H. pylori* con terapia triple de 7 días, ilaprazol vs. pantoprazol, en pacientes con úlcera gástrica y/o duodenal |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisión sistemática / metaanálisis en red | Am J Gastroenterol | Compara bloqueadores ácidos competitivos de potasio (P-CAB) con IBP en esofagitis grado C/D |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | ECA | Gut Liver | Tegoprazán en úlceras artificiales por resección endoscópica (no específico de pantoprazol) |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Revisión | Clin Drug Investig | Perfil de pantoprazol como IBP; sin interacciones farmacológicas identificadas en estudios previos |
| [16961157](https://pubmed.ncbi.nlm.nih.gov/16961157/) | 2006 | Revisión | Int J Clin Pharmacol Ther | Impacto del polimorfismo de CYP2C19 en la acción de los IBP |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | Estudio multicéntrico | Am J Gastroenterol | Pantoprazol vs. ranitidina en úlcera duodenal en población brasileña |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Estudio comparativo | Hepatogastroenterology | Lansoprazol vs. pantoprazol en úlcera duodenal activa y erradicación de *H. pylori* |
| [8930575](https://pubmed.ncbi.nlm.nih.gov/8930575/) | 1996 | Revisión | Eur J Gastroenterol Hepatol | Mecanismo de acción y perfil de actividad predecible de pantoprazol |
| [11060758](https://pubmed.ncbi.nlm.nih.gov/11060758/) | 2000 | Revisión | Expert Opin Investig Drugs | Nuevos enfoques terapéuticos para úlceras gástricas y duodenales |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclínico (ratas) | Inflammopharmacology | Pantoprazol combinado con células madre mesenquimales en úlcera gástrica experimental |
| [26439477](https://pubmed.ncbi.nlm.nih.gov/26439477/) | 2016 | Preclínico (ratas) | J Nat Med | Crocina frente a lesiones gástricas por indometacina, con pantoprazol como comparador |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20102044 (cancelado) | PANTOPRAZOL 40 MG (Laboratorios MK S.A.S.) | Tableta de liberación retardada | Pantoprazol |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 100 interacciones en total. Entre las mostradas hay interacciones de nivel **mayor** con acalabrutinib y atazanavir. Las de nivel **moderado** incluyen hidroclorotiazida, alpelisib, anfotericina B, amikacina, anfetamina, fenofibrato, apalutamida, armodafinilo, atorvastatina, bosutinib y bumetanida. Las de nivel **menor** incluyen ácido acetilsalicílico, axitinib, bortezomib, brivaracetam y cianocobalamina.
- **Enfermedades con contraindicación según el grafo de conocimiento** (no proviene del prospecto): osteoporosis, osteoporosis posmenopáusica, fractura ósea y anemia perniciosa.
- **Otras precauciones**: el polimorfismo de CYP2C19 modifica la exposición, y el uso prolongado de IBP se asocia a hipomagnesemia, fracturas e infecciones.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado y varios ECA publicados (pantoprazol vs. ranitidina y vs. omeprazol en úlcera duodenal) que respaldan el uso en enfermedad ulcerosa péptica. Sin embargo, es un uso ya establecido de la clase, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Confirmar la situación regulatoria en Colombia: no hay registro vigente, por lo que habría que gestionar uno nuevo o identificar otros productos de pantoprazol.
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde una fuente formal como DrugBank.
- Definir un plan de seguimiento para uso prolongado (magnesio, salud ósea, vitamina B12) y para el manejo de interacciones, en especial con acalabrutinib y atazanavir.
- Considerar el genotipo de CYP2C19 en poblaciones relevantes.

---

### Nota sobre otras indicaciones predichas

Otras predicciones del modelo tienen respaldo menor y no se desarrollan en este informe:

- **Úlcera gastroyeyunal** y **perforación de úlcera péptica**: nivel L3, "pregunta de investigación"; evidencia extrapolada de condiciones ácido-pépticas relacionadas.
- **Reflujo duodenogástrico**: nivel L3, ajuste mecanístico parcial.
- **Obstrucción duodenal**: nivel L5, **Hold**; sin vínculo mecanístico claro. El puntaje alto (0.9921) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.
- **Úlcera duodenal**: nivel L1, **Proceed with Guardrails**; evidencia directa de ECA, aunque varios ensayos registrados son de prevención o fueron retirados/terminados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

