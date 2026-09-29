---
layout: default
title: Deferiprone
parent: Evidencia Moderada (L3-L4)
nav_order: 153
evidence_level: L4
indication_count: 9
---

# Deferiprone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **9** 
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

# Deferiprona: De Indicación Original No Documentada a Porfiria Hepática

## Resumen en Una Frase

Deferiprona es un quelante oral de hierro, comercializado en Colombia como IROFIN® 500 mg tabletas recubiertas. Los datos de registro no detallan su indicación original.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática**,
pero hoy solo lo respaldan **0 ensayos clínicos** y **2 publicaciones preclínicas** en modelos de ratón.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No documentada. El registro solo consigna "DEFERIPRONA" (el principio activo), sin una indicación |
| Nueva Indicación Predicha | Porfiria hepática |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, deferiprona es un quelante oral de hierro. Su eficacia como quelante está establecida, y mecanísticamente podría ser aplicable a enfermedades en las que el hierro empeora el daño.

En la porfiria cutánea tarda, el hierro hepático elevado favorece la acumulación de uroporfirina. La flebotomía, que reduce el hierro, es un tratamiento eficaz. Por eso es biológicamente plausible que disminuir el hierro disponible con un quelante también ayude.

La evidencia recuperada tiene límites claros. Los dos estudios son en ratones: uno en un modelo de uroporfiria y otro en porfiria eritropoyética congénita. Esta última no es estrictamente una porfiria hepática, así que la extrapolación es indirecta. No se recuperaron datos de ensayos en humanos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Preclínico (modelo animal) | Blood | En un modelo de porfiria eritropoyética congénita, la quelación de hierro corrigió la anemia hemolítica y la fotosensibilidad cutánea |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Preclínico (modelo murino) | Hepatology | En ratones Hfe-/- con uroporfiria (modelo de porfiria cutánea tarda), compara la quelación con deferiprona frente a dietas deficientes en hierro para reducir la uroporfirina hepática |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20218402 | IROFIN® 500 MG TABLETAS RECUBIERTAS (ZONEPHARMA S.A.S.) | Tableta recubierta | DEFERIPRONA (sin indicación detallada) |

Nota: los datos reportan 12 registros en total, pero las entradas disponibles repiten el mismo número (20218402). Por eso se muestra una sola fila.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es alto (99.20%), pero la evidencia se limita a dos estudios preclínicos en ratones, sin ensayos clínicos. Además, uno de los estudios corresponde a una porfiria que no es estrictamente hepática, y no hay información de seguridad local disponible.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones. Verificar en particular el riesgo hematológico (neutropenia/agranulocitosis) descrito para esta clase de fármacos; este punto proviene de conocimiento general y no del Evidence Pack.
- Confirmar la indicación aprobada y el mecanismo de acción en DrugBank e INVIMA.
- Buscar estudios en humanos en porfiria cutánea tarda u otras porfirias hepáticas (series de casos, ensayos).
- Revisar la predicción de rango 8, beta-talasemia con otras manifestaciones. Deferiprona está autorizada en varias jurisdicciones para la sobrecarga de hierro transfusional en talasemia, así que podría ser un uso ya aprobado y no un reposicionamiento. Verificarlo con la indicación real del registro colombiano.
- Las otras siete predicciones (rangos 2 a 7 y 9) no tienen ensayos ni literatura recuperada. Se mantienen en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

