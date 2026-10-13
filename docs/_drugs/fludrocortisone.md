---
layout: default
title: Fludrocortisone
parent: Solo Predicción del Modelo (L5)
nav_order: 292
evidence_level: L5
indication_count: 8
---

# Fludrocortisone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Fludrocortisona: De Fludrocortisona (sin indicación específica registrada) a Enfermedad Ocular

> Nota: la primera predicción por puntaje del modelo es el linfoma cutáneo primario de células T, pero no cuenta con ninguna evidencia. Por ello, este informe se centra en la predicción con soporte bibliográfico, **enfermedad ocular** (posición 6 en el ranking), y menciona las demás en el contexto.

## Resumen en Una Frase

Fludrocortisona es un corticoide con acción principalmente mineralocorticoide, cuyos registros sanitarios en Colombia solo mencionan el nombre del principio activo, sin una indicación específica detallada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad ocular** (puntaje de 99.14%), con **0 ensayos clínicos** y **20 publicaciones** de relevancia heterogénea, la mayoría tangencial.
La evidencia directa es muy limitada: un estudio preclínico en degeneración retiniana y un estudio de fase 1B en atrofia geográfica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fludrocortisona (el registro no detalla una indicación clínica) |
| Nueva Indicación Predicha | Enfermedad ocular (eye disease) |
| Puntaje de Predicción TxGNN | 99.14% |
| Nivel de Evidencia | L4 (estudios preclínicos y de mecanismo) |
| Estado de Mercado en Colombia | Solo cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold (con la enfermedad ocular como pregunta de investigación; conviene acotarla, por ejemplo a degeneración retiniana) |

**Sobre la predicción de mayor puntaje:** el linfoma cutáneo primario de células T (99.58%) y las otras seis predicciones (quiste teratoma, quiste dermoide espinal, quiste dermoide de ovario, enfermedad de la parte orbitaria de los anexos oculares, enfermedad de la región orbitaria y exostosis) no tienen ensayos ni literatura y son nivel L5. Varias parecen artefactos del grafo de conocimiento. La decisión para ellas es **Hold**.

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, fludrocortisona es un mineralocorticoide con cierta actividad glucocorticoide, de uso establecido en insuficiencia suprarrenal e hipotensión ortostática. Mecanísticamente podría ser aplicable a enfermedades oculares por una vía inflamatoria y neuroprotectora, aunque esto es una inferencia y no está demostrado clínicamente.

El respaldo más directo es un estudio preclínico de 2021 (PMID 34509498) que describe propiedades antiinflamatorias y neuroprotectoras de fludrocortisona en degeneración retiniana, mediante la modulación de citocinas de las células de Müller. Además, un estudio de fase 1B (PMID 36161841) evaluó la seguridad de fludrocortisona intravítrea en atrofia geográfica. Otro hilo indirecto es su uso en glaucoma, para corregir la hipotensión sistémica y las caídas de presión arterial.

Gran parte de la literatura recuperada trata de trastornos autonómicos y suprarrenales, o de acidosis tubular renal en síndrome de Sjögren, y parece coincidir solo por palabras clave. "Enfermedad ocular" es demasiado inespecífico como indicación definida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación. El estudio de fase 1B citado en la literatura (PMID 36161841) no aparece como ensayo registrado en los datos compilados.

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (de las 20 recuperadas):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34509498](https://pubmed.ncbi.nlm.nih.gov/34509498/) | 2021 | Preclínico/Experimental | Experimental Eye Research | Fludrocortisona y triamcinolona reducen la expresión de citocinas proinflamatorias en células de Müller en degeneración retiniana |
| [36161841](https://pubmed.ncbi.nlm.nih.gov/36161841/) | 2022 | Estudio de fase 1B | BMJ Open Ophthalmology | Evalúa seguridad y tolerabilidad de fludrocortisona intravítrea (1 mg y 2 mg) en atrofia geográfica secundaria a DMAE |
| [11008895](https://pubmed.ncbi.nlm.nih.gov/11008895/) | 1999 | Estudio clínico | International Ophthalmology | Efectos hemodinámicos sistémicos de fludrocortisona en pacientes con glaucoma de ángulo abierto e hipotensión |
| [17998043](https://pubmed.ncbi.nlm.nih.gov/17998043/) | 2007 | Revisión | Survey of Ophthalmology | Tratamientos de glaucoma más allá de la presión intraocular; algunos médicos usan sal o fludrocortisona para evitar caídas de presión arterial |
| [23430676](https://pubmed.ncbi.nlm.nih.gov/23430676/) | 2013 | Revisión | Klinische Monatsblätter für Augenheilkunde | Terapias de glaucoma que no reducen la presión intraocular, incluida fludrocortisona |
| [15934882](https://pubmed.ncbi.nlm.nih.gov/15934882/) | 2005 | Revisión | Expert Opinion on Pharmacotherapy | Tratamientos farmacológicos de la disautonomía familiar |
| [31994621](https://pubmed.ncbi.nlm.nih.gov/31994621/) | 2019 | Revisión | Rev Assoc Med Bras | Síndrome poliglandular autoinmune tipo 2 (enfermedad de Addison con enfermedad tiroidea y/o diabetes tipo 1) |
| [38831360](https://pubmed.ncbi.nlm.nih.gov/38831360/) | 2024 | Cohorte/Observacional | Advances in Rheumatology | Hipocitraturia como biomarcador de acidosis tubular renal en enfermedad de Sjögren |
| [25354755](https://pubmed.ncbi.nlm.nih.gov/25354755/) | 2015 | Sin clasificar | Rheumatology (Oxford) | Prevalencia de acidosis tubular renal distal en Sjögren primario; prueba de acidificación con furosemida y fludrocortisona |
| [16331052](https://pubmed.ncbi.nlm.nih.gov/16331052/) | 2006 | Reporte de caso | Cornea | Queratitis por deficiencia de células madre en deficiencia endocrina múltiple |

Las demás publicaciones recuperadas (Parkinson no motor, Addison en SIDA, retinopatía en monos, entre otras) aportan evidencia solo tangencial.

## Información de Mercado en Colombia

Los tres registros están cancelados; actualmente no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20176766 | FLORINEF® 0.1 MG TABLETAS | Tableta | Fludrocortisona (cancelado) |
| 20168629 | FLOCURTIN® 0.1 MG TABLETAS | Tableta | Fludrocortisona (cancelado) |
| 27649 | ASTONIN® H TABLETAS | Tableta | Fludrocortisona (cancelado) |

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** se identificaron 446 interacciones potenciales. Entre las principales, la de **bupropión** es de nivel Mayor. Las de nivel Moderado incluyen antidiabéticos (acarbosa, pioglitazona, alogliptina, canagliflozina, dapagliflozina, empagliflozina, linagliptina, clorpropamida, albiglutida, dulaglutida), anfotericina B (incluida su forma de complejo lipídico), aprepitant, ácido acetilsalicílico, claritromicina, laxantes (bisacodilo, ácido picosulfúrico) y esteroides anabólicos (oxandrolona, oximetolona).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de enfermedad ocular solo cuenta con respaldo preclínico y un estudio de fase 1B de seguridad, sin ensayos clínicos registrados, y el término es demasiado amplio. Además, ningún producto con fludrocortisona está vigente en Colombia.

**Para avanzar se necesita:**
- Acotar la indicación a una condición específica (por ejemplo, degeneración retiniana o atrofia geográfica)
- Datos del mecanismo de acción de fludrocortisona (receptor mineralocorticoide y glucocorticoide en la retina)
- Resultados de eficacia en estudios posteriores al de fase 1B, y evaluación de la vía de administración (intravítrea frente a oral)
- Revisar el prospecto para obtener advertencias y contraindicaciones, y evaluar el perfil de seguridad de un uso oftálmico
- Evaluar la situación regulatoria, dado que los tres registros sanitarios están cancelados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

