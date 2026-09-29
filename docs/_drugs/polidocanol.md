---
layout: default
title: Polidocanol
parent: Solo Predicción del Modelo (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Polidocanol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Polidocanol: De Várices de Miembros Inferiores a Várices Esofágicas con Sangrado

## Resumen en Una Frase

Polidocanol es un agente esclerosante inyectable, cuyo uso aprobado descrito en la literatura es el tratamiento de várices y venas arácnidas de las piernas.
El modelo TxGNN predice que podría ser efectivo para **várices esofágicas con sangrado**,
con **7 ensayos clínicos** y **20 publicaciones** asociados a esta dirección. Solo 1 de esos ensayos prueba directamente lauromacrogol (polidocanol) en várices esofágicas, y la mayor parte de la literatura es antigua.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro INVIMA (el texto solo dice «POLIDOCANOL»). La literatura describe su uso aprobado en várices y venas arácnidas |
| Nueva Indicación Predicha | Várices esofágicas con sangrado |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L2 (ver nota abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** el paquete de evidencia asigna L1, pero solo hay un ensayo de Fase 3 completado (NCT00161915), y no se puede confirmar que incluya un brazo de polidocanol. Por eso no se cumple el criterio de L1 (≥2 ECAs de Fase 3 completados) y se asigna L2. La literatura incluye varios ECAs, pero son antiguos (1989-1999).

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos de mecanismo de acción en DrugBank. Aun así, el mecanismo de polidocanol está bien establecido: es un detergente esclerosante. Inyectado dentro o junto a una várice, daña el endotelio y provoca trombosis y fibrosis, con lo que obstruye el vaso.

Es el mismo mecanismo de su uso comercializado en várices de las piernas. Las várices esofágicas también son vasos dilatados que se pueden obliterar por esclerosis. La escleroterapia endoscópica de várices esofágicas, incluida la que usa lauromacrogol (el mismo compuesto que polidocanol), es una práctica clínica de larga data.

Por eso, el puntaje alto de TxGNN refleja en gran medida un uso ya conocido, más que un hallazgo nuevo. La práctica actual favorece la ligadura con bandas, y el papel de polidocanol frente a ella requiere confirmación comparativa.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02361593](https://clinicaltrials.gov/study/NCT02361593) | No aplica | Completado | 120 | Escleroterapia endoscópica con lauromacrogol asistida por capuchón transparente en várices esofágicas. Es el único ensayo que prueba el fármaco directamente en la indicación |
| [NCT00161915](https://clinicaltrials.gov/study/NCT00161915) | Fase 3 | Completado | No reportada | Sellante de fibrina vs. ligadura (con o sin polidocanol) para hemostasia y prevención de resangrado en várices esofágicas sangrantes |
| [NCT01923064](https://clinicaltrials.gov/study/NCT01923064) | No aplica | Completado | 96 | Cianoacrilato con lipiodol vs. cianoacrilato con lauromacrogol en várices gástricas. Apoyo indirecto |
| [NCT02468206](https://clinicaltrials.gov/study/NCT02468206) | No aplica | Completado | 64 | Cianoacrilato vs. BRTO para prevenir resangrado de várices gástricas. Solo contexto |
| [NCT02468167](https://clinicaltrials.gov/study/NCT02468167) | No aplica | Desconocido | 70 | Cianoacrilato vs. BRTO en sangrado agudo de várices gástricas. Solo contexto |
| [NCT02468180](https://clinicaltrials.gov/study/NCT02468180) | No aplica | Desconocido | 70 | Profilaxis primaria de sangrado de várices gástricas: cianoacrilato vs. BRTO. Solo contexto |
| [NCT05500625](https://clinicaltrials.gov/study/NCT05500625) | No aplica | Desconocido | 70 | Coil guiado por ecoendoscopia más cianoacrilato vs. BRTO en várices gástricas. Solo contexto |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9255525](https://pubmed.ncbi.nlm.nih.gov/9255525/) | 1997 | ECA | Endoscopy | Estudio prospectivo en pacientes cirróticos con várices esofágicas sangrantes: cianoacrilato más polidocanol o polidocanol solo, en manejo de emergencia y a largo plazo |
| [2693076](https://pubmed.ncbi.nlm.nih.gov/2693076/) | 1989 | ECA | Endoscopy | Etanolamina vs. polidocanol en 50 pacientes cirróticos. Erradicación de várices: 81% con etanolamina y 64.1% con polidocanol (diferencia no significativa) |
| [9514542](https://pubmed.ncbi.nlm.nih.gov/9514542/) | 1998 | Estudio comparativo | J Hepatol | Pegamento de fibrina vs. polidocanol para prevenir el resangrado temprano de várices esofágicas |
| [10385713](https://pubmed.ncbi.nlm.nih.gov/10385713/) | 1999 | ECA | Gastrointest Endosc | Ligadura sola vs. ligadura combinada con escleroterapia en várices esofágicas sangrantes |
| [10376453](https://pubmed.ncbi.nlm.nih.gov/10376453/) | 1999 | ECA | Endoscopy | Ligadura combinada con escleroterapia vs. ligadura sola para erradicar más rápido las várices sangrantes |
| [35879573](https://pubmed.ncbi.nlm.nih.gov/35879573/) | 2022 | Estudio prospectivo aleatorizado | Surg Endosc | Escleroterapia con compresión de balón vs. ligadura endoscópica de várices: comparación de tasa de erradicación y eficacia |
| [29473522](https://pubmed.ncbi.nlm.nih.gov/29473522/) | 2017 | Revisión | Curr Clin Pharmacol | Revisión de usos fuera de indicación de polidocanol, aprobado para várices y venas arácnidas |
| [36509625](https://pubmed.ncbi.nlm.nih.gov/36509625/) | 2023 | Cohorte | Arch Pediatr | Escleroterapia paravaricosa con polidocanol en várices cardiales de niños y adolescentes: evaluación de eficacia y seguridad |
| [6609102](https://pubmed.ncbi.nlm.nih.gov/6609102/) | 1984 | Cohorte | Gut | Con polidocanol al 3% (34 pacientes), 20 (59%) desarrollaron estenosis o disfagia esofágica |
| [32517718](https://pubmed.ncbi.nlm.nih.gov/32517718/) | 2020 | Revisión sistemática | BMC Gastroenterol | Riesgo agrupado de resangrado de várices gastroesofágicas tras cianoacrilato. Evidencia indirecta |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20018886 | ETOXIVEN® 3% | Solución inyectable | POLIDOCANOL |
| 20017789 | ETOXIVEN® 1% | Solución inyectable | POLIDOCANOL |

Ambos productos son del fabricante Franco Arango & Cía S.A.S. El registro no detalla la indicación en texto.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los datos de advertencias, contraindicaciones e interacciones no están disponibles. Como referencia, la literatura de escleroterapia con polidocanol describe estenosis y disfagia esofágica (59% en una cohorte de 34 pacientes, PMID 6609102) y sangrado gástrico posterior a la escleroterapia (PMID 1778718).

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La escleroterapia endoscópica con polidocanol/lauromacrogol en várices esofágicas tiene un mecanismo sólido y varios ECAs históricos. Sin embargo, la evidencia directa reciente es limitada (un solo ensayo directo, de fase NA) y faltan datos de seguridad del prospecto colombiano.

**Para avanzar se necesita:**
- Obtener del prospecto INVIMA las advertencias y contraindicaciones, un vacío bloqueante para el tamizaje de seguridad
- Confirmar si el brazo de polidocanol está presente en NCT00161915
- Verificar que la concentración y la forma inyectable de ETOXIVEN® 1% y 3% sean adecuadas para uso endoscópico
- Comparar polidocanol frente a la ligadura con bandas, que es el estándar actual
- Definir un plan de monitoreo de estenosis, disfagia y sangrado post-procedimiento

**Otras predicciones del modelo:** «várices esofágicas sin sangrado» (L2) queda como pregunta de investigación, porque la evidencia es sobre todo indirecta. Las otras 8 indicaciones predichas (enfermedades retinianas, monosomía X e hipoplasia inmunoeritromieloide) no tienen estudios ni vínculo mecanístico plausible, y quedan en Hold como probables artefactos del grafo de conocimiento.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Todo candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

