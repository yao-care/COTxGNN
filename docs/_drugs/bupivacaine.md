---
layout: default
title: Bupivacaine
parent: Solo Predicción del Modelo (L5)
nav_order: 120
evidence_level: L5
indication_count: 4
---

# Bupivacaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Bupivacaína: De Anestesia Local a Acrodermatitis Crónica Atrófica

## Resumen en Una Frase

La bupivacaína es un anestésico local de tipo amida, registrado en Colombia bajo la denominación "BUPIVACAINA" en solución inyectable.
El modelo TxGNN predice que podría ser efectiva para **acrodermatitis crónica atrófica**, pero **no existe ningún ensayo clínico ni publicación** que respalde esta predicción: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | BUPIVACAINA (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Acrodermatitis crónica atrófica |
| Puntaje de Predicción TxGNN | 99.23% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, la bupivacaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje. Los datos farmacológicos compilados también la vinculan con otros canales iónicos (Nav1.5, Kv1.5, Kv4.3 y Kir3.2), aunque sin datos públicos de afinidad que lo confirmen.

**La predicción no es mecanísticamente plausible.** La acrodermatitis crónica atrófica es la manifestación cutánea tardía de la infección por *Borrelia* (enfermedad de Lyme) y se trata con antibióticos. Un bloqueador de canales de sodio no tiene un papel antiinfeccioso ni antiatrófico razonable. El puntaje alto (0.992) es solo una predicción derivada del modelo, sin respaldo de ensayos ni literatura, y la ausencia de datos de mecanismo limita aún más la evaluación.

Las otras predicciones del modelo tampoco tienen sustento mecanístico:

| Indicación predicha | Puntaje TxGNN | Observación |
|------|------|------|
| Dermatomiositis neonatal | 99.15% | Enfermedad inflamatoria inmunomediada; la bupivacaína es miotóxica a altas concentraciones o con exposición prolongada, lo que va en contra de un posible beneficio |
| Enfermedad pulmonar intersticial secundaria infantil asociada a enfermedad del tejido conectivo | 99.11% | Se maneja con inmunosupresión; el bloqueo de canales de sodio no actúa sobre esas vías; habría que resolver además aspectos de seguridad y dosificación pediátrica |
| Dermatomiositis amiopática | 99.03% | Impulsada por vías autoinmunes e interferón; la bupivacaína no tiene mecanismo inmunomodulador relevante |

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
| 20013329 (cancelado) | BUPINEST 0.75% PESADO | Solución inyectable | BUPIVACAINA |

Fabricante: Ropsohn Therapeutics S.A.S. Este es el único registro y se encuentra cancelado, por lo que actualmente no hay productos vigentes con bupivacaína en los datos compilados.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG):** estas relaciones provienen de una red de conocimiento y no del texto del prospecto. Incluyen:
  - **Cardiovasculares:** hipertensión, hipotensión, fibrilación auricular, enfermedad coronaria, infarto de miocardio, trombosis coronaria, paro cardíaco súbito y enfermedad de conducción cardíaca.
  - **Hepáticas y renales:** insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar y enfermedad renal.
  - **Respiratorias:** EPOC (incluida la de inicio temprano grave) e insuficiencia respiratoria.
  - **Endocrinas y metabólicas:** hipotiroidismo (incluidos mixedema y congénito), diabetes mellitus, cetoacidosis diabética y deficiencia de potasio.
  - **Otras:** epilepsia, enfermedad inflamatoria intestinal, hiperplasia prostática benigna, glaucoma de ángulo cerrado, hemoglobinopatías, piourete y abuso/dependencia de sustancias.
- **Interacciones y dianas farmacológicas:** se identificaron 4 dianas de canales iónicos (Nav1.5 humano, Kv1.5 humano, Kv4.3 de ratón y Kir3.2). No se dispone de una lista de interacciones con otros fármacos con nivel de gravedad. La relación con Nav1.5 (canal cardíaco) es coherente con la cardiotoxicidad conocida de la bupivacaína, por lo que conviene prestar atención al riesgo cardíaco.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre un bloqueador de canales de sodio y la acrodermatitis crónica atrófica, que es una enfermedad infecciosa tratada con antibióticos. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank).
- Descargar y analizar el prospecto en INVIMA para obtener advertencias y contraindicaciones oficiales (brecha de datos bloqueante para el tamizaje de seguridad).
- Estudios preclínicos o mecanísticos que justifiquen un posible efecto en la indicación predicha.
- Evaluar si tiene sentido continuar con esta candidata, dado que no hay registros vigentes en Colombia y que las demás predicciones del modelo tampoco tienen respaldo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

