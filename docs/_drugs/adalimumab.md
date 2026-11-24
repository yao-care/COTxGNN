---
layout: default
title: Adalimumab
parent: Solo Predicción del Modelo (L5)
nav_order: 27
evidence_level: L5
indication_count: 3
monitor_inn: "ADALIMUMAB"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
last_modified_at: 2026-11-24
description: "Adalimumab: nueva indicación predicha, hipermovilidad del coxis (hypermobility of coccyx) (nivel de evidencia L5). Indicación original: ADALIMUMAB"
---

# Adalimumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Adalimumab: anticuerpo monoclonal anti-TNF → hipermovilidad del coxis (hypermobility of coccyx)
{: .text-alpha }

## Resumen en Una Frase

Adalimumab es un anticuerpo monoclonal dirigido contra el factor de necrosis tumoral (TNF), con registros sanitarios en Colombia.
El modelo TxGNN predice que podría ser efectivo para **hipermovilidad del coxis (hypermobility of coccyx)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ADALIMUMAB |
| Nueva Indicación Predicha | hipermovilidad del coxis (hypermobility of coccyx) |
| Puntaje de Predicción TxGNN | 0,9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 11 de 11) |
| Número de Registros Sanitarios | 11 (vigentes: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Adalimumab (traducción no oficial): «Los productos de adalimumab se unen específicamente al TNF-alfa y bloquean su interacción con los receptores de TNF p55 y p75 de la superficie celular. Los productos de adalimumab también lisan in vitro las células que expresan TNF en su superficie en presencia del complemento.» Texto original en inglés: "Adalimumab products bind specifically to TNF-alpha and block its interaction with the p55 and p75 cell surface TNF receptors. Adalimumab products also lyse surface TNF expressing cells in vitro in the presence of complement." ([DailyMed: Simlandi (adalimumab-ryvk) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12f609c9-2088-bb05-e063-6394a90a9ecc), versión del 2026-11-11; consultado el 2026-11-19). Por conocimiento general, adalimumab bloquea el TNF, una citocina clave en procesos inflamatorios mediados por el sistema inmune.

La hipermovilidad del coxis es una condición mecánica o estructural. No se ha identificado un mecanismo inflamatorio dependiente de TNF que justifique el uso de adalimumab en ella. El puntaje alto del modelo (0,9977) es únicamente una señal computacional y no constituye evidencia clínica.

Por lo tanto, la plausibilidad mecanística es baja y requeriría una justificación biológica específica antes de cualquier avance.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20108951 | HUMIRA® AC | SOLUCION INYECTABLE | ADALIMUMAB | Vigente |
| 20149227 | AMGEVITA® | SOLUCION INYECTABLE | ADALIMUMAB | Vigente |
| 20169597 | ABRILADA® | SOLUCION INYECTABLE | ADALIMUMAB | Vigente |
| 20175556 | HYRIMOZ® 40MG | SOLUCION INYECTABLE | ADALIMUMAB | Vigente |
| 20177223 | IDACIO | SOLUCION INYECTABLE | ADALIMUMAB | Vigente |

Se muestran 5 de 11 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; se muestran las principales):
  - **Gravedad mayor**: corticosteroides (betametasona, budesonida, dexametasona, hidrocortisona, prednisolona, prednisona, triamcinolona), deferiprona, ibritumomab tiuxetán, iobenguano (I-131), tositumomab y tositumomab (I-131).
  - **Gravedad moderada**: metronidazol, tinidazol, rosuvastatina, simvastatina.
  - **Gravedad menor**: sales de zinc (acetato, gluconato, sulfato).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo, sin ensayos clínicos ni literatura sobre esta enfermedad, y sin un mecanismo TNF plausible para una condición mecánica del coxis. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Una hipótesis mecanística que vincule el TNF con la hipermovilidad del coxis
- Estudios preclínicos o series de casos que evalúen la señal
- Datos del prospecto (advertencias y contraindicaciones) de los productos con registro en Colombia
- Datos detallados del mecanismo de acción

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Simlandi (adalimumab-ryvk) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12f609c9-2088-bb05-e063-6394a90a9ecc) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

