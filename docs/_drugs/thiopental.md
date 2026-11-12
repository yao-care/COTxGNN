---
layout: default
title: Thiopental
parent: Solo Predicción del Modelo (L5)
nav_order: 625
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-12
description: "Thiopental: nueva indicación predicha, Tricotilomanía (nivel de evidencia L5). Indicación original: TIOPENTAL"
monitor_inn: "thiopental"
predicted_indications: ["trichotillomania", "Prinzmetal angina", "migraine disorder", "Tourette syndrome", "migraine with brainstem aura", "obsolete bundle branch block", "substance abuse/dependence", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Thiopental
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Tiopental: De Uso Anestésico (indicación registrada sin detalle) a Tricotilomanía
{: .text-alpha }

## Resumen en Una Frase

Tiopental es un barbitúrico inyectable de acción corta. En su registro sanitario colombiano solo figura el nombre del producto como indicación, sin texto detallado.
El modelo TxGNN predice que podría ser efectivo para **tricotilomanía**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TIOPENTAL (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Tricotilomanía |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, el tiopental es un barbitúrico que potencia la señalización del receptor GABA-A, lo que produce depresión del sistema nervioso central.

Para la tricotilomanía **no se identifica un fundamento mecanístico claro**. Este trastorno se trata principalmente con terapia conductual (reversión de hábito) y con fármacos que actúan sobre vías serotoninérgicas, glutamatérgicas o dopaminérgicas, que no son el blanco del tiopental. El puntaje alto del modelo es solo una predicción computacional y no debe interpretarse como señal terapéutica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-thiopental-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El único registro (fabricante: FEPARVI S.A.S.) está cancelado, por lo que actualmente no hay producto vigente con este principio activo en el registro consultado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-thiopental-2 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11878 | TIOPENTAL 1 G. I.V. polvo para solución inyectable | Polvo estéril para reconstituir a solución inyectable | TIOPENTAL |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto):
  - Renal y hepático: enfermedad renal, insuficiencia renal, uremia, enfermedad hepática, enfermedad de la vesícula biliar.
  - Respiratorio: asma (intrínseca y alérgica).
  - Cardiovascular: trastornos hipotensivos.
  - Hematológico: anemia, incluida la macrocítica.
  - Endocrino: enfermedad de Addison e insuficiencia suprarrenal (varias formas, incluida la hiperplasia suprarrenal congénita), hipotiroidismo y mixedema.
  - Neuromuscular: miastenia gravis y enfermedades de la unión neuromuscular.
  - Porfirias: porfiria variegata y porfiria aguda intermitente.
- **Interacciones farmacológicas**: se identificaron 45 interacciones. Las de nivel **mayor** son:
  - **Etanol**
  - **Warfarina**

  Entre las de nivel moderado figuran morfina, codeína, hidrocodona, dextrometorfano, dronabinol, nabilona, cetirizina, carbinoxamina, clemastina, doxiciclina, azul de metileno, nitisinona y yoduro I-131 e I-123. Las de nivel menor incluyen piridoxina, cimetidina, sulfasalazina y prometazina. Varias combinaciones implican depresión aditiva del SNC.

No se dispone de advertencias ni contraindicaciones del prospecto; se recomienda consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para tricotilomanía carece de ensayos clínicos, literatura y fundamento mecanístico. Además, el perfil de seguridad del fármaco (anestésico de uso hospitalario) es exigente.

<!-- review:begin co-lic-20261105-thiopental-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y el perfil de seguridad del fármaco (anestésico de uso hospitalario) es exigente." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-thiopental-3 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un fundamento biológico plausible para tricotilomanía.
- Estudios preclínicos que respalden la hipótesis antes de plantear estudios clínicos.
- Prospecto vigente con advertencias y contraindicaciones oficiales.

<!-- review:begin co-lic-20261031-thiopental-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Prospecto vigente con advertencias y contraindicaciones oficiales. / Aclarar la situación regulatoria (registro cancelado) y la viabilidad de una vía de administración adecuada para un trastorno crónico." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-thiopental-1 -->

**Otras indicaciones predichas con algo más de respaldo (referencia):** epilepsia del lóbulo frontal y epilepsia de ausencia (nivel L4, "pregunta de investigación"). La evidencia se limita a control agudo de crisis y pruebas prequirúrgicas. En epilepsia de ausencia, la potenciación de GABA-A podría incluso agravar las crisis. Otras predicciones del modelo (angina de Prinzmetal, migraña, síndrome de Tourette, dependencia de sustancias, entre otras) quedan en L5 sin sustento clínico.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registro cancelado) y la viabilidad de una vía de administración adecuada para un trastorno crónico" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "El único registro (fabricante: FEPARVI S.A.S.) está cancelado, por lo que actualmente no hay producto vigente con este principio activo en e" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

