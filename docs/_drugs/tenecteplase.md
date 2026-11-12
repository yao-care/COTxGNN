---
layout: default
title: Tenecteplase
parent: Solo Predicción del Modelo (L5)
nav_order: 611
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
monitor_inn: "tenecteplase"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
description: "Tenecteplase: nueva indicación predicha, Congenital coronary artery anomaly (nivel de evidencia L5). Indicación original: TENECTEPLASA"
---

# Tenecteplase
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Tenecteplase: Congenital coronary artery anomaly
{: .text-alpha }

## Resumen en Una Frase

Tenecteplasa es un activador del plasminógeno tisular específico de la fibrina, utilizado como trombolítico; su registro sanitario en Colombia (Metalyse®) no detalla la indicación aprobada, más allá del nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **infarto de miocardio posteroinferior**, pero **no hay ensayos clínicos ni publicaciones** específicas que respalden esta indicación; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TENECTEPLASA |
| Nueva Indicación Predicha | Congenital coronary artery anomaly |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tenecteplasa es un activador del plasminógeno tisular específico de la fibrina que disuelve los trombos en arterias coronarias ocluidas, por lo que mecanísticamente podría ser aplicable al infarto de miocardio.

El infarto posteroinferior es un subtipo anatómico del infarto de miocardio. El uso establecido de tenecteplasa en infarto con elevación del ST es general y no específico de un subtipo. Por ello, esta predicción debe entenderse como un subconjunto de una indicación ya existente, y no como un reposicionamiento realmente novedoso.

### Otras indicaciones predichas (referencia)

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Comentario |
|------|------|------|------|
| Estenosis coronaria | 0.9953 | L5 | Estudios pequeños de tenecteplasa intracoronaria; señal de uso adyuvante en enfermedad coronaria trombótica |
| Anomalía coronaria congénita y otras (deleción 16p, talasemia beta, deficiencias enzimáticas eritrocitarias) | 0.9920–0.9961 | L5 | Sin vínculo mecanístico plausible; el puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para infarto de miocardio posteroinferior.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para infarto de miocardio posteroinferior.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19932170 | Metalyse® 10.000 U (50 mg) | Polvo liofilizado para reconstituir a solución inyectable | TENECTEPLASA | Vigente |

Fabricante: Boehringer Ingelheim International GmbH.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 137 interacciones registradas. Entre las principales:
  - **Gravedad mayor**: abciximab, apixabán, betrixabán, acalabrutinib, avapritinib, deferasirox, ibritumomab tiuxetán y tositumomab. En general implican mayor riesgo de sangrado.
  - **Gravedad moderada**: ácido acetilsalicílico, ibuprofeno, ketorolaco, celecoxib, diclofenaco tópico, ácido aminocaproico, ácidos grasos omega-3, fenfluramina, dexfenfluramina y sibutramina.

Para advertencias y contraindicaciones, consultar el prospecto. Por su mecanismo trombolítico, el riesgo de hemorragia es una preocupación central.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura específica para infarto de miocardio posteroinferior (nivel L5). La predicción parece corresponder a un subtipo de una indicación ya conocida.

<!-- review:begin co-lic-20261105-tenecteplase-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción parece corresponder a un subtipo de una indicación ya conocida, y el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-tenecteplase-2 -->

**Para avanzar se necesita:**
- Obtener el prospecto con advertencias y contraindicaciones
- Completar los datos del mecanismo de acción
- Evaluar si el infarto posteroinferior debe considerarse parte de la indicación general de infarto con elevación del ST
- Si se busca un reposicionamiento real, priorizar la estenosis coronaria (L3, uso intracoronario adyuvante), con estudios controlados y análisis de riesgo de sangrado

<!-- review:begin co-lic-20261031-tenecteplase-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la indicación aprobada de tenecteplasa en el registro sanitario y su situación regulatoria actual (registro cancelado) / Obtener el prospecto con advertencias y contraindicaciones" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-tenecteplase-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la indicación aprobada de tenecteplasa en el registro sanitario y su situación regulatoria actual (registro cancelado)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

