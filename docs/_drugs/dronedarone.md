---
layout: default
title: Dronedarone
parent: Evidencia Moderada (L3-L4)
nav_order: 238
evidence_level: L3
indication_count: 10
---

# Dronedarone
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Dronedarona: De Fibrilación Auricular a Trastorno Cerebrovascular (Accidente Cerebrovascular)

> Nota: la indicación original registrada en INVIMA figura solo como "DRONEDARONA" (sin texto de indicación detallado). Según la literatura compilada, el uso conocido del fármaco es la fibrilación/aleteo auricular.

## Resumen en Una Frase

Dronedarona es un antiarrítmico multicanal, utilizado originalmente para la fibrilación y el aleteo auriculares.
El modelo TxGNN predice que podría ser efectivo para **accidente cerebrovascular (stroke disorder)**,
con **0 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, la mayoría revisiones y análisis post hoc sobre fibrilación auricular, no estudios específicos de ictus.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dronedarona (el registro no detalla el texto de indicación; uso conocido: fibrilación/aleteo auricular) |
| Nueva Indicación Predicha | Accidente cerebrovascular (stroke disorder) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la literatura, la dronedarona es un antiarrítmico multicanal (bloquea corrientes de Na⁺, K⁺ y Ca²⁺), análogo no yodado de la amiodarona, aprobado para fibrilación y aleteo auriculares.

La relación con el ictus es indirecta: la fibrilación auricular es una causa importante de ictus cardioembólico, por lo que el control del ritmo y la frecuencia podría reducir el riesgo. Análisis post hoc del ensayo ATHENA sugirieron una menor incidencia de ictus en fibrilación paroxística o persistente. Un estudio preclínico describe además efectos protectores frente a la lesión por isquemia/reperfusión en corazón y cerebro, y un estudio de laboratorio sugiere efectos anticoagulantes y antiplaquetarios independientes de la acción antiarrítmica.

Sin embargo, el ictus no fue un criterio principal de valoración en estos estudios, y el ensayo PALLAS en fibrilación auricular permanente mostró más ictus, insuficiencia cardíaca y muerte. El posible beneficio es, por tanto, indirecto y no está demostrado como efecto directo del fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Selección de las publicaciones más relevantes (prioridad: ECA/meta-análisis > cohortes > revisiones). Se incluyen las de la indicación principal y las de trastorno cerebrovascular que aportan datos específicos de ictus.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22149318](https://pubmed.ncbi.nlm.nih.gov/22149318/) | 2011 | Revisión sistemática/meta-análisis (post hoc ATHENA) | Am J Cardiovasc Drugs | Evalúa la reducción del riesgo de ictus con dronedarona en fibrilación auricular paroxística o persistente |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | Análisis post hoc de ECA | Clin Res Cardiol | Seguridad y eficacia de amiodarona y dronedarona en el control temprano del ritmo (EAST-AFNET 4) |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | ECA (PALLAS) | N Engl J Med | Dronedarona en fibrilación auricular permanente de alto riesgo; señal de seguridad con más eventos cardiovasculares |
| [25820938](https://pubmed.ncbi.nlm.nih.gov/25820938/) | 2015 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Antiarrítmicos para mantener el ritmo sinusal tras cardioversión de fibrilación auricular |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohorte | Circ Arrhythm Electrophysiol | Dronedarona frente a sotalol en veteranos con fibrilación auricular sin tratamiento antiarrítmico previo |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohorte | BMC Med | Uso concomitante de anticoagulantes orales directos y antiarrítmicos que interactúan: riesgo de ictus y sangrado |
| [20396635](https://pubmed.ncbi.nlm.nih.gov/20396635/) | 2010 | Revisión | Clin Interv Aging | Impacto de la dronedarona en la reducción de ictus en fibrilación y aleteo auriculares |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Estudio mecanístico | Atherosclerosis | Efectos anticoagulantes y antiplaquetarios independientes de la acción antiarrítmica |
| [22366819](https://pubmed.ncbi.nlm.nih.gov/22366819/) | 2012 | Preclínico (revisión) | Cardiovasc Drugs Ther | Efectos pleiotrópicos sobre la lesión por isquemia/reperfusión en corazón y cerebro |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Revisión | Lancet | Panorama del manejo de la fibrilación auricular y la estratificación del riesgo de ictus |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20014930 (cancelado) | MULTAQ® 400 MG tabletas recubiertas | Tableta recubierta | DRONEDARONA (sin texto de indicación detallado) |

Titular: Sanofi-Aventis de Colombia S.A. No hay registros vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN/PrimeKG, no texto de prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia hepática, deficiencia de potasio, bloqueo auriculoventricular y síndrome del seno enfermo (incluido el familiar).
- **Interacciones farmacológicas**: se identificaron 253 interacciones. Entre las de nivel **mayor** figuran hidrocortisona, anfotericina B (y sus formulaciones lipídicas, liposomal y de sulfato de colesterilo), loperamida, claritromicina, ácido picosulfúrico, polietilenglicol 3350 con electrolitos y dolasetrón. Entre las de nivel **moderado**: famotidina, alvimopán, aprepitant, dexametasona, bisacodilo, budesonida, cimetidina, saxagliptina y aceite de ricino.
- **Señales de la literatura**: más eventos cardiovasculares, ictus e insuficiencia cardíaca en fibrilación auricular permanente (PALLAS) y preocupación en insuficiencia cardíaca descompensada. Además, interacciones con anticoagulantes orales directos que pueden elevar sus niveles.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para ictus (L3) proviene de análisis secundarios y revisiones sobre fibrilación auricular, sin ensayos clínicos específicos ni mecanismo directo demostrado. Además, existen señales de seguridad relevantes y el producto no tiene registro vigente en Colombia.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Advertencias y contraindicaciones del prospecto de INVIMA
- Ensayos o estudios observacionales con el ictus como criterio principal, restringidos a poblaciones con fibrilación auricular no permanente y sin insuficiencia cardíaca descompensada
- Evaluación de seguridad (QT, función hepática, interacciones con anticoagulantes)
- Aclaración de la situación regulatoria local (registro cancelado)

**Otras predicciones del modelo:** "trastorno cerebrovascular" (99.71%, evidencia L2 con análisis post hoc de ATHENA) es la que cuenta con más respaldo y puede evaluarse en paralelo. Las demás (por ejemplo, amiloidosis ABri, obstrucción duodenal, sarcoglicanopatía, síndrome de Wildervanck) solo son predicciones sin evidencia ni vínculo mecanístico plausible, y el síndrome del seno enfermo tipo 2 plantea además un riesgo de seguridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

