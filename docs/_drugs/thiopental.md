---
layout: default
title: Thiopental
parent: Solo Predicción del Modelo (L5)
nav_order: 625
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
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

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11878 (cancelado) | TIOPENTAL 1 G. I.V. polvo para solución inyectable | Polvo estéril para reconstituir a solución inyectable | TIOPENTAL |

El único registro (fabricante: FEPARVI S.A.S.) está cancelado, por lo que actualmente no hay producto vigente con este principio activo en el registro consultado.

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
La predicción para tricotilomanía carece de ensayos clínicos, literatura y fundamento mecanístico. Además, el único registro sanitario en Colombia está cancelado y el perfil de seguridad del fármaco (anestésico de uso hospitalario) es exigente.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un fundamento biológico plausible para tricotilomanía.
- Estudios preclínicos que respalden la hipótesis antes de plantear estudios clínicos.
- Prospecto vigente con advertencias y contraindicaciones oficiales.
- Aclarar la situación regulatoria (registro cancelado) y la viabilidad de una vía de administración adecuada para un trastorno crónico.

**Otras indicaciones predichas con algo más de respaldo (referencia):** epilepsia del lóbulo frontal y epilepsia de ausencia (nivel L4, "pregunta de investigación"). La evidencia se limita a control agudo de crisis y pruebas prequirúrgicas. En epilepsia de ausencia, la potenciación de GABA-A podría incluso agravar las crisis. Otras predicciones del modelo (angina de Prinzmetal, migraña, síndrome de Tourette, dependencia de sustancias, entre otras) quedan en L5 sin sustento clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

