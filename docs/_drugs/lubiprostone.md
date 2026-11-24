---
layout: default
title: Lubiprostone
parent: Solo Predicción del Modelo (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Lubiprostone: nueva indicación predicha, Alopecia (nivel de evidencia L5). Indicación original: Lubiprostona"
monitor_inn: "LUBIPROSTONE"
drugbank_id: DB01046
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "pulmonary hypertension", "kyphoscoliotic heart disease", "Raynaud disease", "pulmonary hypertension, primary, autosomal recessive", "phaeochromocytoma", "peripheral vascular disease"]
---

# Lubiprostone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Lubiprostona: De Estreñimiento Crónico a Alopecia
{: .text-alpha }

## Resumen en Una Frase

Lubiprostona es un activador del canal de cloruro ClC-2, conocido como agente de la clase de las prostonas, que cuenta con registros sanitarios en Colombia y cuyo uso clínico conocido es el tratamiento del estreñimiento crónico y del síndrome de intestino irritable.
El modelo TxGNN predice que podría ser efectivo para **alopecia**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

<!-- review:begin co-lic-20261105-lubiprostone-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Lubiprostona es un activador del canal de cloruro ClC-2, conocido como agente de la clase de las prostonas, que cuenta con registros sanitarios en Colombia (actualmente cancelados) y cuyo uso clínico conocido es el tratamiento del estreñimiento crónico y del síndrome de intestino irritable." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 registros sanitarios (vigentes: 3); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-lubiprostone-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lubiprostona (el registro sanitario solo consigna el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lubiprostone (traducción no oficial): «La lubiprostona es un activador de los canales de cloruro de acción local que potencia la secreción de un líquido intestinal rico en cloruro sin alterar las concentraciones séricas de sodio y potasio. La lubiprostona actúa mediante la activación específica de ClC-2, que es un componente normal de la membrana apical del intestino humano, de manera independiente de la proteína cinasa A.» Texto original en inglés: "Lubiprostone is a locally acting chloride channel activator that enhances a chloride-rich intestinal fluid secretion without altering sodium and potassium concentrations in the serum. Lubiprostone acts by specifically activating ClC-2, which is a normal constituent of the apical membrane of the human intestine, in a protein kinase A–independent fashion." ([DailyMed: Amitiza (lubiprostone) prescribing information, SpecGx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=164a2b47-0a52-4bb4-9e71-5342c2e951f4), versión del 2026-07-10; consultado el 2026-11-19). Según la información farmacológica conocida, lubiprostona es un activador del canal de cloruro ClC-2 (gen CLCN2), derivado de un metabolito de la prostaglandina E1, y se usa en estreñimiento crónico y síndrome de intestino irritable.

La relación con la alopecia es especulativa. La señalización de las prostaglandinas influye en el ciclo del cabello (los análogos de PGF2α favorecen el crecimiento y la PGD2 lo inhibe), pero no existe evidencia directa que vincule la activación de ClC-2 con la biología del folículo piloso. El puntaje alto de TxGNN refleja únicamente proximidad en la red de conocimiento.

Otras predicciones de la lista (hipotricosis congénita, hipotricosis simple del cuero cabelludo y alopecia areata difusa) parecen derivarse de la cercanía con otros fenotipos de pérdida de cabello. En la alopecia areata, de naturaleza autoinmune (vía JAK/STAT), lubiprostona no tiene acción inmunomoduladora conocida. Para hipertensión pulmonar, enfermedad de Raynaud y enfermedad vascular periférica existe un argumento débil por la clase de las prostanoides vasodilatadores, pero lubiprostona tiene absorción sistémica mínima y no se ha demostrado que actúe sobre receptores IP ni que produzca vasodilatación.

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
| 20028573 | MODULEX24MCG | CAPSULA BLANDA | CARBONO DIOXIDO PRODUCTOS FARMACOLOGICOS | Vigente |
| 20057095 | MOVIPROST ® 8 MCG | CAPSULA BLANDA | LUBIPROSTONE | Vigente |
| 20057097 | MOVIPROST® 24 MCG | CAPSULA BLANDA | LUBIPROSTONE | Vigente |

Se muestran los 3 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Se identificó una interacción de nivel **moderado** con **idelalisib** (fuente: DDInter). Además, la base farmacológica confirma como blanco principal el canal ClC-2 (CLCN2), sin que esto constituya una interacción con otro fármaco.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para alopecia se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin vínculo mecanístico directo entre la activación de ClC-2 y el folículo piloso.

<!-- review:begin co-lic-20261105-lubiprostone-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para alopecia se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin vínculo mecanístico directo entre la activación de ClC-2 y el folículo piloso. Además, no hay registros sanitarios vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 registros sanitarios (vigentes: 3); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-lubiprostone-2 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA para completar la revisión de advertencias y contraindicaciones (vacío bloqueante para el tamizaje de seguridad)
- Completar los datos del mecanismo de acción desde DrugBank
- Estudios preclínicos que evalúen el efecto de lubiprostona o de la vía ClC-2/prostanoides en el folículo piloso
- Evaluar la compatibilidad de vía de administración (la forma actual es oral en cápsula blanda, mientras que la alopecia suele requerir abordaje tópico o dirigido)
- Aclarar la situación regulatoria

<!-- review:begin co-lic-20261105-lubiprostone-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria, dado que los dos registros están cancelados" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 registros sanitarios (vigentes: 3); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-lubiprostone-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "(actualmente cancelados)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, no hay registros sanitarios vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que los dos registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Amitiza (lubiprostone) prescribing information, SpecGx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=164a2b47-0a52-4bb4-9e71-5342c2e951f4) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

