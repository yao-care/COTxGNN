---
layout: default
title: Mepivacaine
parent: Solo Predicción del Modelo (L5)
nav_order: 428
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Mepivacaine: nueva indicación predicha, Gastroduodenitis (nivel de evidencia L5). Indicación original: Mepivacaína combinaciones"
monitor_inn: "mepivacaine"
predicted_indications: ["gastroduodenitis", "peptic ulcer disease"]
---

# Mepivacaine
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

## Mepivacaína: De Anestésico Local (Combinaciones de Mepivacaína) a Gastroduodenitis
{: .text-alpha }

## Resumen en Una Frase

La mepivacaína es un anestésico local de tipo amida, registrado en Colombia bajo la indicación genérica "Mepivacaína combinaciones" (producto ODONTOCAINA® 2%, solución inyectable).
El modelo TxGNN predice que podría ser efectiva para **gastroduodenitis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mepivacaína combinaciones |
| Nueva Indicación Predicha | Gastroduodenitis |
| Puntaje de Predicción TxGNN | 0.9949 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Mepivacaine (traducción no oficial): «Los anestésicos locales bloquean la generación y la conducción de los impulsos nerviosos, presumiblemente al aumentar el umbral de excitación eléctrica en el nervio, al ralentizar la propagación del impulso nervioso y al reducir la velocidad de ascenso del potencial de acción. En general, la progresión de la anestesia está relacionada con el diámetro, la mielinización y la velocidad de conducción de las fibras nerviosas afectadas.» Texto original en inglés: "Local anesthetics block the generation and the conduction of nerve impulses, presumably by increasing the threshold for electrical excitation in the nerve, by slowing the propagation of the nerve impulse, and by reducing the rate of rise of the action potential. In general, the progression of anesthesia is related to the diameter, myelination, and conduction velocity of affected nerve fibers." ([DailyMed: Polocaine-Mpf (mepivacaine hydrochloride) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a27d0815-ae6b-4a21-a8f5-564c01e83814), versión del 2022-10-01; consultado el 2026-11-19). Según la información conocida, la mepivacaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje, y su uso está establecido para la anestesia local (en este caso, en presentación odontológica inyectable).

La relación con la gastroduodenitis es débil. De manera especulativa, un anestésico local podría aliviar el dolor de la mucosa, pero esto no está respaldado por ningún ensayo ni publicación. El bloqueo de canales de sodio no tiene un papel reconocido en la cicatrización de la mucosa gastroduodenal ni en la supresión ácida, y el uso sistémico u oral para inflamación gastroduodenal no está establecido.

Por lo tanto, el puntaje alto de TxGNN (0.9949) debe interpretarse solo como una señal computacional que requiere validación, no como evidencia de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para gastroduodenitis.

*Nota: para la segunda predicción del modelo (enfermedad ulcerosa péptica), la única publicación recuperada (PMID 6890367, 1982) es un estudio en animales sobre farmacología de seguridad de la lofexidina, un fármaco distinto; no aporta evidencia sobre la mepivacaína.*

<!-- review:begin co-lic-20261105-mepivacaine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El fabricante es Productora y Comercializadora Odontológica New Stetic S.A. Actualmente no hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-mepivacaine-1 -->

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19933337 | ODONTOCAINA ® 2% | SOLUCION INYECTABLE | MEPIVACAINA COMBINACIONES | Vigente |
| 19935278 | ODONTOCAINA 3% | SOLUCION INYECTABLE | MEPIVACAINA | Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, miastenia gravis (incluida la de inicio en adultos), enfermedad de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular y enfermedad cardíaca.
- **Interacciones Farmacológicas**: se identificaron 11 interacciones.
  - Moderadas (10): morfina liposomal, lidocaína (tópica y oftálmica), benzocaína (tópica), cocaína (tópica y nasal), tetracaína (oftálmica y tópica), oxibuprocaína (oftálmica) y cinchocaína (tópica). En general corresponden a la combinación con otros anestésicos locales o depresores, con posible efecto aditivo.
  - Menores (1): hialuronidasa.

No se dispone de las advertencias y contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5), sin ensayos clínicos ni literatura pertinente, y no existe un vínculo mecanístico plausible entre el bloqueo de canales de sodio y la gastroduodenitis.

<!-- review:begin co-lic-20261105-mepivacaine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción es solo computacional (L5), sin ensayos clínicos ni literatura pertinente, y no existe un vínculo mecanístico plausible entre el bloqueo de canales de sodio y la gastroduodenitis. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-mepivacaine-2 -->

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción (MOA) desde DrugBank
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), indispensable antes de cualquier evaluación de seguridad
- Estudios preclínicos que justifiquen un mecanismo plausible en mucosa gastroduodenal
- Definir la vía de administración requerida y su compatibilidad con la presentación inyectable disponible
- Evaluar si existe alguna presentación vigente en Colombia

<!-- review:begin co-lic-20261105-mepivacaine-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar si existe alguna presentación vigente en Colombia, dado que el único registro está cancelado" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-mepivacaine-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "El fabricante es Productora y Comercializadora Odontológica New Stetic S.A. Actualmente no hay registros vigentes en Colombia" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que el único registro está cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Polocaine-Mpf (mepivacaine hydrochloride) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a27d0815-ae6b-4a21-a8f5-564c01e83814) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

