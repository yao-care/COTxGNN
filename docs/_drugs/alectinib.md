---
layout: default
title: Alectinib
parent: Solo Predicción del Modelo (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# Alectinib: De Cáncer de Pulmón No Microcítico ALK-positivo a Fibromatosis Gingival

## Resumen en Una Frase

Alectinib es un inhibidor de tirosina quinasa (ALK/RET) usado en el cáncer de pulmón no microcítico (CPNM) ALK-positivo. La literatura del paquete de evidencia lo confirma; el registro sanitario solo indica "ALECTINIB" como texto de indicación.
El modelo TxGNN predice que podría ser efectivo para la **fibromatosis gingival**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CPNM ALK-positivo (según la literatura; el texto del registro INVIMA solo dice "ALECTINIB") |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 (todos con el mismo número, 20157000) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Alectinib inhibe las quinasas ALK y RET. Su uso establecido es el CPNM con reordenamiento ALK, donde los ensayos de fase 3 lo han comparado con crizotinib. No hay datos detallados de mecanismo de acción en DrugBank para este paquete.

**Esta predicción no tiene un respaldo mecanístico claro.** No se ha establecido ningún impulsor ALK o RET en la fibromatosis gingival, y no hay estudios clínicos ni preclínicos que relacionen el fármaco con esta enfermedad. El puntaje alto de TxGNN (99.97%, posición 489 del modelo) proviene solo de la estructura del grafo de conocimiento y no equivale a evidencia biológica.

Las propias predicciones vecinas del modelo (fibroma de pulmón, hamartoma de pulmón) tampoco tienen impulsor ALK conocido. Por eso conviene tratar este resultado como una hipótesis de bajo respaldo, no como un candidato listo para investigación clínica.

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
| 20157000 | ALECENSA (F. Hoffmann-La Roche Ltd., Basilea, Suiza) | Cápsula dura | Solo figura "ALECTINIB" (sin texto de indicación) |

Nota: el registro aparece cuatro veces con datos idénticos, por lo que se muestra una sola vez.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK/RET) |
| Riesgo de Mielosupresión | No hay datos formales de toxicidad en el paquete. La literatura describe anemia (usualmente leve) y un caso de anemia hemolítica. Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, triglicéridos (por el reporte de pancreatitis), peso corporal, función hepática y renal, y ECG (hay un estudio de electrofisiología cardíaca) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y las normas institucionales de manejo de antineoplásicos orales |

---

## Consideraciones de Seguridad

- **Señales de seguridad reportadas en la literatura recuperada (no provienen del prospecto):** anemia hemolítica, pancreatitis por hipertrigliceridemia, aumento de peso importante (alrededor del 10%), síndrome DRESS y eritema multiforme.

Consultar el prospecto para información de advertencias, contraindicaciones e interacciones, ya que el paquete no las trae de INVIMA.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción está en nivel L5. No hay ensayos ni publicaciones sobre fibromatosis gingival, y no existe un vínculo mecanístico conocido con ALK/RET.

**Para avanzar se necesita:**
- Evidencia biológica de que ALK o RET participan en la fibromatosis gingival, o estudios preclínicos que lo respalden.
- El prospecto de INVIMA con advertencias, contraindicaciones e interacciones, y los datos de mecanismo de acción de DrugBank.
- Aclarar el texto de indicación del registro sanitario, que hoy solo contiene el nombre del fármaco.
- Si se busca una línea con más sustento, priorizar otras predicciones del mismo fármaco. Por ejemplo, el tumor de células germinales de pulmón (posición 7) tiene un ensayo de fase 2/3 en reclutamiento y casos clínicos de tumores neuroendocrinos pulmonares con fusión ALK. Aun así, solo tendría sentido en pacientes con reordenamiento ALK documentado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

