---
layout: default
title: Mupirocin
parent: Solo Predicción del Modelo (L5)
nav_order: 458
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Mupirocin: nueva indicación predicha, Empiema pleural (nivel de evidencia L5). Indicación original: Mupirocina"
monitor_inn: "mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
---

# Mupirocin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Mupirocina: De Indicación Registrada (Mupirocina tópica) a Empiema Pleural
{: .text-alpha }

## Resumen en Una Frase

Mupirocina es un antibiótico de uso tópico, registrado en Colombia bajo el producto PRESIDERM® (ungüento tópico), cuya indicación aprobada figura únicamente como "mupirocina".
El modelo TxGNN predice que podría ser efectivo para **empiema pleural**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mupirocina (el registro sanitario no detalla la indicación clínica) |
| Nueva Indicación Predicha | Empiema pleural |
| Puntaje de Predicción TxGNN | 0.9949 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 4) |
| Número de Registros Sanitarios | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la mupirocina es un antibacteriano tópico que inhibe la isoleucil-tRNA sintetasa bacteriana y es activo sobre todo contra cocos grampositivos, como *Staphylococcus aureus* (incluido el SARM) y estreptococos.

Estos microorganismos pueden causar empiema pleural, por lo que existe un vínculo antibacteriano teórico entre la indicación original y la nueva.

Sin embargo, el vínculo no es clínicamente aplicable. La mupirocina se formula para uso tópico, tiene exposición sistémica insignificante y se metaboliza rápidamente a ácido mónico inactivo, por lo que no alcanzaría concentraciones terapéuticas en el espacio pleural. El empiema pleural se maneja con drenaje y antibióticos sistémicos. El puntaje de TxGNN (0.9949) es solo una predicción computacional.

**Segunda predicción (referencia):** queratoconjuntivitis epitelial punteada (puntaje 0.9910, nivel L5, Hold). Su vínculo con la actividad antiestafilocócica es indirecto y solo aplicaría al subgrupo de origen bacteriano. El ungüento no está formulado ni aprobado para uso oftálmico, y sus excipientes (polietilenglicol) generan dudas de tolerabilidad ocular. Existen alternativas oftálmicas establecidas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19952603 | PRESIDERM® | Ungüento tópico | Mupirocina | Vigente |

Fabricante: MEGALABS COLOMBIA S.A.S.

---

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento (TxGNN/PrimeKG, no del prospecto):** dermatitis.
- **Interacciones farmacológicas:** se identificaron 118 posibles interacciones en la base consultada, pero ninguna tiene nivel de gravedad clasificado (todas "desconocido"). Entre las listadas figuran calcitriol, clotrimazol, morfina, metformina, pantoprazol, omeprazol, sucralfato, vancomicina, lactulosa, triamcinolona, prednisona y simvastatina. No deben interpretarse como interacciones clínicamente relevantes sin verificación adicional.

Para advertencias y contraindicaciones del producto, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura (nivel L5), y la mupirocina tópica no alcanza concentraciones terapéuticas en el espacio pleural, donde el tratamiento estándar es drenaje y antibióticos sistémicos.

<!-- review:begin co-lic-20261105-mupirocin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción no cuenta con ensayos clínicos ni literatura (nivel L5), y la mupirocina tópica no alcanza concentraciones terapéuticas en el espacio pleural, donde el tratamiento estándar es drenaje y antibióticos sistémicos. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 4 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-mupirocin-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados desde DrugBank.
- Prospecto del INVIMA con advertencias y contraindicaciones, necesario para el tamizaje de seguridad.
- Evidencia preclínica o clínica que demuestre una vía de administración viable y concentraciones efectivas en el sitio de infección.
- Evaluación de compatibilidad de vía de administración (actualmente pendiente) y de similitud con la indicación original.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

