---
layout: default
title: Glimepiride
parent: Solo Predicción del Modelo (L5)
nav_order: 315
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Glimepiride: nueva indicación predicha, Síndrome de rigidez focal de las extremidades (nivel de evidencia L5). Indicación original: Metformina y sulfonilureas"
monitor_inn: "Glimepiride"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Glimepirida: De Metformina y Sulfonilureas a Síndrome de Rigidez Focal de las Extremidades

## Resumen en Una Frase

Glimepirida es una sulfonilurea utilizada originalmente en el tratamiento de la diabetes (registro sanitario colombiano asociado a "metformina y sulfonilureas").
El modelo TxGNN predice que podría ser efectivo para el **síndrome de rigidez focal de las extremidades**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Metformina y sulfonilureas |
| Nueva Indicación Predicha | Síndrome de rigidez focal de las extremidades |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la glimepirida es una sulfonilurea que cierra los canales de potasio sensibles a ATP (K-ATP) de las células beta pancreáticas para estimular la secreción de insulina.

El síndrome de rigidez focal de las extremidades es una variante del espectro de la persona rígida, un grupo de trastornos autoinmunes asociados a patología GABAérgica y a anticuerpos anti-GAD65. No se identifica un puente mecanístico plausible entre el cierre de canales K-ATP y esta enfermedad. La autoinmunidad anti-GAD se asocia con diabetes como comorbilidad, pero eso no sugiere un papel terapéutico de la glimepirida.

Por lo tanto, el puntaje alto del modelo debe interpretarse como una predicción puramente computacional, probablemente originada por la cercanía en la red de conocimiento con nodos relacionados con la diabetes, y no como una señal de eficacia clínica.

---

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20046981 | METGLITAL LEX 850/4 MG TABLETAS DE LIBERACIÓN PROLONGADA | Tableta de liberación prolongada | Metformina y sulfonilureas | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento asocia la glimepirida con enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, hipopituitarismo y otras deficiencias hipofisarias (incluida la deficiencia de hormona del crecimiento), hipogonadismo hipogonadotrópico (incluido el síndrome de Kallmann), síndrome de Sheehan, enfermedad del timo, osteoporosis (incluida la posmenopáusica) y enfermedades infecciosas.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total; la mayoría de las mostradas son de nivel moderado. Entre las principales se encuentran:
  - Agentes adrenérgicos/simpaticomiméticos: fenilefrina, epinefrina, pseudoefedrina, salbutamol, formoterol.
  - Betabloqueador: acebutolol.
  - Antiinflamatorios: ibuprofeno, ketorolaco, hidrocortisona.
  - Bloqueadores H2: famotidina, ranitidina.
  - Otros: acetazolamida, acitretina, etinilestradiol, hidroclorotiazida, nitazoxanida, albiglutida y etanol.
  - Las interacciones con corticoides tópicos (hidrocortisona tópica, alclometasona tópica) son de nivel menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto, ya que no se dispone de esa información en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que respalden el uso de glimepirida en el síndrome de rigidez focal de las extremidades, y no se identifica un mecanismo plausible. El puntaje del modelo (99.75%) es solo una predicción computacional (nivel L5). Además, el único registro sanitario colombiano está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y un análisis mecanístico que justifique la hipótesis.
- Obtener y analizar el prospecto de INVIMA para completar el tamizaje de seguridad (actualmente un vacío bloqueante).
- Estudios preclínicos que sustenten la hipótesis antes de considerar ensayos clínicos.
- Evaluar otras indicaciones predichas, aunque las revisadas también carecen de evidencia: síndrome de la persona rígida clásico, opsismodisplasia, síndrome de disfunción sensible a tiamina, distintas lipodistrofias localizadas y agenesia pancreática. En la agenesia pancreática, la glimepirida requiere células beta funcionales, por lo que no se esperaría eficacia.
- Confirmar la situación comercial en Colombia, dado que no hay registros vigentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

