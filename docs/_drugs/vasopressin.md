---
layout: default
title: Vasopressin
parent: Evidencia Moderada (L3-L4)
nav_order: 654
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
description: "Vasopressin: nueva indicación predicha, Deficiencia congénita de protrombina (nivel de evidencia L4). Indicación original: VASOPRESINA"
---

# Vasopressin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Vasopresina: De Vasopresina (indicación sin detallar) a Deficiencia Congénita de Protrombina

## Resumen en Una Frase

La vasopresina cuenta con registros sanitarios en Colombia como solución inyectable, aunque el texto de indicación registrado solo indica el nombre del principio activo ("VASOPRESINA") y no detalla un uso clínico específico.
El modelo TxGNN predice que podría ser efectiva para **deficiencia congénita de protrombina**, pero **no hay ensayos clínicos** y solo **3 publicaciones** indirectas (ninguna sobre protrombina) que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | VASOPRESINA (el registro no detalla una indicación clínica) |
| Nueva Indicación Predicha | Deficiencia congénita de protrombina |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la vasopresina y su análogo desmopresina (DDAVP) actúan sobre los receptores V2, lo que libera factor von Willebrand y factor VIII desde los depósitos endoteliales.

Este mecanismo es relevante para las deficiencias de factor VIII y de von Willebrand, pero **no tiene un vínculo establecido con la deficiencia de protrombina (factor II)**. El puntaje alto de TxGNN (0.996) probablemente refleja la cercanía en la red de conocimiento dentro del grupo de trastornos de la coagulación, más que un efecto mecanístico real sobre la protrombina.

La literatura recuperada trata sobre hemofilia A adquirida, deficiencia combinada de factores V/VIII y reemplazo de factor VIII en el embarazo. Es evidencia indirecta, relacionada con DDAVP y no con la vasopresina misma, y ninguna aborda la deficiencia de protrombina.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Revisión | Autoimmunity Reviews | Hemofilia A adquirida: enfermedad rara (~1 por millón/año) por autoanticuerpos contra el factor VIII, con mortalidad superior al 20%; revisa diagnóstico, etiología y opciones de tratamiento |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Reporte de caso | Rinsho Ketsueki | Administración de DDAVP en un paciente con deficiencia congénita combinada de factores V y VIII |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Reporte de caso | Rinsho Ketsueki | Manejo de cesárea con concentrados de factor VIII en una gestante con deficiencia congénita combinada de factores V y VIII |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20272748 | VESAPRESYN® SOLUCIÓN INYECTABLE | Solución inyectable | VASOPRESINA |
| 20096205 | VASOPRESINA 20 UI/1ML SOLUCIÓN INYECTABLE | Solución inyectable | VASOPRESINA |

Ambos registros figuran como cancelados.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 121 interacciones en total. Entre las listadas:
  - **Mayores**: dolasetrón, cisaprida, papaverina, macimorelina.
  - **Moderadas**: famotidina, epinefrina, loperamida, clorpropamida, claritromicina, ácido picosulfúrico, polietilenglicol (3350 con electrolitos), palonosetrón, sulfato de sodio, levofloxacino, ondansetrón, granisetrón, prometazina, cilostazol y heparina.
  - **Menores**: metronidazol.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en la proximidad computacional dentro de la red de conocimiento: no hay ensayos clínicos, la literatura es indirecta y no trata la deficiencia de protrombina, y no existe un vínculo mecanístico establecido. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la vasopresina para evaluar un posible vínculo con la protrombina.
- Evidencia preclínica o clínica directa en deficiencia de protrombina.
- Prospecto de INVIMA con advertencias y contraindicaciones para completar el análisis de seguridad (vacío bloqueante).
- Aclarar la situación regulatoria, dado que ambos registros están cancelados.

---

### Nota sobre la segunda predicción

**Osteoporosis inducida por fármacos** (puntaje TxGNN 99.62%, nivel de evidencia L5, decisión Hold): no hay ensayos clínicos ni literatura. La señalización por receptores V1/V2 en células óseas es solo especulativa en entornos preclínicos, y la hiponatremia asociada al exceso de vasopresina se ha vinculado con pérdida ósea, por lo que el efecto podría ser perjudicial y la dirección del efecto es incierta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

