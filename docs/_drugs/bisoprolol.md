---
layout: default
title: Bisoprolol
parent: Solo Predicción del Modelo (L5)
nav_order: 110
evidence_level: L5
indication_count: 5
---

# Bisoprolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Bisoprolol: De Bisoprolol y Tiazidas a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Bisoprolol es un bloqueador beta-1 selectivo, registrado en Colombia en combinación con tiazidas (producto ZIAC® 10 mg) para el tratamiento de la hipertensión.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta indicación; se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bisoprolol y tiazidas |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, bisoprolol es un bloqueador selectivo del receptor beta-1 adrenérgico (ADRB1), usado en hipertensión, angina crónica estable y algunas formas de insuficiencia cardíaca crónica estable. Su eficacia como antihipertensivo está bien establecida.

Mecanísticamente, el bloqueo beta-1 reduce la frecuencia cardíaca y el gasto cardíaco, y suprime la liberación de renina. Esto resulta biológicamente plausible en hipertensión dependiente de renina, como la renovascular. La relación con la indicación original (hipertensión tratada con bisoprolol y tiazidas) es la reducción de la presión arterial.

Sin embargo, la puntuación del modelo es solo una predicción computacional. La hipertensión maligna es habitualmente una emergencia que se maneja con fármacos intravenosos titulables, por lo que un betabloqueante oral sería, como mucho, un coadyuvante.

### Otras predicciones del modelo (todas con evidencia débil)

| Indicación Predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Enfermedad renal hipertensiva maligna | 99.94% | L5 | Sin ensayos ni literatura; considerar ajuste de dosis en insuficiencia renal |
| Hipertensión pulmonar de mecanismo multifactorial incierto | 99.93% | L5 | Los betabloqueantes se han evitado históricamente por el riesgo para la función del ventrículo derecho |
| Hipertensión pulmonar por enfermedad pulmonar o hipoxia | 99.93% | L4 | Solo evidencia indirecta (preclínica e insuficiencia cardíaca) |
| Síndrome de Braddock | 99.91% | L5 | Sin vínculo mecanístico; probable artefacto del grafo |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para hipertensión renovascular maligna.

---

## Evidencia de Literatura

No hay literatura disponible para la indicación principal (hipertensión renovascular maligna). Como referencia, la literatura indirecta disponible corresponde a la cuarta predicción (hipertensión pulmonar por enfermedad pulmonar o hipoxia); ninguna publicación estudia pacientes con hipertensión pulmonar:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Revisión | Cardiovasc Drugs Ther | Efectos de los betabloqueantes sobre la función pulmonar en insuficiencia cardíaca; se cuestiona la idea de que no estén indicados con función pulmonar alterada |
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Estudio clínico comparativo | Int J Cardiol | Comparación multiparamétrica de carvedilol, nebivolol y bisoprolol en insuficiencia cardíaca moderada (CARNEBI) |
| [23706341](https://pubmed.ncbi.nlm.nih.gov/23706341/) | 2013 | Estudio de fisiología clínica | J Am Soc Echocardiogr | Adaptación del ventrículo izquierdo a hipoxia aguda, con y sin bloqueo β1 |
| [18845967](https://pubmed.ncbi.nlm.nih.gov/18845967/) | 2008 | Estudio de fisiología clínica | Med Sci Sports Exerc | Bloqueo beta-adrenérgico y contribución del metabo-quimiorreflejo a la capacidad de ejercicio |
| [32363697](https://pubmed.ncbi.nlm.nih.gov/32363697/) | 2020 | Preclínico | Fundam Clin Pharmacol | Bisoprolol protege los cardiomiocitos de la lesión por isquemia-reperfusión vía PI3K/AKT/GSK3β |
| [27687650](https://pubmed.ncbi.nlm.nih.gov/27687650/) | 2016 | Preclínico (in vitro) | Nan Fang Yi Ke Da Xue Xue Bao | Efecto del pretratamiento con bisoprolol sobre la lesión por hipoxia/reoxigenación en cardiomiocitos H9c2 |
| [39088923](https://pubmed.ncbi.nlm.nih.gov/39088923/) | 2024 | Preclínico (animal) | Int Immunopharmacol | Diosmina y bisoprolol atenúan la cardiotoxicidad inducida por cloruro de cobalto |
| [12887136](https://pubmed.ncbi.nlm.nih.gov/12887136/) | 2003 | Reporte de caso | Hypertens Res | Dos casos de feocromocitoma asociado a tetralogía de Fallot |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 202329 (cancelado) | ZIAC® 10 MG (MERCK S.A.) | Tableta recubierta | Bisoprolol y tiazidas |

Actualmente no hay registros vigentes en Colombia; el único registro está cancelado.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: el grafo de conocimiento asocia bisoprolol con contraindicaciones en las siguientes condiciones: trastorno de ansiedad, trastorno neurótico, trastorno distímico, enfermedad renal, pionefrosis/piouréter, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico (incluido el pediátrico), asma (intrínseca y alérgica), deficiencia de potasio, psoriasis, parapsoriasis, diabetes mellitus, cetoacidosis diabética, hiperuricemia, hiperparatiroidismo, osteítis fibrosa, coma hepático, encefalopatía hepática, ictericia neonatal, anuria, gota, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo y miastenia gravis. Parte de esta lista probablemente refleja los componentes tiazídicos de la combinación y no el bisoprolol solo.
- **Interacciones Farmacológicas**: los datos disponibles solo confirman que bisoprolol actúa sobre el receptor β1-adrenérgico (ADRB1); no hay interacciones fármaco-fármaco específicas listadas.
- **Consideraciones específicas**: en hipertensión pulmonar existe preocupación por la reducción de la reserva contráctil del ventrículo derecho; en enfermedad renal hipertensiva se requeriría ajuste de dosis por eliminación renal y hepática.

No se dispone de advertencias del prospecto de INVIMA; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las predicciones son de nivel L5 (o L4 en el caso de hipertensión pulmonar por hipoxia, con evidencia solo indirecta), sin ensayos clínicos ni literatura directa. Además, el único registro en Colombia está cancelado y faltan los datos de seguridad del prospecto, por lo que no es posible avanzar.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío de datos bloqueante.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios clínicos o literatura específica sobre betabloqueantes en hipertensión renovascular o maligna.
- Evaluar el papel real de un betabloqueante oral frente al manejo estándar de la hipertensión maligna.
- Aclarar la situación regulatoria (registro cancelado) y la disponibilidad de bisoprolol en monoterapia en Colombia.
- Descartar o justificar con evidencia las predicciones de hipertensión pulmonar, dado el riesgo de seguridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

