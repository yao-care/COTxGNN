---
layout: default
title: Bupivacaine
parent: Solo Predicción del Modelo (L5)
nav_order: 120
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-25
description: "Bupivacaine: nueva indicación predicha, Acrodermatitis crónica atrófica (nivel de evidencia L5). Indicación original: BUPIVACAINA"
monitor_inn: "Bupivacaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Bupivacaína: De Anestesia Local a Acrodermatitis Crónica Atrófica
{: .text-alpha }

## Resumen en Una Frase

La bupivacaína es un anestésico local de tipo amida, registrado en Colombia bajo la denominación "BUPIVACAINA" en solución inyectable.
El modelo TxGNN predice que podría ser efectiva para **acrodermatitis crónica atrófica**, pero **no existe ningún ensayo clínico ni publicación** que respalde esta predicción: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | BUPIVACAINA (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Acrodermatitis crónica atrófica |
| Puntaje de Predicción TxGNN | 0.9923 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Bupivacaine (traducción no oficial): «Los anestésicos locales bloquean la generación y la conducción de los impulsos nerviosos, presumiblemente al aumentar el umbral de excitación eléctrica del nervio, al ralentizar la propagación del impulso nervioso y al reducir la velocidad de ascenso del potencial de acción. En general, la progresión de la anestesia está relacionada con el diámetro, la mielinización y la velocidad de conducción de las fibras nerviosas afectadas.» Texto original en inglés: "Local anesthetics block the generation and the conduction of nerve impulses presumably by increasing the threshold for electrical excitation in the nerve, by slowing the propagation of the nerve impulse, and by reducing the rate of rise of the action potential. In general, the progression of anesthesia is related to the diameter, myelination, and conduction velocity of affected nerve fibers." ([DailyMed: Exparel (bupivacaine) prescribing information, Pacira Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bb5a9e59-0f51-11df-8a39-0800200c9a66), versión del 2026-11-09; consultado el 2026-11-19). Según la información conocida, la bupivacaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje. Los datos farmacológicos compilados también la vinculan con otros canales iónicos (Nav1.5, Kv1.5, Kv4.3 y Kir3.2), aunque sin datos públicos de afinidad que lo confirmen.

**La predicción no es mecanísticamente plausible.** La acrodermatitis crónica atrófica es la manifestación cutánea tardía de la infección por *Borrelia* (enfermedad de Lyme) y se trata con antibióticos. Un bloqueador de canales de sodio no tiene un papel antiinfeccioso ni antiatrófico razonable. El puntaje alto (0.9923) es solo una predicción derivada del modelo, sin respaldo de ensayos ni literatura, y la ausencia de datos de mecanismo limita aún más la evaluación.

Las otras predicciones del modelo tampoco tienen sustento mecanístico:

| Indicación predicha | Puntaje TxGNN | Observación |
|------|------|------|
| Dermatomiositis neonatal | 0.9915 | Enfermedad inflamatoria inmunomediada; la bupivacaína es miotóxica a altas concentraciones o con exposición prolongada, lo que va en contra de un posible beneficio |
| Enfermedad pulmonar intersticial secundaria infantil asociada a enfermedad del tejido conectivo | 0.9911 | Se maneja con inmunosupresión; el bloqueo de canales de sodio no actúa sobre esas vías; habría que resolver además aspectos de seguridad y dosificación pediátrica |
| Dermatomiositis amiopática | 0.9903 | Impulsada por vías autoinmunes e interferón; la bupivacaína no tiene mecanismo inmunomodulador relevante |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19931883 | BUPIVACAINA CLORHIDRATO SOLUCION INYECTABLE 50 MG / 10 ML | SOLUCION INYECTABLE | BUPIVACAINA | Vigente |
| 20013329 | BUPINEST 0.75% PESADO | SOLUCION INYECTABLE | BUPIVACAINA | Vigente |
| 52033 | BUPIROP 0.5% SIMPLEAMPOULEPACK | SOLUCION INYECTABLE | BUPIVACAINA | Vigente |
| 19908342 | LEVOBUPIVACAINA 0.75% SIMPLE SOLUCIÓNINYECTABLE | SOLUCION INYECTABLE | BUPIVACAINA | Temp. no comercializado - En Trámite Renov |
| 20148957 | BUPITROY0.5% | SOLUCION INYECTABLE | BUPIVACAINA | Temp. no comerc - Vigente |

Se muestran 5 de 6 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

<!-- review:begin co-lic-20261105-bupivacaine-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Fabricante: Ropsohn Therapeutics S.A.S. Este es el único registro y se encuentra cancelado, por lo que actualmente no hay productos vigentes con bupivacaína en los datos compilados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. También se eliminó la línea «Fabricante: Ropsohn Therapeutics S.A.S.», que describía solo el registro de la tabla anterior; los registros actuales tienen distintos titulares (tabla de Información de Mercado en Colombia). Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-bupivacaine-1 -->

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
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre un bloqueador de canales de sodio y la acrodermatitis crónica atrófica, que es una enfermedad infecciosa tratada con antibióticos.

<!-- review:begin co-lic-20261105-bupivacaine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre un bloqueador de canales de sodio y la acrodermatitis crónica atrófica, que es una enfermedad infecciosa tratada con antibióticos. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-bupivacaine-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank).
- Descargar y analizar el prospecto en INVIMA para obtener advertencias y contraindicaciones oficiales (brecha de datos bloqueante para el tamizaje de seguridad).
- Estudios preclínicos o mecanísticos que justifiquen un posible efecto en la indicación predicha.
- Evaluar si tiene sentido continuar con esta candidata, dado que las demás predicciones del modelo tampoco tienen respaldo.

<!-- review:begin co-lic-20261105-bupivacaine-3 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Evaluar si tiene sentido continuar con esta candidata, dado que no hay registros vigentes en Colombia y que las demás predicciones del modelo tampoco tienen respaldo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Actualizado el 2026-11-25: se reformuló el texto que quedó tras la eliminación para que la frase se lea completa. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-bupivacaine-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Este es el único registro y se encuentra cancelado, por lo que actualmente no hay productos vigentes con bupivacaína en los datos compilados" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-25 | «Evaluar si tiene sentido continuar con esta candidata, dado …» → «Evaluar si tiene sentido continuar con esta candidata, dado …» | Corregido (revisado el 2026-11-25; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Exparel (bupivacaine) prescribing information, Pacira Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bb5a9e59-0f51-11df-8a39-0800200c9a66) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

