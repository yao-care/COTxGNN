---
layout: default
title: Pentosan Polysulfate
parent: Solo Predicción del Modelo (L5)
nav_order: 508
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Pentosan Polysulfate: nueva indicación predicha, Trastorno primario de liberación plaquetaria (primary release disorde… (nivel de evidencia L5). Indicación original: Pentosano polisulfato de sodio"
---

# Pentosan Polysulfate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Pentosano Polisulfato: De Pentosano Polisulfato de Sodio a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

El pentosano polisulfato es un polisacárido sulfatado semisintético con actividad anticoagulante tipo heparina; en Colombia su registro sanitario solo indica el nombre del principio activo (pentosano polisulfato de sodio), sin una indicación clínica detallada.
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el modelo y, desde el punto de vista farmacológico, existen razones para dudar de ella.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Pentosano polisulfato de sodio (el registro no detalla una indicación clínica) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria (primary release disorder of platelets) |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, el pentosano polisulfato es un polisacárido sulfatado semisintético con actividad anticoagulante similar a la heparina y una débil actividad antitrombótica. Puede interferir con la coagulación y con la función plaquetaria.

En un trastorno de liberación (secreción) plaquetaria, el problema de fondo es que las plaquetas no funcionan adecuadamente y el paciente tiene tendencia al sangrado. Un fármaco que interfiere con la coagulación y la función plaquetaria actúa en sentido contrario a lo que se necesitaría, por lo que no se identificó un vínculo mecanístico terapéutico plausible.

El puntaje alto del modelo probablemente refleja la cercanía en la red de conocimiento con genes y fármacos relacionados con la hemostasia, y no un mecanismo terapéutico real. Además, el fármaco podría empeorar la tendencia al sangrado en estos pacientes.

### Otras predicciones del modelo (todas de nivel L5)

| Enfermedad predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Trombastenia de Glanzmann | 99.65% | Se debe a la deficiencia o disfunción de la integrina αIIbβ3. No se conoce ningún mecanismo por el que el fármaco restaure esta función, y su efecto anticoagulante agravaría el riesgo de sangrado. |
| Pseudoenfermedad de von Willebrand | 99.62% | Se debe a variantes con ganancia de función en GP1BA. Una interacción con el factor de von Willebrand o con glicoproteínas plaquetarias es solo teórica y especulativa, y existen preocupaciones de seguridad por sangrado. |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20177532 (cancelado) | PENTODOL 100 MG CAPSULA | Cápsula dura | Pentosano polisulfato de sodio |

El fabricante del registro es Inversiones Plamatech Ltda. No hay registros vigentes en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de PrimeKG, no provienen del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, trastornos de la coagulación sanguínea, hemofilia y trombocitopenia inducida por heparina.
- **Interacciones farmacológicas**: se registraron **58 interacciones** (nivel moderado en las mostradas), muchas de ellas con anticoagulantes y antiagregantes plaquetarios, lo que implica mayor riesgo de sangrado. Entre las principales se encuentran:
  - Ácido acetilsalicílico
  - Warfarina
  - Apixabán, edoxabán y betrixabán
  - Clopidogrel
  - Cilostazol y dipiridamol
  - Abciximab y cangrelor
  - Dalteparina
  - Alteplasa y anistreplasa
  - Bivalirudina
  - Defibrótido
  - Caplacizumab
  - Antitrombina III humana
  - Ibritumomab tiuxetán y tositumomab

Las contraindicaciones y advertencias del prospecto del INVIMA no están disponibles; se recomienda consultar el prospecto cuando se obtenga.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos clínicos ni literatura. Además, la actividad anticoagulante del fármaco va en contra de lo que requieren los trastornos plaquetarios y podría aumentar el riesgo de sangrado. Las contraindicaciones del grafo incluyen trastornos de la coagulación y trombocitopenia, y el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto del INVIMA (advertencias y contraindicaciones), un vacío que bloquea el tamizaje de seguridad.
- Consultar en DrugBank los datos del mecanismo de acción.
- Realizar una revisión de literatura y estudios preclínicos que justifiquen un posible vínculo mecanístico con la función plaquetaria.
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original (actualmente pendientes).
- Reevaluar la utilidad de continuar con esta línea frente a las otras predicciones (trombastenia de Glanzmann y pseudoenfermedad de von Willebrand), que presentan las mismas limitaciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

