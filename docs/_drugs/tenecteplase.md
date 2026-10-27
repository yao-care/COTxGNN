---
layout: default
title: Tenecteplase
parent: Solo Predicción del Modelo (L5)
nav_order: 611
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tenecteplase: nueva indicación predicha, Infarto de miocardio posteroinferior (nivel de evidencia L5). Indicación original: TENECTEPLASA"
monitor_inn: "tenecteplase"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
---

# Tenecteplase
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

## Tenecteplasa: De Tenecteplasa (indicación sin detallar en el registro) a Infarto de Miocardio Posteroinferior
{: .text-alpha }

## Resumen en Una Frase

Tenecteplasa es un activador del plasminógeno tisular específico de la fibrina, utilizado como trombolítico; su registro sanitario en Colombia (Metalyse®) no detalla la indicación aprobada, más allá del nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **infarto de miocardio posteroinferior**, pero **no hay ensayos clínicos ni publicaciones** específicas que respalden esta indicación; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TENECTEPLASA (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Infarto de miocardio posteroinferior |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tenecteplasa es un activador del plasminógeno tisular específico de la fibrina que disuelve los trombos en arterias coronarias ocluidas, por lo que mecanísticamente podría ser aplicable al infarto de miocardio.

El infarto posteroinferior es un subtipo anatómico del infarto de miocardio. El uso establecido de tenecteplasa en infarto con elevación del ST es general y no específico de un subtipo. Por ello, esta predicción debe entenderse como un subconjunto de una indicación ya existente, y no como un reposicionamiento realmente novedoso.

El puntaje de 99.87% es solo una predicción del modelo. No hay ensayos ni literatura específica para este subtipo que lo confirmen.

### Otras indicaciones predichas (referencia)

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Comentario |
|------|------|------|------|
| Infarto de miocardio posterolateral | 99.87% | L5 | Mismo mecanismo; probable subconjunto del infarto con elevación del ST |
| Infarto de miocardio septal | 99.85% | L4 | Solo literatura indirecta (embolia pulmonar, casos clínicos) |
| Estenosis coronaria | 99.53% | L3 | Estudios pequeños de tenecteplasa intracoronaria; señal de uso adyuvante en enfermedad coronaria trombótica |
| Anomalía coronaria congénita y otras (deleción 16p, talasemia beta, deficiencias enzimáticas eritrocitarias) | 99.20%–99.61% | L5 | Sin vínculo mecanístico plausible; probables artefactos del grafo de conocimiento |

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
| 19932170 | Metalyse® 10.000 U (50 mg) | Polvo liofilizado para reconstituir a solución inyectable | TENECTEPLASA | Cancelado |

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
No hay ensayos clínicos ni literatura específica para infarto de miocardio posteroinferior (nivel L5). La predicción parece corresponder a un subtipo de una indicación ya conocida, y el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Aclarar la indicación aprobada de tenecteplasa en el registro sanitario y su situación regulatoria actual (registro cancelado)
- Obtener el prospecto con advertencias y contraindicaciones
- Completar los datos del mecanismo de acción
- Evaluar si el infarto posteroinferior debe considerarse parte de la indicación general de infarto con elevación del ST
- Si se busca un reposicionamiento real, priorizar la estenosis coronaria (L3, uso intracoronario adyuvante), con estudios controlados y análisis de riesgo de sangrado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

