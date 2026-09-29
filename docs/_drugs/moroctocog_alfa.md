---
layout: default
title: Moroctocog Alfa
parent: Solo Predicción del Modelo (L5)
nav_order: 291
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
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

# Moroctocog alfa: De Coagulación con Factor VIII a Trastorno de Liberación Primaria de las Plaquetas

## Resumen en Una Frase

Moroctocog alfa es un factor VIII de coagulación recombinante humano con el dominio B eliminado. En Colombia está registrado para la indicación "coagulación factor VIII", es decir, reposición de este factor.
El modelo TxGNN predice que podría ser efectivo para **trastorno de liberación primaria de las plaquetas**, con un puntaje muy alto (99.97%).
Sin embargo, hay **0 publicaciones** y los **7 ensayos clínicos** encontrados no evalúan este fármaco ni esta enfermedad (todos con relevancia baja, grado C), por lo que la predicción carece de respaldo real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Coagulación factor VIII |
| Nueva Indicación Predicha | Trastorno de liberación primaria de las plaquetas |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 16 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, moroctocog alfa es un factor VIII recombinante con el dominio B eliminado. Su función es reponer un factor plasmático de la coagulación en personas con deficiencia de factor VIII, y esa eficacia es la que sustenta su uso aprobado.

Los trastornos de liberación de las plaquetas son defectos propios de los gránulos plaquetarios o de su secreción. El factor VIII no corrige estos defectos, así que **no existe una relación mecanística directa** entre el fármaco y la nueva indicación.

El puntaje tan alto (0.9997) probablemente refleja la cercanía en el grafo de conocimiento a través de nodos como "trastorno hemorrágico", y no una coincidencia biológica real. La predicción debe leerse como una señal del modelo, no como una hipótesis terapéutica sólida.

---

## Evidencia de Ensayos Clínicos

Los ensayos encontrados corresponden a otros productos o a poblaciones sin relación con los trastornos plaquetarios. Ninguno estudia moroctocog alfa.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Fase 3 | Completado | 159 | Eficacia, seguridad y farmacocinética de otro FVIII (rFVIIIFc-VWF-XTEN, BIVV001) en hemofilia A grave, pacientes ≥12 años. No incluye pacientes con trastornos plaquetarios. |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Fase 3 | Completado | 74 | Seguridad de BIVV001 en niños <12 años con hemofilia A grave. Producto y población distintos. |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Fase 3 | Completado | 30 | FVIII pegilado (BAX 855) en hemofilia A grave sometida a cirugía u otros procedimientos invasivos. Otro producto y otra indicación. |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/D | Aún sin reclutar | 80 | Estudio observacional de perfiles clínico-hematológicos y de coagulación en leucemia mieloide aguda con quimioterapia de inducción. Sin relación con el fármaco. |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/D | Reclutando | 200 | Evaluación de laboratorio y síntomas en el síndrome posvacunación contra COVID-19. Sin relación. |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/D | Reclutando | 25 | Soporte hepático artificial (DPMAS + recambio plasmático) en insuficiencia hepática aguda sobre crónica y su efecto en la coagulación primaria. Sin relación. |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/D | Reclutando | 45 | Exploración de la hemostasia sistémica y portal en pacientes con derivación portosistémica intrahepática transyugular (TIPS). Sin relación. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Se muestran los registros únicos, porque el mismo registro aparece repetido en los datos. El paquete de evidencia lista solo 5 filas de los 16 registros totales.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20046519 | XYNTHA® 2000 UI | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factor VIII |
| 20005016 | XYNTHA® 500 UI polvo liofilizado para solución inyectable | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factor VIII |

Titular de ambos registros: PFIZER S.A.S.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5). No hay ensayos ni publicaciones que evalúen moroctocog alfa en trastornos de liberación plaquetaria, y el factor VIII no corrige ese defecto. Los ensayos de Fase 3 encontrados pertenecen a otros productos y a hemofilia A, así que no cuentan como respaldo.

**Para avanzar se necesita:**
- Verificar si el puntaje proviene de un artefacto del grafo (proximidad con nodos de "trastorno hemorrágico") y no de una relación biológica real.
- Completar el mecanismo de acción desde DrugBank y descargar el prospecto del INVIMA para revisar advertencias y contraindicaciones, que aún son un vacío bloqueante para el tamizaje de seguridad.
- Priorizar otras predicciones del mismo fármaco. Las candidatas plaquetarias (pseudo-enfermedad de von Willebrand, trombastenia de Glanzmann, síndrome de Scott, defecto del receptor de colágeno) tampoco tienen respaldo mecanístico. La deficiencia adquirida de factores de coagulación (hemofilia A adquirida) es la única con lógica de reposición de FVIII. Aun así, los inhibidores neutralizan el FVIII humano, y la evidencia de Fase 2/3 corresponde al análogo porcino (susoctocog alfa), que no es extrapolable.
- Verificar el término "flood factor deficiency" (rango 8), posible error de nomenclatura u ontología, antes de cualquier evaluación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

