---
layout: default
title: Mupirocin
parent: Solo Predicción del Modelo (L5)
nav_order: 458
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
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
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 (cancelado) |
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
La predicción no cuenta con ensayos clínicos ni literatura (nivel L5), y la mupirocina tópica no alcanza concentraciones terapéuticas en el espacio pleural, donde el tratamiento estándar es drenaje y antibióticos sistémicos. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados desde DrugBank.
- Prospecto del INVIMA con advertencias y contraindicaciones, necesario para el tamizaje de seguridad.
- Evidencia preclínica o clínica que demuestre una vía de administración viable y concentraciones efectivas en el sitio de infección.
- Evaluación de compatibilidad de vía de administración (actualmente pendiente) y de similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

