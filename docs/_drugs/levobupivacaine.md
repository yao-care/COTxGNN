---
layout: default
title: Levobupivacaine
parent: Solo Predicción del Modelo (L5)
nav_order: 396
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Levobupivacaine: nueva indicación predicha, Gastroduodenitis (nivel de evidencia L5). Indicación original: Bupivacaína"
monitor_inn: "levobupivacaine"
predicted_indications: ["gastroduodenitis"]
---

# Levobupivacaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Levobupivacaína: De Bupivacaína (anestésico local) a Gastroduodenitis
{: .text-alpha }

## Resumen en Una Frase

La levobupivacaína es un anestésico local de acción prolongada; en Colombia su único registro sanitario (BUPINEST® 0.75 % solución inyectable) figura con la indicación "bupivacaína".
El modelo TxGNN predice que podría ser efectiva para **gastroduodenitis**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: la predicción se apoya solo en el modelo computacional.

<!-- review:begin co-lic-20261105-levobupivacaine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La levobupivacaína es un anestésico local de acción prolongada; en Colombia su único registro sanitario (BUPINEST® 0.75 % solución inyectable) figura con la indicación "bupivacaína" y se encuentra cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-levobupivacaine-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bupivacaína (anestésico local, según el registro INVIMA) |
| Nueva Indicación Predicha | Gastroduodenitis |
| Puntaje de Predicción TxGNN | 0.9909 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general (no proveniente de los datos), la levobupivacaína es un anestésico local de tipo amida y de acción prolongada que bloquea los canales de sodio dependientes de voltaje, impidiendo la conducción del impulso nervioso.

Un vínculo plausible, pero no verificado, sería una acción analgésica o antinociceptiva local sobre las fibras aferentes viscerales de la mucosa gastroduodenal. También se han descrito efectos antiinflamatorios de los anestésicos locales, pero no hay datos que los relacionen con la gastroduodenitis.

Existe además una barrera probable de vía de administración: la levobupivacaína se usa normalmente por infiltración, epidural o bloqueo nervioso, y no está establecida su administración tópica o sistémica al tracto digestivo superior. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y podría reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. La compatibilidad de vías de administración está pendiente de evaluar.

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
| 19902579 | BUPINEST® 0.75 % SIMPLE INYECTABLE | Solución inyectable | Bupivacaína | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no provienen del prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, miastenia gravis (incluida la de inicio en adultos), enfermedad de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular y cardiopatía.
- **Interacciones Farmacológicas**: se identificaron 62 interacciones en total. Entre las listadas:
  - *Moderadas*: aprepitant, cimetidina, claritromicina, ácido obeticólico, miconazol, clotrimazol, cobicistat, deferasirox, ticlopidina, fostamatinib, tiabendazol, primaquina, y los anestésicos tópicos lidocaína (tópica y oftálmica), benzocaína y cocaína.
  - *Menores*: dexametasona, omeprazol, hialuronidasa, albendazol.

Consultar el prospecto para información sobre advertencias y contraindicaciones de la etiqueta, ya que no se dispone de ella en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en un puntaje computacional alto (0.9909), sin ensayos clínicos ni literatura (nivel L5). Además, la vía de administración habitual no es compatible de forma evidente con la gastroduodenitis.

<!-- review:begin co-lic-20261105-levobupivacaine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y la vía de administración habitual no es compatible de forma evidente con la gastroduodenitis." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-levobupivacaine-2 -->

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente sin datos.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de literatura preclínica y clínica sobre anestésicos locales en gastroduodenitis o dolor visceral gastroduodenal.
- Evaluar la compatibilidad de vías de administración y la viabilidad de una formulación o vía adecuada para el tracto digestivo superior.
- Analizar las contraindicaciones del grafo (hepáticas, renales, cardiovasculares y neuromusculares) frente a la población objetivo.

<!-- review:begin co-lic-20261105-levobupivacaine-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Confirmar la situación regulatoria: el registro está cancelado, por lo que no hay producto vigente en Colombia. / Analizar las contraindicaciones del grafo (hepáticas, renales, cardiovasculares y neuromusculares) frente a la población objetivo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-levobupivacaine-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y se encuentra cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Confirmar la situación regulatoria: el registro está cancelado, por lo que no hay producto vigente en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

