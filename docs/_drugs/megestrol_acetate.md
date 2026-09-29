---
layout: default
title: Megestrol Acetate
parent: Evidencia Alta (L1-L2)
nav_order: 272
evidence_level: L2
indication_count: 10
---

# Megestrol Acetate
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Acetato de Megestrol: De Indicación no detallada en el registro (texto "MEGESTROL") a Carcinoma Endometrial del Cuerpo Uterino

## Resumen en Una Frase

El acetato de megestrol es una progestina sintética comercializada en Colombia, pero el registro sanitario no detalla su indicación original: solo dice "MEGESTROL".
El modelo TxGNN predice que podría ser efectivo para el **carcinoma endometrial del cuerpo uterino**,
con **4 ensayos clínicos** (uno de ellos de Fase 2 aleatorizado y completado) y **ninguna publicación** asociada a esta indicación específica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | MEGESTROL (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Carcinoma endometrial del cuerpo uterino |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, el acetato de megestrol es una progestina sintética que actúa sobre los receptores de progesterona. Sus efectos de diferenciación celular y de freno a la proliferación son biológicamente plausibles en tumores endometrioides con receptores hormonales.

La relación con la indicación predicha es directa. El estrógeno estimula el crecimiento de las células del cáncer de endometrio, y la terapia con progestinas busca contrarrestar ese estímulo. Por eso se ha estudiado en hiperplasia atípica, neoplasia intraepitelial y cáncer endometrial temprano, incluso en mujeres que desean preservar la fertilidad.

Es probable que el beneficio se limite a enfermedad bien diferenciada y con receptores de progesterona positivos, o a contextos hormonalmente seleccionados. No se debe extrapolar a todos los subtipos de cáncer endometrial.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Fase 2 | Completado | 73 | Temsirolimus solo o combinado con terapia hormonal (acetato de megestrol + tamoxifeno) en cáncer de endometrio avanzado, persistente o recurrente |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Fase 2 | Terminado | 9 | Progestina continua vs secuencial (megestrol) en neoplasia intraepitelial endometrial con deseo de preservar el útero. Se terminó con solo 9 pacientes y no informa sobre eficacia |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Fase 1 temprana | Desconocido | 60 | Inhibidor de PD-1 más progesterona vs progesterona sola en cáncer endometrial temprano con preservación de la fertilidad. No se confirma cuál es la progestina |
| [NCT07462663](https://clinicaltrials.gov/study/NCT07462663) | Fase 4 | Aún no recluta | 80 | Estudio piloto SHAPE-ENDO: enfoque hormonal con prehabilitación vs cirugía inmediata en hiperplasia atípica o cáncer endometrioide de bajo riesgo con IMC ≥40. Sin resultados, y el agente específico no está confirmado |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

## Información de Mercado en Colombia

Las cinco filas del Evidence Pack corresponden al mismo registro y producto. Se muestran una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20004640 | MEGETRAL (AL PHARMA S.A.S.) | Tableta | MEGESTROL |

Los datos indican 8 registros en total, pero solo se recibió información de este producto.

## Citotoxicidad

El acetato de megestrol es un antineoplásico hormonal, no un citotóxico convencional. El Evidence Pack no trae datos de toxicidad de DrugBank, así que estos puntos son orientativos.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (progestina); no es citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función suprarrenal (la literatura describe supresión adrenal con dosis altas), parámetros de coagulación (efectos hemostáticos descritos con dosis altas) y la evaluación clínica habitual |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo aleatorizado de Fase 2 completado (n=73) que incluye terapia con megestrol en cáncer endometrial, y el mecanismo hormonal es plausible. Sin embargo, la evidencia directa es limitada. El otro ensayo de Fase 2 se terminó con 9 pacientes, y no hay publicaciones asociadas a esta indicación.

**Para avanzar se necesita:**
- Obtener del prospecto de INVIMA las advertencias y contraindicaciones, hoy sin datos.
- Complementar el mecanismo de acción desde DrugBank.
- Revisar los resultados de NCT00729586 para aislar la contribución del megestrol.
- Restringir el uso a enfermedad bien diferenciada con receptores de progesterona positivos, en contextos como la preservación de la fertilidad, con seguimiento clínico.
- Definir la indicación aprobada real del producto MEGETRAL.

**Nota sobre otras predicciones:** la única otra con evidencia relevante es **cáncer de ovario** (puesto 8, nivel L3). Tiene estudios históricos de Fase 2 de una sola rama con megestrol a dosis altas, incluso en enfermedad refractaria a platino, con actividad modesta. Se considera una pregunta de investigación, no una recomendación. Las demás predicciones no tienen respaldo clínico y quedan en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

